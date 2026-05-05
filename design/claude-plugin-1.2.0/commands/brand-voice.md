---
description: Review or enforce Banking Digital brand voice rules on UX copy
argument-hint: "<copy to review or component type>"
---

# /brand-voice

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Review copy against the Banking Digital platform guideline, or write new copy that follows all brand rules.

## Usage

```
/brand-voice $ARGUMENTS
```

## Modes

- **Review**: `/brand-voice review "Successfully exported!"` — check against all rules
- **Write**: `/brand-voice write toast success for transfer` — write copy in correct format
- **Audit**: `/brand-voice audit` — scan locale files for violations

## Quick Reference

### Capitalization
- **UPPERCASE**: Primary buttons (APPLY, CONFIRM)
- **Title Case**: Headers, secondary buttons (Next, Done)
- **Sentence case**: Toasts, tooltips, descriptions, errors

### Forbidden
- No exclamation marks (!)
- No contractions (can't → cannot)
- No "Dear Customer" in emails
- No generic errors like "Unable to proceed" or "Error"
- No question marks in Thai copy
- No lowercase buttons
- Never use "ท่าน" — use "คุณ"

### Component Patterns
| Component | EN Pattern | TH Pattern |
|-----------|-----------|------------|
| Toast (success) | `Successfully [past verb].` | `[action]สำเร็จ` |
| Toast (fail) | `Unable to [verb].` | `ไม่สามารถ[action]ได้` |
| Button (primary) | UPPERCASE verb | ยืนยัน, อนุมัติ |
| Empty state title | Title Case noun | ไม่พบ... |
| Placeholder (search) | `Search by [criteria]` | `ค้นหาโดย[criteria]` |
| Placeholder (select) | `Select [item]` | `เลือก[item]` |
| Placeholder (input) | `Enter [item]` | `ระบุ[item]` |

## If Connectors Available

If **~~ux-copy MCP** is connected:
- AI-generated copy already applies these rules server-side
- Use this command to double-check output or audit existing copy

If **~~design tool** is connected:
- Pull the design to verify component types match the correct copy format

## Tips

1. **Pair with `/ux-copy`** — ux-copy handles the creative writing, brand-voice enforces the rules
2. **Run audit before PR** — catch capitalization and punctuation violations early
3. **Check toasts carefully** — most common violation is wrong capitalization or exclamation marks
