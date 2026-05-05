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

Also available as:

| รูปแบบ | Platform | โฟลเดอร์ |
|--------|----------|----------|
| **Plugin** | Cowork / Claude Code (plugin system) | `claude-plugin-1.2.0/` |
| **Claude Skills** | Claude Web + Claude Code | `claude-skills/` |
| **Project Instructions** | Claude Web (Projects) | `claude-web-project-instructions.md` |

---

## Skills ทั้ง 7 ตัว

| Skill | หน้าที่ | Slash Command |
|-------|---------|---------------|
| **design-critique** | วิจารณ์ดีไซน์ — usability, visual hierarchy, consistency | `/design-critique` |
| **accessibility-review** | ตรวจ WCAG 2.1 AA — contrast, keyboard, screen reader | `/accessibility-review` |
| **ux-writing** | เขียน/รีวิว UX copy — error messages, CTAs, empty states | `/ux-writing` |
| **brand-voice** | บังคับ brand voice ของ Banking Digital — capitalization, punctuation, component formats | `/brand-voice` |
| **design-system** | Audit/Document/Extend design system — tokens, components | `/design-system` |
| **research-synthesis** | สรุปงานวิจัยผู้ใช้ — interviews, surveys, usability tests | `/research-synthesis` |
| **design-handoff** | สร้าง spec ส่งงาน dev — measurements, states, edge cases | `/design-handoff` |

---

## Installation Guides

| วิธี | คำอธิบาย | Guide |
|------|----------|-------|
| **Claude Code** (CLI/Desktop/IDE) | Features เต็ม — slash commands, auto-trigger, tool approve | [install-claude-code.md](../docs/install-claude-code.md) |
| **Claude Web Skills** (upload ZIP) | ใช้ได้ทุก conversation บน claude.ai | [install-claude-web-skills.md](../docs/install-claude-web-skills.md) |
| **Claude Web Instructions** (copy-paste) | ง่ายสุด — วาง text ใน Project Instructions | [install-web-instructions.md](../docs/install-web-instructions.md) |
| **Codex / Gemini / Antigravity** | ผ่าน install.sh | ดูด้านล่าง |

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

### Install Claude Skills manually

```bash
# ใช้กับทุก project (personal)
cp -r claude-skills/design-critique ~/.claude/skills/
cp -r claude-skills/accessibility-review ~/.claude/skills/
cp -r claude-skills/ux-writing ~/.claude/skills/
cp -r claude-skills/brand-voice ~/.claude/skills/
cp -r claude-skills/design-system ~/.claude/skills/
cp -r claude-skills/research-synthesis ~/.claude/skills/
cp -r claude-skills/design-handoff ~/.claude/skills/

# ใช้เฉพาะ project นี้
cp -r claude-skills/design-critique .claude/skills/
# ... (same pattern)
```

### Plugin (Cowork / Claude Code)

```bash
claude plugins add knowledge-work-plugins/design
```

### Project Instructions (Claude Web)

