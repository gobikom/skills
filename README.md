# Skills

AI skill packs for design, engineering, and product workflows — multi-platform, single source of truth.

## Available Packs

| Pack | Skills | Description |
|------|--------|-------------|
| [**design/**](design/) | 6 | UI/UX Design — critique, accessibility, UX writing, design system, research synthesis, handoff |

## Supported Platforms

All packs generate adapters for 5 AI coding tools from a single source:

| Platform | Format | Install Path |
|----------|--------|--------------|
| Claude Code | `SKILL.md` (allowed-tools, paths, auto-trigger) | `.claude/skills/` |
| Claude Skills | `SKILL.md` (portable) | `.claude/skills/` |
| Codex CLI | `SKILL.md` (name, description, metadata) | `.codex/skills/` |
| Gemini CLI | `.toml` (description + prompt) | `.gemini/skills/` |
| Antigravity | `.md` (description frontmatter) | `.antigravity/commands/` |

## Quick Start

```bash
# Install design skills to your project (all platforms)
./design/install.sh /path/to/your/project

# Install specific platforms only
./design/install.sh /path/to/project codex gemini

# Regenerate adapters after editing prompts
python3 design/scripts/generate-adapters.py
```

## Architecture

Each pack follows the same structure:

```
<pack>/
├── prompts/              ← Source of truth (edit here)
├── adapters.yml          ← Platform generation config
├── scripts/
│   └── generate-adapters.py
├── adapters/             ← Auto-generated (do not edit)
│   ├── claude-code/
│   ├── claude-skills/
│   ├── codex/
│   ├── gemini/
│   └── antigravity/
└── install.sh            ← Deploy to target project
```

Edit once in `prompts/`, regenerate, deploy everywhere.

## Adding a New Pack

1. Create a new folder (e.g. `engineering/`)
2. Add `prompts/*.md` with YAML frontmatter (name, description, argument-hint)
3. Copy and adapt `adapters.yml` + `scripts/generate-adapters.py`
4. Run the generator, commit adapters

## License

MIT
