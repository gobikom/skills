---
name: ux-writing
description: Write or review UX copy — microcopy, error messages, empty states, CTAs, onboarding flows. Integrates with UX Copy MCP for langpack search and AI generation when available.
argument-hint: "<context, copy to review, or component name>"
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

## Frontitude CSV Export

After bulk processing, generate a CSV file in Frontitude import format with these columns:

```
Name,Unique key,Context,Value,Value (English - en),Value (Thai - th),Status,Tags,Copy guidelines,Updated at,Last Edited By,Frontitude link
```

Column mapping:

| Column | Source |
|--------|--------|
| Name | `{platform_name} / {category} / {copy_name} / {id}` |
| Unique key | Same as Name |
| Context | Screen/flow context |
| Value | EN copy (default) |
| Value (English - en) | EN copy |
| Value (Thai - th) | TH copy |
| Status | `Draft` (new) or `Review` (partial match) |
| Tags | Product, device, "AI Generated" |
| Copy guidelines | Guideline rule applied |

Category mapping for the Name column:

| Placement | Category Code |
|-----------|--------------|
| Title | `03 Title` |
| Button / CTA | `05 Button` |
| Toast / Snackbar | `08 Informing` |
| Popup / Dialog | `07 Popup` |
| Empty State | `09 Empty State` |
| Inline Error | `06 Error` |
| Tooltip | `10 Tooltip` |
| Label | `04 Label` |
| Placeholder | `04 Placeholder` |
| Push Notification | `11 Notification` |

Write the file as `frontitude-export-{screen_name}-{date}.csv` in the working directory.

## Workflow

Follow this workflow to ensure consistency before creating new copy:

### Step 1: Search existing copy

Before writing anything new, search for existing copy:
- **With UX Copy MCP**: Use `match_copy` to search langpack and Frontitude database
- **Without MCP**: Grep locale/i18n files for similar terms and keys

### Step 2: Generate or write copy

- **With UX Copy MCP**: Use `generate_copy` with placement, intent, tone, and max_length parameters
- **Without MCP**: Write copy manually following the Writing Principles and Copy Patterns above

### Step 3: Batch processing (full screens)

For multiple fields on one screen:
- **With UX Copy MCP**: Use `process_screen` to batch-process all UI text at once
- **Without MCP**: Review each field and cross-reference with existing copy patterns

For multi-screen flows:
- **With UX Copy MCP**: Use `process_screens` which adds cross-screen consistency checks (tone divergence, CTA verb sprawl)
- **Without MCP**: Manually audit copy across screen files for consistency

### Step 4: Export CSV

After processing, generate a Frontitude CSV file with all results (existing matches + new generated copy).

## Brand Voice Integration

This skill provides the universal workflow for writing UX copy. For platform-specific rules (capitalization, punctuation, component formats), pair with the **brand-voice** skill.

| Skill | Responsibility |
|-------|---------------|
| **ux-writing** | HOW to write — principles, workflow, MCP integration, search/generate |
| **brand-voice** | WHAT rules to follow — capitalization, punctuation, component patterns, vocab |

## Figma Integration

If a Figma URL is provided, use the Figma MCP to view the screen context and understand the full user flow. Check character limits and layout constraints from the design.

When both Figma MCP and UX Copy MCP are available:
1. Pull the screen design from Figma → identify all text fields
2. Feed those fields into `process_screen` → get existing matches + generated alternatives
3. Return results with Frontitude CSV file for direct import

## Local Code Integration

When working with local code:
- Read existing copy from locale/i18n files to maintain consistency with current terminology
- Grep for existing copy patterns to ensure the new copy matches the product's voice
- Read component files to understand the UI context where copy will appear
- Check for hardcoded strings that should be extracted to locale files
- When writing copy, output in the project's i18n format if one exists (JSON, YAML, etc.)
- If UX Copy MCP is connected, cross-reference local i18n keys with the centralized langpack to detect drift
