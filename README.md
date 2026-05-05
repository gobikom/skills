# Skills

AI skill packs for design, engineering, and product workflows — multi-platform, single source of truth.

## Available Packs

| Pack | Skills | Description |
|------|--------|-------------|
| [**design/**](design/) | 7 | UI/UX Design — critique, accessibility, UX writing, brand voice, design system, research synthesis, handoff |

## Supported Platforms

All packs generate adapters for 5 AI coding tools from a single source:

| Platform | Format | Install Path |
|----------|--------|--------------|
| Claude Code | `SKILL.md` (allowed-tools, paths, auto-trigger) | `.claude/skills/` |
| Claude Skills | `SKILL.md` (portable) | `.claude/skills/` |
| Codex CLI | `SKILL.md` (name, description, metadata) | `.codex/skills/` |
| Gemini CLI | `.toml` (description + prompt) | `.gemini/skills/` |
| Antigravity | `.md` (description frontmatter) | `.antigravity/commands/` |

## Installation Guides

| Platform | Guide |
|----------|-------|
| Claude Code (CLI / Desktop / IDE) | [docs/install-claude-code.md](docs/install-claude-code.md) |
| Claude Web — Skills (upload ZIP) | [docs/install-claude-web-skills.md](docs/install-claude-web-skills.md) |
| Claude Web — Project Instructions (copy-paste) | [docs/install-web-instructions.md](docs/install-web-instructions.md) |
| Codex CLI | `./design/install.sh <project> codex` |
| Gemini CLI | `./design/install.sh <project> gemini` |
| Antigravity | `./design/install.sh <project> antigravity` |

## Quick Start

```bash
# Install design skills to your project (all platforms)
./design/install.sh /path/to/your/project

# Install specific platforms only
./design/install.sh /path/to/project codex gemini

# Regenerate adapters after editing prompts
python3 design/scripts/generate-adapters.py
```

## UX Copy MCP Integration (v1.2.0)

The design pack integrates with the **UX Copy MCP Server** for langpack search, AI copy generation, and Frontitude CSV export.

| Tool | Description |
|------|-------------|
| `match_copy` | Search existing copy in langpack and Frontitude database |
| `generate_copy` | AI-generate new copy with placement, intent, and tone context |
| `process_screen` | Batch-process all fields on a single screen (search + generate) |
| `process_screens` | Batch-process multiple screens with cross-screen consistency checks |

Key skills that use the MCP:
- **ux-writing** — universal copy workflow (search → generate → batch)
- **brand-voice** — Banking Digital platform rules (capitalization, punctuation, component formats)

See [docs/USAGE-GUIDE.md](docs/USAGE-GUIDE.md) for 16 use cases with examples.

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
