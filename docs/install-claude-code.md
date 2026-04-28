# Install: Claude Code (CLI / Desktop / IDE)

วิธีติดตั้ง Design Skills สำหรับ **Claude Code** — รองรับ features เต็ม (allowed-tools, paths auto-trigger, $ARGUMENTS)

## วิธี 1: install.sh (แนะนำ)

```bash
# Clone repo
git clone https://github.com/gobikom/skills.git
cd skills

# Install to your project
./design/install.sh /path/to/your/project claude-code
```

Skills จะถูก copy ไปที่ `/path/to/your/project/.claude/skills/`

## วิธี 2: Copy manual

```bash
# ใช้กับทุก project (personal)
cp -r design/adapters/claude-code/* ~/.claude/skills/

# ใช้เฉพาะ project นี้
cp -r design/adapters/claude-code/* /path/to/project/.claude/skills/
```

## วิธีใช้งาน

### Slash Commands

```
/design-critique https://figma.com/design/abc123/...
/accessibility-review https://figma.com/design/abc123/...
/ux-writing error message for payment failure
/design-system audit
/design-system document Button
/research-synthesis
/design-handoff https://figma.com/design/abc123/...
```

### Auto-Trigger (ตาม path)

Skills จะ trigger อัตโนมัติเมื่อทำงานกับไฟล์ที่เกี่ยวข้อง:

| Skill | Paths ที่ trigger |
|---|---|
| design-critique | `**/*.css`, `**/*.scss`, `**/components/**`, `**/ui/**` |
| accessibility-review | `**/*.html`, `**/*.jsx`, `**/*.tsx`, `**/*.vue` |
| ux-writing | `**/locales/**`, `**/i18n/**`, `**/translations/**` |
| design-system | `**/tokens/**`, `**/theme/**`, `**/tailwind.config.*` |
| research-synthesis | `**/research/**`, `**/surveys/**`, `**/*.csv` |
| design-handoff | `**/design/**`, `**/specs/**`, `**/handoff/**` |

### Tool Auto-Approve

Claude Code adapter มี `allowed-tools` config ที่ auto-approve tools ที่จำเป็น:
- Figma MCP tools (get_design_context, get_screenshot, etc.)
- Read (อ่านไฟล์)
- Bash commands ที่ specific (npx axe-core, npx pa11y, grep, find)

## อัปเดต

```bash
cd skills
git pull
python3 design/scripts/generate-adapters.py
./design/install.sh /path/to/your/project claude-code
```

## ดูเพิ่มเติม

- [install-claude-web-skills.md](install-claude-web-skills.md) — สำหรับ Claude Web (upload ZIP)
- [install-web-instructions.md](install-web-instructions.md) — สำหรับ Claude Web (copy-paste)
