---
name: accessibility-review
description: Run a WCAG 2.1 AA accessibility audit on a design or page. Use when checking color contrast, screen reader support, keyboard navigation, or any accessibility compliance question.
argument-hint: "<Figma URL, URL, or description>"
allowed-tools:
  - mcp__claude_ai_Figma__get_design_context
  - mcp__claude_ai_Figma__get_screenshot
  - mcp__claude_ai_Figma__get_metadata
  - Read
  - Bash(npx axe-core *)
  - Bash(npx pa11y *)
  - Bash(npx lighthouse *)
paths:
  - "**/*.html"
  - "**/*.jsx"
  - "**/*.tsx"
  - "**/*.vue"
  - "**/*.svelte"
  - "**/*.css"
  - "**/*.scss"
  - "**/components/**"
  - "**/a11y/**"
  - "**/accessibility/**"
---

# Accessibility Review

Audit designs and implementations against WCAG 2.1 AA standards.

## When Triggered

Activate when the user says "accessibility", "WCAG audit", "is this accessible", "color contrast", "screen reader check", "keyboard navigation", or asks about making designs accessible.

## Usage

```
/accessibility-review $ARGUMENTS
```

Audit for accessibility: @$1

If a Figma URL is provided, pull the design using Figma MCP. If a local file or URL is given, analyze it directly.

## What to Ask (if missing)

- **The design**: Figma URL, screenshot, URL, or detailed description
- **Scope**: Full page audit or specific component?
- **Standard**: WCAG 2.1 AA (default) or AAA?

## WCAG 2.1 AA Quick Reference

### Perceivable
- **1.1.1** Non-text content has alt text
- **1.3.1** Info and structure conveyed semantically
- **1.4.3** Contrast ratio >= 4.5:1 (normal text), >= 3:1 (large text)
- **1.4.11** Non-text contrast >= 3:1 (UI components, graphics)

### Operable
- **2.1.1** All functionality available via keyboard
- **2.4.3** Logical focus order
- **2.4.7** Visible focus indicator
- **2.5.5** Touch target >= 44x44 CSS pixels

### Understandable
- **3.2.1** Predictable on focus (no unexpected changes)
- **3.3.1** Error identification (describe the error)
- **3.3.2** Labels or instructions for inputs

### Robust
- **4.1.2** Name, role, value for all UI components

## Common Issues Checklist

1. Insufficient color contrast
2. Missing form labels
3. No keyboard access to interactive elements
4. Missing alt text on meaningful images
5. Focus traps in modals
6. Missing ARIA landmarks
7. Auto-playing media without controls
8. Time limits without extension options

## Testing Approach

1. Automated scan (catches ~30% of issues)
2. Keyboard-only navigation
3. Screen reader testing (VoiceOver, NVDA)
4. Color contrast verification
5. Zoom to 200% — does layout break?

## Output Format

```markdown
## Accessibility Audit: [Design/Page Name]
**Standard:** WCAG 2.1 AA | **Date:** [Date]

### Summary
**Issues found:** [X] | **Critical:** [X] | **Major:** [X] | **Minor:** [X]

### Findings

#### Perceivable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [e.g. 1.4.3 Contrast] | Critical/Major/Minor | [Fix] |

#### Operable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [e.g. 2.1.1 Keyboard] | Critical/Major/Minor | [Fix] |

#### Understandable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [e.g. 3.3.2 Labels] | Critical/Major/Minor | [Fix] |

#### Robust
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [e.g. 4.1.2 Name, Role, Value] | Critical/Major/Minor | [Fix] |

### Color Contrast Check
| Element | Foreground | Background | Ratio | Required | Pass? |
|---------|-----------|------------|-------|----------|-------|
| [Body text] | [color] | [color] | [X]:1 | 4.5:1 | Yes/No |

### Keyboard Navigation
| Element | Tab Order | Enter/Space | Escape | Arrow Keys |
|---------|-----------|-------------|--------|------------|
| [Element] | [Order] | [Behavior] | [Behavior] | [Behavior] |

### Screen Reader
| Element | Announced As | Issue |
|---------|-------------|-------|
| [Element] | [What SR says] | [Problem if any] |

### Priority Fixes
1. **[Critical fix]** — Affects [who] and blocks [what]
2. **[Major fix]** — Improves [what] for [who]
3. **[Minor fix]** — Nice to have
```

## Figma Integration

If the user provides a Figma URL, use the Figma MCP to inspect color values, font sizes, and touch targets directly. Check component ARIA roles and keyboard behavior in the design spec.

## Local Code Audit (Claude Code)

When working with local code in Claude Code:
- Read HTML/JSX/TSX files to check for missing alt text, ARIA labels, and semantic elements
- Read CSS/SCSS files to verify contrast ratios and focus styles
- Run automated tools if available: `npx axe-core`, `npx pa11y`, or `npx lighthouse --only-categories=accessibility`
- Check `!git diff` for recent changes that may introduce accessibility regressions
- Scan for common code patterns: missing `aria-label`, `role` attributes, keyboard event handlers without `onKeyDown`
