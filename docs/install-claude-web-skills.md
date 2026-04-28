# Install: Claude Web Skills

วิธีติดตั้ง Design Skills บน **Claude Web** (claude.ai) ผ่านระบบ Skills

## ขั้นตอน

1. เปิด [claude.ai](https://claude.ai)
2. คลิก **Customize** (เมนูด้านซ้ายล่าง)
3. คลิก **Skills** → **Create Skill**
4. อัปโหลด ZIP ทีละไฟล์จาก `design/claude-skills/`:

```
design/claude-skills/
├── design-critique.zip
├── accessibility-review.zip
├── ux-writing.zip
├── design-system.zip
├── research-synthesis.zip
└── design-handoff.zip
```

5. เปิดใช้งานทั้ง 6 ตัว
6. (แนะนำ) เชื่อมต่อ **Figma MCP** ใน Settings เพื่อดึงดีไซน์จาก Figma โดยตรง

## วิธีใช้งาน

หลังติดตั้ง skills จะ trigger อัตโนมัติเมื่อ Claude จับได้ว่าคำถามเกี่ยวข้อง:

| พิมพ์ว่า... | Skill ที่ trigger |
|---|---|
| "ช่วยดูดีไซน์นี้หน่อย" + แปะ screenshot | design-critique |
| "เช็ค accessibility ให้หน่อย" | accessibility-review |
| "เขียน error message สำหรับ payment ล้มเหลว" | ux-writing |
| "ตรวจ design tokens ใน project" | design-system |
| "สรุปผลสัมภาษณ์ user" + แปะ transcript | research-synthesis |
| "สร้าง spec ส่งให้ dev" + แปะ Figma link | design-handoff |

## อัปเดต Skills

เมื่อมี version ใหม่:
1. ลบ skills เก่าออก (Customize → Skills → ลบ)
2. อัปโหลด ZIP ใหม่จาก release ล่าสุด

## หมายเหตุ

- Claude Web Skills ไม่รองรับ `allowed-tools` หรือ `paths` auto-trigger — ใช้ keyword trigger แทน
- ถ้าต้องการ features เต็ม (auto-trigger by path, tool auto-approve) ใช้ Claude Code แทน → ดู [install-claude-code.md](install-claude-code.md)