1. เปิด [claude.ai](https://claude.ai) → สร้าง Project ใหม่
2. Copy เนื้อหาจาก `claude-web-project-instructions.md` ไปวางใน **Project Instructions**
3. เชื่อมต่อ Figma MCP (optional)

---

## วิธีใช้งาน

### เรียกด้วย Slash Command

```
/design-critique https://figma.com/design/abc123/...
/accessibility-review https://figma.com/design/abc123/...
/ux-writing error message for payment failure
/brand-voice review "Successfully transferred!"
/design-system audit
/research-synthesis
/design-handoff https://figma.com/design/abc123/...
```

### เรียกด้วยภาษาธรรมชาติ (auto-trigger)

| พิมพ์ว่า... | Skill ที่ trigger |
|---|---|
| "ช่วยดูดีไซน์นี้หน่อย" + แปะ screenshot | design-critique |
| "เช็ค accessibility ให้หน่อย" | accessibility-review |
| "เขียน error message สำหรับ payment ล้มเหลว" | ux-writing |
| "เช็ค copy นี้ตรงตาม guideline ไหม" | brand-voice |
| "ตรวจ design tokens ใน project" | design-system |
| "สรุปผลสัมภาษณ์ user" + แปะ transcript | research-synthesis |
| "สร้าง spec ส่งให้ dev" + แปะ Figma link | design-handoff |

### เรียกอัตโนมัติตาม path (Claude Code เท่านั้น)

| Skill | Paths ที่ trigger |
|---|---|
| design-critique | `**/*.css`, `**/*.scss`, `**/components/**`, `**/ui/**` |
| accessibility-review | `**/*.html`, `**/*.jsx`, `**/*.tsx`, `**/*.vue` |
| ux-writing | `**/locales/**`, `**/i18n/**`, `**/translations/**` |
| brand-voice | `**/locales/**`, `**/i18n/**`, `**/translations/**`, `**/strings/**` |
| design-system | `**/tokens/**`, `**/theme/**`, `**/tailwind.config.*` |
| research-synthesis | `**/research/**`, `**/surveys/**`, `**/*.csv` |
| design-handoff | `**/design/**`, `**/specs/**`, `**/handoff/**` |

---

## Architecture

```
design/
├── prompts/                    ← Source of truth (platform-agnostic)
│   ├── design-critique.md
│   ├── accessibility-review.md
│   ├── ux-writing.md
│   ├── brand-voice.md
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
├── claude-plugin-1.2.0/        ← Plugin format (Cowork / Claude Code)
│   ├── .claude-plugin/plugin.json
│   ├── .mcp.json
│   ├── README.md
│   ├── CONNECTORS.md
│   ├── commands/               ← /critique, /ux-copy, /brand-voice, etc.
│   └── skills/                 ← Plugin skill definitions
│
├── claude-skills/              ← Claude Skills format (Web + Code)
│   ├── design-critique/SKILL.md
│   ├── accessibility-review/SKILL.md
│   ├── ux-writing/SKILL.md
│   ├── brand-voice/SKILL.md
│   ├── design-system/SKILL.md
│   ├── research-synthesis/SKILL.md
│   └── design-handoff/SKILL.md
│
└── claude-web-project-instructions.md
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
| MCP integration | Figma MCP, UX Copy MCP | Figma MCP | Generic | Generic | Generic |

---

## MCP Integrations

Skills ทำงานได้เดี่ยวๆ (บอกหรือแปะ screenshot) แต่จะทรงพลังขึ้นเมื่อเชื่อมต่อ MCP:

| MCP | ทำอะไรได้เพิ่ม |
|-----|----------------|
| **Figma** | ดึงดีไซน์, ตรวจ components, อ่าน tokens, Code Connect |
| **UX Copy** | ค้นหา copy ใน langpack, AI generate copy, batch process หน้าจอ, Frontitude CSV, cross-screen consistency check |
| **Notion** | ดึง brand guidelines, design principles, research repo |
| **Linear / Jira** | Link designs กับ tickets, สร้าง sub-tasks จาก handoff |
| **Intercom** | ดึง user feedback, support tickets สำหรับ research |
| **Slack** | แชร์ผลลัพธ์กับทีม |

---

## ที่มา

แปลงจาก [Design Plugin v1.2.0](claude-plugin-1.2.0/) โดย Anthropic — ปรับให้ใช้ได้กับ Claude Skills format + multi-platform adapters:

- `allowed-tools` — auto-approve Figma MCP, UX Copy MCP, Read, Bash
- `paths` — auto-trigger เมื่อทำงานกับไฟล์ที่เกี่ยวข้อง
- `$ARGUMENTS` — ส่ง argument ตรงจาก slash command
- Local Code Integration — อ่านไฟล์, รัน CLI tools, scan codebase
- UX Copy MCP Integration — ค้นหา/สร้าง copy, batch process, Frontitude export
- Multi-platform adapters — Codex, Gemini, Antigravity จาก source เดียว
