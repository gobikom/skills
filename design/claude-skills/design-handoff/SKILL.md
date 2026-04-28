---
name: design-handoff
description: Generate developer handoff specs from a design — measurements, tokens, states, interactions, responsive behavior, and edge cases. Use when preparing designs for engineering implementation.
argument-hint: "<Figma URL or design description>"
allowed-tools:
  - mcp__claude_ai_Figma__get_design_context
  - mcp__claude_ai_Figma__get_screenshot
  - mcp__claude_ai_Figma__get_metadata
  - mcp__claude_ai_Figma__get_libraries
  - mcp__claude_ai_Figma__get_variable_defs
  - mcp__claude_ai_Figma__get_code_connect_suggestions
  - Read
  - Bash(grep *)
  - Bash(find *)
paths:
  - "**/design/**"
  - "**/specs/**"
  - "**/handoff/**"
  - "**/components/**"
  - "**/*.figma"
---

# Design Handoff

Create clear, complete handoff documentation so developers can implement designs accurately.

## When Triggered

Activate when the user says "handoff", "dev handoff", "developer specs", "implementation spec", "hand off to engineering", "design specs for developers", or when a design needs to be translated into implementation guidance.

## Usage

```
/design-handoff $ARGUMENTS
```

Generate handoff specs for: @$1

If a Figma URL is provided, pull the design using Figma MCP. Otherwise, work from the provided description or screenshot.

## What to Ask (if missing)

- **The design**: Figma URL, screenshot, or detailed description
- **Tech stack** (optional): "React + Tailwind", "SwiftUI", etc. — helps give relevant implementation notes
- **Edge cases** (optional): "What happens with 100 items?" — helps spec boundary conditions

## What to Include

### Visual Specifications
- Exact measurements (padding, margins, widths)
- Design token references (colors, typography, spacing)
- Responsive breakpoints and behavior
- Component variants and states

### Interaction Specifications
- Click/tap behavior
- Hover states
- Transitions and animations (duration, easing)
- Gesture support (swipe, pinch, long-press)

### Content Specifications
- Character limits
- Truncation behavior
- Empty states
- Loading states
- Error states

### Edge Cases
- Minimum/maximum content
- International text (longer strings)
- Slow connections
- Missing data

### Accessibility
- Focus order
- ARIA labels and roles
- Keyboard interactions
- Screen reader announcements

## Handoff Principles

1. **Don't assume** — If it's not specified, the developer will guess. Specify everything.
2. **Use tokens, not values** — Reference `spacing-md` not `16px`.
3. **Show all states** — Default, hover, active, disabled, loading, error, empty.
4. **Describe the why** — "This collapses on mobile because users primarily use one-handed" helps developers make good judgment calls.

## Output Format

```markdown
## Handoff Spec: [Feature/Screen Name]

### Overview
[What this screen/feature does, user context]

### Layout
[Grid system, breakpoints, responsive behavior]

### Design Tokens Used
| Token | Value | Usage |
|-------|-------|-------|
| [token name] | [value] | [where it's used] |

### Components
| Component | Variant | Props | Notes |
|-----------|---------|-------|-------|
| [Component] | [Variant] | [Props] | [Special behavior] |

### States and Interactions
| Element | State | Behavior |
|---------|-------|----------|
| [Element] | Hover / Loading / Error / Disabled | [What happens] |

### Responsive Behavior
| Breakpoint | Changes |
|------------|---------|
| Desktop (>1024px) | [Default layout] |
| Tablet (768-1024px) | [What changes] |
| Mobile (<768px) | [What changes] |

### Edge Cases
- **Empty state**: [What to show when no data]
- **Long text**: [Truncation rules]
- **Loading**: [Skeleton or spinner]
- **Error**: [Error state appearance]

### Animation / Motion
| Element | Trigger | Animation | Duration | Easing |
|---------|---------|-----------|----------|--------|
| [Element] | [Trigger] | [Description] | [ms] | [easing] |

### Accessibility Notes
- [Focus order]
- [ARIA labels needed]
- [Keyboard interactions]
```

## Figma Integration

If the user provides a Figma URL, use the Figma MCP to pull exact measurements, tokens, and component specs. Export assets and generate a complete spec sheet. Use `get_code_connect_suggestions` to map Figma components to existing codebase components. If a project tracker is connected, link the handoff to the implementation ticket.

## Local Code Integration (Claude Code)

When working with local code in Claude Code:
- **Map to existing components**: Scan the codebase for existing components that match the design. Reference them in the handoff spec instead of specifying from scratch.
- **Token mapping**: Read the project's design token files (CSS variables, Tailwind config, Style Dictionary) to use correct token names in the spec.
- **Tech stack detection**: Check `package.json`, framework configs to tailor the handoff to the actual stack (React props vs Vue slots, Tailwind classes vs CSS modules).
- **Code Connect**: If Figma Code Connect is set up, use `get_code_connect_suggestions` to link Figma components directly to codebase components.
- **Generate scaffolding**: Optionally create stub component files with the correct props/types based on the handoff spec.
