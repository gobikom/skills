---
name: ux-writing
description: "Write or review UX copy — microcopy, error messages, empty states, CTAs, onboarding flows. Use when writing interface text, button labels, or any user-facing copy."
argument-hint: "<context, copy to review, or component name>"
allowed-tools:
  - mcp__claude_ai_Figma__get_design_context
  - mcp__claude_ai_Figma__get_screenshot
  - Read
  - Bash(grep *)
paths:
  - "**/locales/**"
  - "**/i18n/**"
  - "**/translations/**"
  - "**/strings/**"
  - "**/copy/**"
  - "**/content/**"
  - "**/*.json"
---

# UX Writing

Write clear, concise, and helpful interface copy.

## When Triggered

Activate when the user says "ux copy", "write copy for", "error message", "empty state", "what should this button say", "microcopy", "CTA copy", "onboarding copy", or asks for help with any interface text.

## Usage

```
/ux-writing $ARGUMENTS
```

Write or review UX copy for: @$1

## What to Ask (if missing)

- **Context**: What screen, flow, or feature?
- **User state**: What is the user trying to do? How are they feeling?
- **Tone**: Formal, friendly, playful, reassuring?
- **Constraints**: Character limits, platform guidelines?
- **Brand voice** (optional): Any existing style guide?

## Writing Principles

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

### Tooltips
- Concise, helpful, never obvious
- Answer "what does this do?" not "what is this?"

### Loading States
- Set expectations: "Generating report... This usually takes about 30 seconds"
- Reduce anxiety with progress indicators

## Voice and Tone Adaptation

Adapt tone to context:
- **Success**: Celebratory but not over the top
- **Error**: Empathetic and helpful
- **Warning**: Clear and actionable
- **Neutral**: Informative and concise

## Output Format

```markdown
## UX Copy: [Context]

### Recommended Copy
**[Element]**: [Copy]

### Alternatives
| Option | Copy | Tone | Best For |
|--------|------|------|----------|
| A | [Copy] | [Tone] | [When to use] |
| B | [Copy] | [Tone] | [When to use] |
| C | [Copy] | [Tone] | [When to use] |

### Rationale
[Why this copy works — user context, clarity, action-orientation]

### Localization Notes
[Anything translators should know — idioms to avoid, character expansion, cultural context]
```

## Figma Integration

If a Figma URL is provided, use the Figma MCP to view the screen context and understand the full user flow. Check character limits and layout constraints from the design.

## Local Code Integration

When working with local code:
- Read existing copy from locale/i18n files to maintain consistency with current terminology
- Grep for existing copy patterns to ensure the new copy matches the product's voice
- Read component files to understand the UI context where copy will appear
- Check for hardcoded strings that should be extracted to locale files
- When writing copy, output in the project's i18n format if one exists (JSON, YAML, etc.)
