# Design Skills

ชุดเครื่องมือ AI สำหรับงาน UI/UX Design — ครอบคลุม design critique, design system, UX writing, accessibility audit, user research synthesis, และ developer handoff

รองรับ **5 platforms** จาก source of truth เดียว:

| Platform | Format | Install Path |
|----------|--------|--------------|
| **Claude Code** | `SKILL.md` (full features: allowed-tools, paths) | `.claude/skills/` |
| **Claude Skills** | `SKILL.md` (portable: Claude Web + Code) | `.claude/skills/` |
| **Codex CLI** | `SKILL.md` (name, description, metadata) | `.codex/skills/` |
| **Gemini CLI** | `.toml` (description + prompt) | `.gemini/skills/` |
| **Antigravity** | `.md` (description frontmatter) | `.antigravity/commands/` |

---

## Skills ทั้ง 6 ตัว

| Skill | หน้าที่ | Slash Command |
|-------|---------|---------------|
| **design-critique** | วิจารณ์ดีไซน์ — usability, visual hierarchy, consistency | `/design-critique` |
| **accessibility-review** | ตรวจ WCAG 2.1 AA — contrast, keyboard, screen reader | `/accessibility-review` |
| **ux-writing** | เขียน/รีวิว UX copy — error messages, CTAs, empty states | `/ux-writing` |
| **design-system** | Audit/Document/Extend design system — tokens, components | `/design-system` |
| **research-synthesis** | สรุปงานวิจัยผู้ใช้ — interviews, surveys, usability tests | `/research-synthesis` |
| **design-handoff** | สร้าง spec ส่งงาน dev — measurements, states, edge cases | `/design-handoff` |

---

## Quick Start

### Install to a project (all platforms at once)

```bash
./install.sh /path/to/your/project
```

### Install specific platforms only

```bash
./install.sh /path/to/project codex gemini    # Codex + Gemini only
./install.sh /path/to/project claude-code     # Claude Code only
```

---

## Architecture

```
design/
├── prompts/                    ← Source of truth (platform-agnostic)
│   ├── design-critique.md
│   ├── accessibility-review.md
│   ├── ux-writing.md
│   ├── design-system.md
│   ├── research-synthesis.md
│   └── design-handoff.md
├── adapters.yml                ← Per-platform generation config
├── scripts/
│   └── generate-adapters.py   ← Generator script
├── adapters/                   ← Auto-generated output (do not edit)
│   ├── claude-code/
│   ├── claude-skills/
│   ├── codex/
│   ├── gemini/
│   └── antigravity/
├── install.sh                  ← Install to target project
│
├── claude-plugin-1.1.0/        ← Legacy: Cowork plugin format
├── claude-skills/              ← Legacy: original Claude Skills
└── claude-web-project-instructions.md  ← Legacy: Project Instructions
```

### How it works

1. **Edit** skill content in `prompts/*.md` (YAML frontmatter + body)
2. **Generate** platform adapters: `python3 scripts/generate-adapters.py`
3. **Install** to target project: `./install.sh /path/to/project`

Single source of truth — change once, propagate to all 5 platforms.

---

## Regenerating Adapters

After editing any file in `prompts/`:

```bash
python3 scripts/generate-adapters.py           # Generate all platforms
python3 scripts/generate-adapters.py codex     # Generate only codex
python3 scripts/generate-adapters.py --clean   # Clean + regenerate all
```

---

## Platform Differences

| Feature | Claude Code | Claude Skills | Codex | Gemini | Antigravity |
|---------|-------------|---------------|-------|--------|-------------|
| allowed-tools | Yes | No | No | No | No |
| paths (auto-trigger) | Yes | Yes | No | No | No |
| argument-hint | Yes | Yes | No | No | No |
| Args placeholder | `$ARGUMENTS` | `$ARGUMENTS` | `$ARGUMENTS` | `{{args}}` | `$ARGUMENTS` |
| MCP integration | Figma MCP | Figma MCP | Generic | Generic | Generic |

---

## MCP Integrations

Skills ทำงานได้เดี่ยวๆ (บอกหรือแปะ screenshot) แต่จะทรงพลังขึ้นเมื่อเชื่อมต่อ MCP:

| MCP | ทำอะไรได้เพิ่ม |
|-----|----------------|
| **Figma** | ดึงดีไซน์, ตรวจ components, อ่าน tokens, Code Connect |
| **Notion** | ดึง brand guidelines, design principles, research repo |
| **Linear / Jira** | Link designs กับ tickets, สร้าง sub-tasks จาก handoff |
| **Intercom** | ดึง user feedback, support tickets สำหรับ research |

---

## Legacy Formats

The original formats are still available for backward compatibility:

- `claude-plugin-1.1.0/` — Cowork/Claude Code plugin system
- `claude-skills/` — Original Claude Skills (before multi-platform)
- `claude-web-project-instructions.md` — Claude Web Projects

These are no longer the source of truth. Edit `prompts/` instead.
