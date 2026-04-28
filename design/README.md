# Design Skills

ชุดเครื่องมือ AI สำหรับงาน UI/UX Design — ครอบคลุม design critique, design system, UX writing, accessibility audit, user research synthesis, และ developer handoff

มีให้เลือก 3 รูปแบบตาม platform ที่ใช้งาน:

| รูปแบบ | Platform | โฟลเดอร์ |
|--------|----------|----------|
| **Plugin** | Cowork / Claude Code (plugin system) | `claude-plugin-1.1.0/` |
| **Claude Skills** | Claude Web + Claude Code | `claude-skills/` |
| **Project Instructions** | Claude Web (Projects) | `claude-web-project-instructions.md` |

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

## การติดตั้ง

### วิธี 1: Claude Skills (แนะนำ — ใช้ได้ทั้ง Claude Web + Claude Code)

#### Claude Web (claude.ai)

1. เปิด [claude.ai](https://claude.ai)
2. คลิก **Customize** (เมนูด้านซ้ายล่าง)
3. คลิก **Skills** → **Create Skill**
4. อัปโหลด ZIP ทีละไฟล์จากโฟลเดอร์ `claude-skills/`:

```
claude-skills/
├── design-critique.zip
├── accessibility-review.zip
├── ux-writing.zip
├── design-system.zip
├── research-synthesis.zip
└── design-handoff.zip
```

5. เปิดใช้งานทั้ง 6 ตัว
6. (แนะนำ) เชื่อมต่อ **Figma MCP** ใน Settings เพื่อดึงดีไซน์จาก Figma โดยตรง

#### Claude Code (CLI / Desktop / IDE)

Copy โฟลเดอร์ skill ไปวางที่:

**ใช้กับทุก project (personal):**

```bash
cp -r claude-skills/design-critique ~/.claude/skills/
cp -r claude-skills/accessibility-review ~/.claude/skills/
cp -r claude-skills/ux-writing ~/.claude/skills/
cp -r claude-skills/design-system ~/.claude/skills/
cp -r claude-skills/research-synthesis ~/.claude/skills/
cp -r claude-skills/design-handoff ~/.claude/skills/
```

**ใช้เฉพาะ project นี้:**

```bash
cp -r claude-skills/design-critique .claude/skills/
cp -r claude-skills/accessibility-review .claude/skills/
cp -r claude-skills/ux-writing .claude/skills/
cp -r claude-skills/design-system .claude/skills/
cp -r claude-skills/research-synthesis .claude/skills/
cp -r claude-skills/design-handoff .claude/skills/
```

### วิธี 2: Plugin (Cowork / Claude Code plugin system)

```bash
claude plugins add knowledge-work-plugins/design
```

หรือ copy โฟลเดอร์ `claude-plugin-1.1.0/` ไปติดตั้งเอง

### วิธี 3: Project Instructions (Claude Web — ง่ายสุด)

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
/design-system audit
/design-system document Button
/design-system extend DateRangePicker
/research-synthesis
/design-handoff https://figma.com/design/abc123/...
```

### เรียกด้วยภาษาธรรมชาติ (auto-trigger)

Skills จะ trigger อัตโนมัติเมื่อ Claude จับได้ว่าคำถามเกี่ยวข้อง:

| พิมพ์ว่า... | Skill ที่ trigger |
|---|---|
| "ช่วยดูดีไซน์นี้หน่อย" + แปะ screenshot | design-critique |
| "เช็ค accessibility ให้หน่อย" | accessibility-review |
| "เขียน error message สำหรับ payment ล้มเหลว" | ux-writing |
| "ตรวจ design tokens ใน project" | design-system |
| "สรุปผลสัมภาษณ์ user" + แปะ transcript | research-synthesis |
| "สร้าง spec ส่งให้ dev" + แปะ Figma link | design-handoff |

### เรียกอัตโนมัติตาม path (Claude Code เท่านั้น)

Skills จะ trigger เมื่อทำงานกับไฟล์ที่เกี่ยวข้อง:

| Skill | Paths ที่ trigger |
|---|---|
| design-critique | `**/*.css`, `**/*.scss`, `**/components/**`, `**/ui/**` |
| accessibility-review | `**/*.html`, `**/*.jsx`, `**/*.tsx`, `**/*.vue` |
| ux-writing | `**/locales/**`, `**/i18n/**`, `**/translations/**` |
| design-system | `**/tokens/**`, `**/theme/**`, `**/tailwind.config.*` |
| research-synthesis | `**/research/**`, `**/surveys/**`, `**/*.csv` |
| design-handoff | `**/design/**`, `**/specs/**`, `**/handoff/**` |

---

## เปรียบเทียบ 3 รูปแบบ

### ภาพรวม

| | Plugin | Claude Skill | Project Instructions |
|---|---|---|---|
| **Platform** | Cowork, Claude Code | Claude Web, Claude Code | Claude Web (Projects) |
| **ติดตั้ง** | `claude plugins add` | Upload ZIP / copy folder | Copy-paste text |
| **ความยาก** | ง่าย | ง่าย | ง่ายมาก |
| **แชร์ได้** | Plugin registry | ZIP file / git | Copy-paste |

### การ Loading

| | Plugin | Claude Skill | Project Instructions |
|---|---|---|---|
| **วิธี load** | ติดตั้งครั้งเดียว | Dynamic — load เมื่อ trigger | Static — load ตลอด |
| **Context cost** | ~100 tokens/skill (metadata) | ~100 tokens/skill (metadata) | ทั้งหมด load ทุกครั้ง |
| **Progressive loading** | Level 1-3 | Level 1-3 | ไม่มี — load ทั้งก้อน |

### Slash Commands

| | Plugin | Claude Skill | Project Instructions |
|---|---|---|---|
| **Slash commands** | `/critique`, `/handoff` | `/design-critique`, `/design-handoff` | ไม่มี — ใช้ keyword แทน |
| **$ARGUMENTS** | ใช้ได้ | ใช้ได้ (Claude Code) | ไม่ได้ |
| **argument-hint** | ใช้ได้ | ใช้ได้ (Claude Code) | ไม่ได้ |

### Auto-Trigger

| | Plugin | Claude Skill | Project Instructions |
|---|---|---|---|
| **Natural language trigger** | ใช่ (via skills) | ใช่ (via description) | ใช่ (via keywords ใน instructions) |
| **Path-based trigger** | ไม่ | ใช่ (`paths` field, Claude Code) | ไม่ |
| **disable-model-invocation** | ไม่ | ใช่ (Claude Code) | ไม่ |

### Tools & Permissions

| | Plugin | Claude Skill | Project Instructions |
|---|---|---|---|
| **allowed-tools** | ผ่าน plugin config | ใช่ — Figma MCP, Read, Bash | ไม่ได้ |
| **Auto-approve tools** | ไม่ | ใช่ (Claude Code) | ไม่ |
| **MCP config** | `.mcp.json` อัตโนมัติ | ผู้ใช้ต่อเอง | ผู้ใช้ต่อเอง |

### Local Code Integration (Claude Code เท่านั้น)

| | Plugin | Claude Skill | Project Instructions |
|---|---|---|---|
| **อ่านไฟล์ในเครื่อง** | ใช่ | ใช่ | ไม่ได้ |
| **รัน CLI tools** | ใช่ | ใช่ (axe-core, pa11y, lighthouse) | ไม่ได้ |
| **Git integration** | ใช่ | ใช่ (git diff) | ไม่ได้ |
| **Scan codebase** | ใช่ | ใช่ (grep, find) | ไม่ได้ |

### Scope & Portability

| | Plugin | Claude Skill | Project Instructions |
|---|---|---|---|
| **Scope** | ทุก project (installed) | ทุก project (`~/.claude/skills/`) หรือเฉพาะ project (`.claude/skills/`) | เฉพาะ 1 project |
| **แชร์กับทีม** | Plugin registry | ZIP / git / org provisioning (Team/Enterprise) | Share project |
| **Cross-platform** | Cowork + Claude Code | Claude Web + Claude Code + Agent Skills standard | Claude Web เท่านั้น |

### สรุปแนะนำ

| สถานการณ์ | ใช้แบบไหน |
|---|---|
| ต้องการความยืดหยุ่นสูงสุด ใช้ได้ทุกที่ | **Claude Skills** |
| ใช้ Cowork เป็นหลัก | **Plugin** |
| ต้องการลองใช้เร็วๆ ไม่อยาก setup | **Project Instructions** |
| ทำงานกับ codebase ใน IDE | **Claude Skills** (ใน Claude Code) |
| แชร์กับทีมที่ใช้ claude.ai | **Claude Skills** (ZIP) |

---

## โครงสร้างโปรเจค

```
design/
├── README.md                              ← ไฟล์นี้
├── claude-plugin-1.1.0/                   ← Plugin format (Cowork / Claude Code)
│   ├── .claude-plugin/plugin.json
│   ├── .mcp.json
│   ├── README.md
│   ├── CONNECTORS.md
│   ├── commands/
│   │   ├── critique.md
│   │   ├── accessibility.md
│   │   ├── design-system.md
│   │   ├── ux-copy.md
│   │   ├── research-synthesis.md
│   │   └── handoff.md
│   └── skills/
│       ├── design-critique/SKILL.md
│       ├── accessibility-review/SKILL.md
│       ├── design-system-management/SKILL.md
│       ├── ux-writing/SKILL.md
│       ├── user-research/SKILL.md
│       └── design-handoff/SKILL.md
│
├── claude-skills/                         ← Claude Skills format (Web + Code)
│   ├── design-critique/SKILL.md
│   ├── design-critique.zip
│   ├── accessibility-review/SKILL.md
│   ├── accessibility-review.zip
│   ├── ux-writing/SKILL.md
│   ├── ux-writing.zip
│   ├── design-system/SKILL.md
│   ├── design-system.zip
│   ├── research-synthesis/SKILL.md
│   ├── research-synthesis.zip
│   ├── design-handoff/SKILL.md
│   └── design-handoff.zip
│
└── claude-web-project-instructions.md     ← Project Instructions (Claude Web)
```

---

## MCP Integrations

Skills ทำงานได้เดี่ยวๆ (บอกหรือแปะ screenshot) แต่จะทรงพลังขึ้นเมื่อเชื่อมต่อ MCP:

| MCP | ทำอะไรได้เพิ่ม |
|-----|----------------|
| **Figma** | ดึงดีไซน์, ตรวจ components, อ่าน tokens, Code Connect |
| **Notion** | ดึง brand guidelines, design principles, research repo |
| **Linear / Jira** | Link designs กับ tickets, สร้าง sub-tasks จาก handoff |
| **Intercom** | ดึง user feedback, support tickets สำหรับ research |
| **Slack** | แชร์ผลลัพธ์กับทีม |

---

## ที่มา

แปลงจาก [Design Plugin v1.1.0](claude-plugin-1.1.0/) โดย Anthropic — ปรับให้ใช้ได้กับ Claude Skills format (Claude Web + Claude Code) พร้อม enhance ฟีเจอร์เฉพาะ Claude Code:

- `allowed-tools` — auto-approve Figma MCP, Read, Bash
- `paths` — auto-trigger เมื่อทำงานกับไฟล์ที่เกี่ยวข้อง
- `$ARGUMENTS` — ส่ง argument ตรงจาก slash command
- Local Code Integration — อ่านไฟล์, รัน CLI tools, scan codebase
