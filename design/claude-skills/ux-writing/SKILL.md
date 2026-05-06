---
name: ux-writing
description: Write or review UX copy — microcopy, error messages, empty states, CTAs, onboarding flows. Use when writing interface text, button labels, or any user-facing copy. Integrates with UX Copy MCP for langpack search and AI generation when available.
argument-hint: "<context, copy to review, or component name>"
allowed-tools:
  - mcp__claude_ai_Figma__get_design_context
  - mcp__claude_ai_Figma__get_screenshot
  - mcp__ux-copy__match_copy
  - mcp__ux-copy__generate_copy
  - mcp__ux-copy__process_screen
  - mcp__ux-copy__process_screens
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

## Frontitude CSV Export

After bulk processing (`process_screen` / `process_screens`), generate a downloadable CSV file in Frontitude import format.

### CSV Columns

```
Name,Unique key,Context,Value,Value (English - en),Value (Thai - th),Status,Tags,Copy guidelines,Updated at,Last Edited By,Frontitude link
```

### Column Mapping

| Column | Source | Example |
|--------|--------|---------|
| Name | `{platform_name} / {category} / {copy_name} / {id}` | `Krungthai Business / 03 Title / Transfer Confirmation / 001 Title_mobile` |
| Unique key | Same as Name | (same) |
| Context | `screen_context` from process_screen input | `Transfer confirmation before executing` |
| Value | EN copy (default) | `Confirm Transfer` |
| Value (English - en) | EN copy | `Confirm Transfer` |
| Value (Thai - th) | TH copy | `ยืนยันการโอน` |
| Status | `Draft` for new, `Review` for partial match | `Draft` |
| Tags | `product + device + "AI Generated"` | `Transfer, Mobile, AI Generated` |
| Copy guidelines | Guideline rule applied | `Title Case for headers` |
| Updated at | Current date (ISO format) | `2026-05-05` |
| Last Edited By | Empty (filled by Frontitude) | |
| Frontitude link | Empty (filled by Frontitude) | |

### Category Mapping (for Name column)

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

### Output Instructions

After generating copy results, always produce the Frontitude CSV output:

**Claude Code (CLI / Desktop IDE):**
1. Compile all fields into Frontitude CSV format
2. Write the file to the working directory: `frontitude-export-{screen_name}-{date}.csv`
3. Present the file path to the user

**Claude Desktop / Claude Web (no filesystem access):**
1. Compile all fields into Frontitude CSV format
2. Output the complete CSV as a code block so the user can copy it
3. Tell the user to save as `.csv` file for Frontitude import

Always produce the CSV regardless of platform — the delivery method changes, the content does not.

## Workflow

Follow this workflow to ensure consistency before creating new copy.

**Important:** At the start of every session, check if UX Copy MCP tools are available by attempting to use `match_copy`. If it responds, use the MCP workflow. If not available, use the fallback workflow. Always state which mode you are using.

### Step 1: Search existing copy

**With UX Copy MCP (try this first):**
- Call `match_copy` with the text you need to write
- Check if the same or similar copy already exists in langpack/Frontitude
- Reuse existing i18n keys when possible
- Note the tone and terminology patterns in existing copy

**Without MCP (fallback):**
- Grep locale/i18n files for similar terms and keys
- Check existing JSON files for patterns

### Step 2: Generate or write copy

**With UX Copy MCP:**
- Call `generate_copy` with context parameters:
  - `placement`: button, toast, title, subtitle, description, error, empty-state, tooltip, modal, push-notification
  - `intent`: inform, confirm, warn, error, success, onboard, upsell
  - `tone`: formal, friendly, playful, reassuring (match brand voice)
  - `max_length`: character limit if constrained by design
- The MCP returns 3 options with TH/EN text and tone labels

**Without MCP (fallback):**
- Write copy manually following the Writing Principles and Copy Patterns above
- Provide 3 alternatives with tone labels

### Step 3: Batch processing (full screens)

**With UX Copy MCP:**
- Single screen: call `process_screen` with all fields at once
- Multi-screen flow: call `process_screens` which adds consistency checks:
  - Tone divergence detection
  - CTA verb sprawl (too many different verbs for similar actions)
  - Terminology consistency across the flow

**Without MCP (fallback):**
- Review each field manually and cross-reference with existing copy patterns
- Manually check consistency across screens

### Step 4: Export Frontitude CSV

Always produce CSV output after bulk processing (see Frontitude CSV Export section above).

## Figma Integration

If a Figma URL is provided, use the Figma MCP to view the screen context and understand the full user flow. Check character limits and layout constraints from the design.

When both Figma MCP and UX Copy MCP are available:
1. Pull the screen design from Figma → identify all text fields
2. Feed those fields into `process_screen` → get existing matches + generated alternatives
3. Return results with Frontitude CSV format for direct import

## UX Copy MCP Integration

The UX Copy MCP server (`ux-copy`) provides four tools:

| Tool | When to Use |
|------|-------------|
| `match_copy` | Search existing langpack/Frontitude copy before writing new |
| `generate_copy` | AI-generate copy with placement, intent, and tone context |
| `process_screen` | Batch all fields on a single screen (search + generate) |
| `process_screens` | Batch multiple screens with cross-screen consistency checks |

### When MCP is available

- **Always search first**: Call `match_copy` before generating new copy to avoid duplicates
- **Use batch tools for screens**: `process_screen` is more efficient than individual calls
- **Leverage consistency checks**: `process_screens` catches tone drift and CTA sprawl automatically
- **Output includes Frontitude format**: Results are ready for direct import into the copy management system

### When MCP is NOT available (fallback)

The skill works fully without the MCP — use these local alternatives:

| MCP Tool | Local Fallback |
|----------|---------------|
| `match_copy` | Grep locale/i18n JSON files for similar terms and keys |
| `generate_copy` | Write manually following Writing Principles + Copy Patterns |
| `process_screen` | Read component file → identify text fields → write copy for each |
| `process_screens` | Manually audit copy across screen files for consistency |

## Brand Voice Integration

This skill provides the universal **workflow** for writing UX copy. For platform-specific **rules** (capitalization, punctuation, component formats), pair with the **brand-voice** skill.

| Skill | Responsibility |
|-------|---------------|
| **ux-writing** | HOW to write — principles, workflow, MCP integration, search/generate |
| **brand-voice** | WHAT rules to follow — capitalization, punctuation, component patterns, vocab |

When both skills are active:
1. ux-writing handles search → generate → batch workflow
2. brand-voice validates output against platform guideline rules
3. Final copy passes both universal quality AND brand compliance

## Local Code Integration (Claude Code)

When working with local code in Claude Code:
- Read existing copy from locale/i18n files to maintain consistency with current terminology
- Grep for existing copy patterns to ensure the new copy matches the product's voice
- Read component files to understand the UI context where copy will appear
- Check for hardcoded strings that should be extracted to locale files
- When writing copy, output in the project's i18n format if one exists (JSON, YAML, etc.)
- If UX Copy MCP is connected, cross-reference local i18n keys with the centralized langpack to detect drift
