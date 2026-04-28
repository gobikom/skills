#!/usr/bin/env python3
"""Generate platform-specific skill adapters from prompts/ source of truth.

Usage:
    python3 scripts/generate-adapters.py          # Generate all adapters
    python3 scripts/generate-adapters.py codex    # Generate only codex adapter
    python3 scripts/generate-adapters.py --clean  # Remove adapters/ before generating

Reads: prompts/*.md + adapters.yml
Writes: adapters/{platform}/{skill files}
"""

import os
import re
import sys
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
CONFIG_PATH = ROOT / "adapters.yml"
ADAPTERS_DIR = ROOT / "adapters"


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def parse_prompt(path: Path) -> tuple[dict, str]:
    """Parse a prompt file into (frontmatter_dict, body_text)."""
    text = path.read_text()
    match = re.match(r"^---\n(.+?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError(f"No YAML frontmatter in {path}")
    fm = yaml.safe_load(match.group(1))
    body = match.group(2).lstrip("\n")
    return fm, body


def replace_args_placeholder(body: str, target_placeholder: str) -> str:
    """Replace $ARGUMENTS with the target platform's placeholder."""
    if target_placeholder == "$ARGUMENTS":
        return body
    return body.replace("$ARGUMENTS", target_placeholder)


def generate_claude_code(fm: dict, body: str, config: dict, skill_name: str) -> str:
    """Generate Claude Code SKILL.md with full frontmatter (allowed-tools, paths)."""
    lines = ["---"]
    lines.append(f"name: {fm['name']}")
    lines.append(f"description: {fm['description']}")
    lines.append(f'argument-hint: "{fm["argument-hint"]}"')

    allowed_tools = config.get("allowed_tools", {}).get(skill_name, [])
    if allowed_tools:
        lines.append("allowed-tools:")
        for tool in allowed_tools:
            lines.append(f"  - {tool}")

    paths = fm.get("paths", [])
    if paths:
        lines.append("paths:")
        for p in paths:
            lines.append(f'  - "{p}"')

    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines)


def generate_claude_skills(fm: dict, body: str, config: dict, skill_name: str) -> str:
    """Generate Claude Skills SKILL.md (no allowed-tools, has paths)."""
    lines = ["---"]
    lines.append(f"name: {fm['name']}")
    lines.append(f"description: {fm['description']}")
    lines.append(f'argument-hint: "{fm["argument-hint"]}"')

    paths = fm.get("paths", [])
    if paths:
        lines.append("paths:")
        for p in paths:
            lines.append(f'  - "{p}"')

    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines)


def generate_codex(fm: dict, body: str, config: dict, skill_name: str) -> str:
    """Generate Codex SKILL.md with name, description, metadata."""
    skills_config = config.get("_skills", {}).get(skill_name, {})
    short_desc = skills_config.get("short-description", fm["name"])

    lines = ["---"]
    lines.append(f"name: {fm['name']}")
    lines.append(f'description: "{fm["description"]}"')
    lines.append("metadata:")
    lines.append(f"  short-description: {short_desc}")
    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines)


def generate_gemini(fm: dict, body: str, config: dict, skill_name: str) -> str:
    """Generate Gemini .toml file."""
    escaped_desc = fm["description"].replace('"', '\\"')
    escaped_body = body.replace('"""', '\\"""')

    lines = []
    lines.append(f'description = "{escaped_desc}"')
    lines.append(f'prompt = """')
    lines.append(escaped_body)
    lines.append('"""')
    return "\n".join(lines)


def generate_antigravity(fm: dict, body: str, config: dict, skill_name: str) -> str:
    """Generate Antigravity .md file with minimal frontmatter."""
    lines = ["---"]
    lines.append(f'description: "{fm["description"]}"')
    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines)


GENERATORS = {
    "claude-code": generate_claude_code,
    "claude-skills": generate_claude_skills,
    "codex": generate_codex,
    "gemini": generate_gemini,
    "antigravity": generate_antigravity,
}


def main():
    args = sys.argv[1:]
    clean = "--clean" in args
    args = [a for a in args if a != "--clean"]

    config = load_config()
    adapters_config = config["adapters"]
    skills_config = config.get("skills", {})

    target_platforms = args if args else list(adapters_config.keys())

    if clean and ADAPTERS_DIR.exists():
        shutil.rmtree(ADAPTERS_DIR)
        print(f"Cleaned {ADAPTERS_DIR}")

    prompts = sorted(PROMPTS_DIR.glob("*.md"))
    if not prompts:
        print("No prompts found in prompts/")
        sys.exit(1)

    total = 0
    for platform in target_platforms:
        if platform not in adapters_config:
            print(f"Unknown platform: {platform}")
            sys.exit(1)

        pconfig = adapters_config[platform]
        output_dir = ROOT / pconfig["output_dir"]
        file_pattern = pconfig["file_pattern"]
        args_placeholder = pconfig["args_placeholder"]
        generator = GENERATORS[platform]

        for prompt_path in prompts:
            fm, body = parse_prompt(prompt_path)
            skill_name = fm["name"]

            body = replace_args_placeholder(body, args_placeholder)

            gen_config = dict(pconfig)
            gen_config["_skills"] = skills_config

            content = generator(fm, body, gen_config, skill_name)

            out_file = output_dir / file_pattern.format(name=skill_name)
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(content)
            total += 1

        print(f"  [{platform}] Generated {len(prompts)} skills → {output_dir}")

    print(f"\nTotal: {total} files generated across {len(target_platforms)} platforms.")


if __name__ == "__main__":
    main()
