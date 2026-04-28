# Install: Claude Web Project Instructions

วิธีติดตั้ง Design Skills บน **Claude Web** (claude.ai) แบบง่ายที่สุด — ไม่ต้องอัปโหลดไฟล์ แค่ copy-paste

## ขั้นตอน

1. เปิด [claude.ai](https://claude.ai)
2. สร้าง **Project** ใหม่ (หรือเปิด project ที่ต้องการ)
3. คลิก **Project Instructions** (ไอคอนรูปเกียร์)
4. Copy เนื้อหาทั้งหมดจากไฟล์ [`design/claude-web-project-instructions.md`](../design/claude-web-project-instructions.md)
5. วางลงใน Project Instructions
6. บันทึก

## วิธีใช้งาน

เรียกผ่าน keyword (ไม่มี slash command ในโหมดนี้):

| พิมพ์ว่า... | Workflow ที่ trigger |
|---|---|
| "critique this design" หรือ "ดูดีไซน์นี้ให้หน่อย" | Design Critique |
| "accessibility audit" หรือ "เช็ค a11y" | Accessibility Review |
| "write error message for..." หรือ "เขียน copy" | UX Writing |
| "audit design system" หรือ "ตรวจ tokens" | Design System |
| "synthesize this research" หรือ "สรุปงานวิจัย" | Research Synthesis |
| "handoff to dev" หรือ "สร้าง spec" | Design Handoff |

## เปรียบเทียบกับ Claude Web Skills

| | Project Instructions | Claude Web Skills |
|---|---|---|
| **ติดตั้ง** | Copy-paste (ง่ายมาก) | Upload ZIP (ง่าย) |
| **Scope** | เฉพาะ 1 project | ทุก conversation |
| **Context cost** | Load ทั้งก้อนทุกครั้ง | Load เฉพาะเมื่อ trigger |
| **Slash commands** | ไม่มี | ไม่มี (Web ไม่รองรับ) |
| **อัปเดต** | Copy-paste ใหม่ | ลบ + upload ใหม่ |

**แนะนำ:**
- ลองเร็วๆ / project เดียว → **Project Instructions**
- ใช้ทุก conversation → **Claude Web Skills** (ดู [install-claude-web-skills.md](install-claude-web-skills.md))

## เชื่อมต่อ Figma MCP (optional)

เพิ่มความสามารถโดยเชื่อมต่อ Figma MCP:
1. ไปที่ Settings → Connected Tools
2. เชื่อมต่อ Figma
3. Skills จะดึงดีไซน์จาก Figma ได้โดยตรงเมื่อแปะ URL

## หมายเหตุ

- Project Instructions จะถูก load ทุกครั้งที่เปิด conversation ใน project นั้น (ใช้ context มากกว่า Skills)
- ถ้า project มีหลาย instructions อยู่แล้ว อาจเพิ่ม token cost — พิจารณาใช้ Skills แทน
- ไฟล์ต้นฉบับ: [`design/claude-web-project-instructions.md`](../design/claude-web-project-instructions.md)
