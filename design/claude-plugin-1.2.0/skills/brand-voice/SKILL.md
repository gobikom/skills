---
name: brand-voice
description: Enforce Banking Digital platform brand voice rules — capitalization, punctuation, component-specific copy formats, and TH/EN style conventions.
---

# Brand Voice — Banking Digital Platform

Enforce the official UX writing guideline for the Banking Digital platform.

## Voice and Tone

- **Professional & Polished** — sincere, confident language to build trust
- **Approachable & Human** — plain language, no robot-like phrasing
- **Polite but Not Playful** — respectful without humor or slang
- **Helpful** — clear, easy-to-follow solutions

## Capitalization

| Context | Style | Examples |
|---------|-------|---------|
| Headers, page titles, sub-headers, email subjects, empty state titles, secondary buttons | **Title Case** | Next, Done, New Transfer |
| Pop-up headers, descriptions, tooltips, inline errors, placeholders, toasts | **Sentence case** | Successfully exported. |
| Primary action buttons | **UPPERCASE** | APPLY, APPROVE, CONFIRM |

## Punctuation

- Period at end of every sentence (except headers, buttons, sentences ending in numbers)
- **Oxford Comma** always in English lists
- **No exclamation marks** — strictly forbidden
- Question marks in EN only; never in Thai copy
- Double quotes for UI element references (e.g., Please select "PROCEED")

## Component Formats

### Toasts
- Success EN: `Successfully [past verb].` / TH: `[action]สำเร็จ`
- Fail EN: `Unable to [verb].` / TH: `ไม่สามารถ[action]ได้`
- 1 sentence. Sentence case.

### Buttons
- Primary: UPPERCASE, 1-3 words, verb-first (APPLY, APPROVE, EXPORT)
- Secondary: Title Case (Next, Done, New Transfer)
- TH: must start with verb (ยืนยัน, อนุมัติ)

### Empty States
- Title: Title Case (EN) / `ไม่พบ...` (TH)
- Explainer: why empty + what to do next
- Always include CTA

### Inline Errors
- Field-level: short, sentence case, state what is wrong
- Form-level: action-oriented, tell how to fix
- Never blame the user

## Style Rules

- American English (exception: British banking terms like "Current account", "Cheque")
- Active voice (exception: passive to soften negatives)
- No contractions ("cannot" not "can't")
- Numerals for numbers (1, 2, 3)
- Currency EN: 3-letter codes (THB, USD) / TH: full names (บาท)
- Pronouns: "you" (คุณ), never "ท่าน"
