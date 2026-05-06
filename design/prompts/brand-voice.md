---
name: brand-voice
description: Enforce Banking Digital platform brand voice rules — capitalization, punctuation, component-specific copy formats, and TH/EN style conventions. Use alongside ux-writing skill.
argument-hint: "[review | write | audit] <copy or component type>"
paths:
  - "**/locales/**"
  - "**/i18n/**"
  - "**/translations/**"
  - "**/strings/**"
  - "**/*.json"
---

# Brand Voice — Banking Digital Platform

Enforce the official UX writing guideline for the Banking Digital platform. Pair with the **ux-writing** skill which provides the universal writing workflow.

## When Triggered

Activate when the user says "brand voice", "check guideline", "review copy against guideline", "capitalization check", "is this copy correct", "banking copy rules", or when reviewing/writing copy for the Banking Digital platform.

## Usage

```
/brand-voice $ARGUMENTS
```

Modes:
- `/brand-voice review [copy]` — check copy against all guideline rules
- `/brand-voice write [component] [context]` — write copy following rules for that component
- `/brand-voice audit` — scan locale files for guideline violations

## Voice and Tone

All copy must be:
- **Professional & Polished** — sincere, confident language to build trust
- **Approachable & Human** — plain language, no robot-like phrasing
- **Polite but Not Playful** — respectful without humor or slang
- **Helpful** — clear, easy-to-follow solutions

## Style Rules (English)

### Spelling
- **American English** (e.g., "Favorite," "Canceled")
- **Exception**: British terms for banking concepts familiar to Thai users (e.g., "Current account," "Cheque")

### Voice & Tense
- **Active voice** always — exception: passive to soften negative messages or unknown subject
- **Present Simple**: general product behavior
- **Present Perfect**: recently completed actions
- **Future Simple**: only for actual future outcomes

### Capitalization
| Context | Style | Examples |
|---------|-------|---------|
| Headers, page titles, sub-headers, email subjects, empty state titles, secondary buttons | **Title Case** | Next, Done, New Transfer |
| Pop-up headers, descriptions, tooltips, inline errors, placeholders, toasts | **Sentence case** | Successfully exported. |
| Primary action buttons | **UPPERCASE** | APPLY, APPROVE, CONFIRM, CANCEL, EXPORT |

### Other Rules
- **No contractions** — "cannot" not "can't"
- **Action-oriented** — start with objective or required action

## Punctuation Rules

| Mark | Rule |
|------|------|
| Period | End of every sentence. Exception: headers, sub-headers, buttons, sentences ending in numbers |
| Comma | Always use **Oxford Comma** in English lists |
| Exclamation mark | **Strictly forbidden** |
| Question mark | Use in EN questions; do not use in Thai copy |
| Ampersand (&) | Page titles/headers only, space before and after |
| Quotation marks | Double quotes for page names, menus, CTAs (e.g., Please select "PROCEED") |

## Component Copy Formats

### Toasts / Snackbars
| Type | EN Pattern | TH Pattern |
|------|-----------|------------|
| Success | `Successfully [past verb].` | `[action]สำเร็จ` |
| Fail | `Unable to [verb].` | `ไม่สามารถ[action]ได้` |
| Fail + retry | Append `Please try again.` | Append `กรุณาลองใหม่อีกครั้ง` |

Rules: 1 sentence. Sentence case. No exclamation marks.

### Pop-ups / Dialogs / Modals
- **Header**: Sentence case. Specific context — never "Unable to proceed" or "Error"
- **Body**: Explain consequence (e.g., "By clicking 'CONFIRM', your transaction will be submitted and cannot be undone.")
- **Buttons**: Primary = UPPERCASE / Secondary = Title Case
- Reference UI elements with double quotes

### Inline Errors
- **Field-level**: Short, sentence case, state what is wrong
- **Form-level**: Action-oriented, tell how to fix
- Never blame the user. Focus on the solution.

