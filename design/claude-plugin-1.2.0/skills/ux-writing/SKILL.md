---
name: ux-writing
description: Write effective microcopy for user interfaces. Integrates with UX Copy MCP for langpack search, AI generation, and Frontitude CSV export when available.
---

# UX Writing

Write clear, concise, and helpful interface copy.

## Principles

1. **Clear**: Say exactly what you mean. No jargon, no ambiguity.
2. **Concise**: Use the fewest words that convey the full meaning.
3. **Consistent**: Same terms for the same things everywhere.
4. **Useful**: Every word should help the user accomplish their goal.
5. **Human**: Write like a helpful person, not a robot.

## Copy Patterns

### CTAs
- Start with a verb: "Start free trial", "Save changes", "Download report"
- Be specific: "Create account" not "Submit"
- Match the outcome to the label

### Error Messages
Structure: What happened + Why + How to fix
- "Payment declined. Your card was declined by your bank. Try a different card or contact your bank."

### Empty States
Structure: What this is + Why it's empty + How to start
- "No projects yet. Create your first project to start collaborating with your team."

### Confirmation Dialogs
- Make the action clear: "Delete 3 files?" not "Are you sure?"
- Describe consequences: "This can't be undone"
- Label buttons with the action: "Delete files" / "Keep files" not "OK" / "Cancel"

## Voice and Tone

Adapt tone to context:
- **Success**: Celebratory but not over the top
- **Error**: Empathetic and helpful
- **Warning**: Clear and actionable
- **Neutral**: Informative and concise

## Workflow

1. **Search first**: Use `match_copy` (MCP) or grep locale files to find existing copy
2. **Generate or write**: Use `generate_copy` (MCP) or write manually following principles
3. **Batch screens**: Use `process_screen` / `process_screens` (MCP) or review each field manually
4. **Export CSV**: Generate Frontitude CSV file with all results

## Frontitude CSV Export

After bulk processing, generate a CSV file in Frontitude 12-column import format:

| Column | Rule | Example |
|--------|------|---------|
| Name | `{platform} / {category} / {actual EN copy}: / {seq} {Type}_{device}` | `Krungthai Business / 03 Title / Rate Confirmation Summary: / 999 Title_web` |
| Unique key | Same as Name | (same) |
| Context | Leave **empty** | |
| Value | Raw display value (may differ from EN copy) | `Rate Confirmation Summary 999` |
| Value (English - en) | EN copy as shown in UI | `Rate Confirmation Summary:` |
| Value (Thai - th) | TH copy as shown in UI | `สรุปการยืนยันอัตราแลกเปลี่ยน:` |
| Status | `Draft` | `Draft` |
| Tags | Ask user for sprint/milestone tags | `OR Multiple Approve, KB_MVP5_D2` |
| Copy guidelines | Short note (1-3 words) | `New copy` |
| Updated at | Leave **empty** | |
| Last Edited By | Leave **empty** | |
| Frontitude link | Leave **empty** | |

Rules: Name uses actual EN copy (not generic labels). Tags from user (not "AI Generated"). Copy guidelines max 1-3 words. Ask user for: platform, device, tags, sequence number.

Category mapping:

| Placement | Category |
|-----------|---------|
| Title | 03 Title |
| Label | 04 Label |
| Button / CTA | 05 Button |
| Inline Error | 06 Error |
| Popup / Dialog | 07 Popup |
| Toast / Snackbar | 08 Informing |
| Empty State | 09 Empty State |
| Tooltip | 10 Tooltip |
| Push Notification | 11 Notification |

**Claude Code:** Write to `frontitude-export-{screen_name}-{date}.csv`
**Claude Desktop / Web:** Output CSV as code block for user to copy and save as `.csv`

## Workflow

1. **Check MCP**: Try `match_copy` first — if it responds, use MCP workflow. If not, use fallback. State which mode.
2. **Search**: `match_copy` (MCP) or grep locale files (fallback)
3. **Generate**: `generate_copy` (MCP) or write manually with 3 alternatives (fallback)
4. **Batch**: `process_screen` / `process_screens` (MCP) or review each field manually (fallback)
5. **Export CSV**: Always produce Frontitude CSV output regardless of platform

## Brand Voice Integration

Pair with **brand-voice** skill for platform-specific rules (capitalization, punctuation, component formats).

| Skill | Role |
|-------|------|
| ux-writing | HOW to write (principles, workflow, MCP) |
| brand-voice | WHAT rules to follow (Banking Digital guideline) |
