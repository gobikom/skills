---
name: design-system
description: Audit, document, or extend your design system — components, tokens, and patterns. Use when reviewing component libraries, creating design tokens, or maintaining design consistency.
argument-hint: "[audit | document | extend] <component or system>"
paths:
  - "**/tokens/**"
  - "**/design-tokens/**"
  - "**/theme/**"
  - "**/styles/**"
  - "**/components/**"
  - "**/ui/**"
  - "**/*.css"
  - "**/*.scss"
  - "**/tailwind.config.*"
  - "**/style-dictionary.*"
---

# Design System Management

Help build, maintain, and evolve design systems.

## When Triggered

Activate when the user says "design system", "component library", "design tokens", "style guide", "audit components", or asks about maintaining consistency across designs.

## Usage

```
/design-system $ARGUMENTS
```

Supported modes:
- `/design-system audit` — Full system audit
- `/design-system document [component]` — Document a component
- `/design-system extend [pattern]` — Design a new component or pattern

## Three Modes

Determine which mode based on user intent:
- **Audit**: "audit design system", "review our components", "check consistency"
- **Document**: "document [component]", "write specs for [component]"
- **Extend**: "new component", "add [pattern] to design system"

## Design System Knowledge

### Design Tokens
Atomic values that define the visual language:
- Colors (brand, semantic, neutral)
- Typography (scale, weights, line heights)
- Spacing (scale, component padding)
- Borders (radius, width)
- Shadows (elevation levels)
- Motion (durations, easings)

### Components
Reusable UI elements with defined:
- Variants (primary, secondary, ghost)
- States (default, hover, active, disabled, loading, error)
- Sizes (sm, md, lg)
- Behavior (interactions, animations)
- Accessibility (ARIA, keyboard)

### Patterns
Common UI solutions combining components:
- Forms (input groups, validation, submission)
- Navigation (sidebar, tabs, breadcrumbs)
- Data display (tables, cards, lists)
- Feedback (toasts, modals, inline messages)

## Principles

1. **Consistency over creativity** — The system exists so teams don't reinvent the wheel
2. **Flexibility within constraints** — Components should be composable, not rigid
3. **Document everything** — If it's not documented, it doesn't exist
4. **Version and migrate** — Breaking changes need migration paths

## Output Format — Audit

```markdown
## Design System Audit

### Summary
**Components reviewed:** [X] | **Issues found:** [X] | **Score:** [X/100]

### Naming Consistency
| Issue | Components | Recommendation |
|-------|------------|----------------|
| [Inconsistent naming] | [List] | [Standard to adopt] |

### Token Coverage
| Category | Defined | Hardcoded Values Found |
|----------|---------|----------------------|
| Colors | [X] | [X] instances of hardcoded hex |
| Spacing | [X] | [X] instances of arbitrary values |
| Typography | [X] | [X] instances of custom fonts/sizes |

### Component Completeness
| Component | States | Variants | Docs | Score |
|-----------|--------|----------|------|-------|
| [Component] | Yes/Partial/No | Yes/Partial/No | Yes/Partial/No | [X/10] |

### Priority Actions
1. [Most impactful improvement]
2. [Second priority]
3. [Third priority]
```

## Output Format — Document

```markdown
## Component: [Name]

### Description
[What this component is and when to use it]

### Variants
| Variant | Use When |
|---------|----------|
| [Primary] | [Main actions] |

### Props / Properties
| Property | Type | Default | Description |
|----------|------|---------|-------------|

### States
| State | Visual | Behavior |
|-------|--------|----------|
| Default / Hover / Active / Disabled / Loading | [description] | [interaction] |

### Accessibility
- **Role**: [ARIA role]
- **Keyboard**: [Tab, Enter, Escape behavior]
- **Screen reader**: [Announced as...]

### Do's and Don'ts
| Do | Don't |
|----|-------|
| [Best practice] | [Anti-pattern] |
```

## Output Format — Extend

```markdown
## New Component: [Name]

### Problem
[What user need or gap this component addresses]

### Existing Patterns
| Related Component | Similarity | Why It's Not Enough |
|-------------------|-----------|---------------------|

### Proposed Design
[API/Props, Variants, States, Tokens Used]

### Accessibility
[Role, Keyboard, Screen reader]

### Open Questions
- [Decisions that need review]
```

## Figma Integration

If the user provides a Figma URL or library, use the Figma MCP to audit components directly — check naming, variants, and token usage. Pull component properties and layer structure for documentation. Use variable definitions and library tools to pull token definitions and component inventory.

## Local Code Integration

When working with local code:
- **Token audit**: Read CSS/SCSS/Tailwind config to find hardcoded values that should be tokens. Grep for raw hex colors, pixel values, and font declarations.
- **Component audit**: Scan component directories to check for consistent naming, prop interfaces, and state coverage.
- **Consistency check**: Compare Figma tokens (via MCP) against code tokens to find drift.
- **Style Dictionary**: If `style-dictionary` config exists, validate token structure and output formats.
- **Tailwind**: If `tailwind.config.*` exists, audit theme extension for consistency with design tokens.