### Buttons / CTAs
| Type | Style | Examples |
|------|-------|---------|
| Primary action | UPPERCASE, 1-3 words, verb-first | APPLY, APPROVE, EXPORT, CANCEL |
| Secondary/navigation | Title Case, 1-3 words | Next, Done, New Transfer |
| TH buttons | Must start with verb | ยืนยัน, อนุมัติ, ส่งออกข้อมูล |

Never use lowercase for buttons.

### Tooltips
- **Action**: 1 word, sentence case (e.g., "Approve" / "อนุมัติ")
- **Explanatory**: 1-2 sentences max (~80 chars), sentence case. Tell user what to do, not what the element is.

### Empty States
- **Title**: Short noun phrase, Title Case (EN), `ไม่พบ...` (TH)
- **Explainer**: 1-2 sentences — why empty + what to do next
- Always include CTA — never leave user at a dead end

### Placeholder Text
| Field Type | EN Pattern | TH Pattern |
|-----------|-----------|------------|
| Search | `Search by [criteria]` | `ค้นหาโดย[criteria]` |
| Select | `Select [item]` | `เลือก[item]` |
| Input | `Enter [item]` | `ระบุ[item]` |

Sentence case. No periods. Include format example when relevant.

### Push Notifications
- **Title**: Max 50 chars, Title Case
- **Body**: Max 100 chars, sentence case, actionable next step

### Email Notifications
- **Subject**: Title Case, max 60 chars, state purpose (not "Notification from KTB")
- **Body**: Open with context (what happened), end with CTA. No "Dear Customer" greeting.

## Formatting Rules

| Element | Rule |
|---------|------|
| Numbers | Use numerals (1, 2, 3) not words |
| Dates | Abbreviate months (Aug, Dec), 4-digit year. Example: 02 Aug 2020 - 13:00 |
| Time | 24-hour format, no am/pm (exception: maintenance alerts) |
| Currency (EN) | 3-letter codes: THB, USD |
| Currency (TH) | Full names: บาท, ดอลลาร์สหรัฐ |

## Vocabulary Rules

- **No jargon** — use common, clear words
- **Acronyms** — only if common or previously explained
- **Pronouns** — "you" (คุณ) for user. Never "ท่าน". Use "they/them" for unknown gender.

## Output Format — Review

    ## Brand Voice Review: [Context]
    
    ### Copy Reviewed
    [Original copy]
    
    ### Violations Found
    | # | Rule | Violation | Fix |
    |---|------|-----------|-----|
    | 1 | [Rule name] | [What's wrong] | [Corrected copy] |
    
    ### Corrected Copy
    **[Element]**: [Corrected copy]
    
    ### Compliance Score
    [X/10] — [Summary]

## Output Format — Write

    ## Brand Voice Copy: [Component] — [Context]
    
    ### Copy
    **EN**: [Copy following all rules]
    **TH**: [Copy following all rules]
    
    ### Rules Applied
    - [Which rules were applied]
    
    ### Alternatives
    | Option | EN | TH | Notes |
    |--------|----|----|-------|
    | A | [Copy] | [Copy] | [Rule applied] |
    | B | [Copy] | [Copy] | [Rule applied] |

## Output Format — Audit

    ## Brand Voice Audit: [Scope]
    
    ### Summary
    **Files scanned**: [X] | **Violations**: [X] | **Score**: [X/100]
    
    ### Violations by Rule
    | Rule | Count | Severity | Examples |
    |------|-------|----------|---------|
    | [Rule] | [X] | High/Med/Low | [key: "..." should be "..."] |
    
    ### Top Fixes
    1. [Most common violation + batch fix]
    2. [Second most common]
    3. [Third]

## Figma Integration

If a Figma URL is provided, use the Figma MCP to inspect component types and verify the correct copy format is applied (e.g., primary button = UPPERCASE).

## Local Code Integration

When working with local code:
- Grep locale files for guideline violations (exclamation marks, wrong capitalization, contractions)
- Check button labels match the UPPERCASE/Title Case convention
- Verify toast messages follow the success/fail patterns
- Scan for "ท่าน" usage that should be "คุณ"
