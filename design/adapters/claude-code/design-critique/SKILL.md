---
name: design-critique
description: "Get structured design feedback on usability, visual hierarchy, accessibility, and consistency. Use when sharing a Figma URL, screenshot, or describing a design for review."
argument-hint: "<Figma URL, screenshot, or description>"
allowed-tools:
  - mcp__claude_ai_Figma__get_design_context
  - mcp__claude_ai_Figma__get_screenshot
  - mcp__claude_ai_Figma__get_metadata
  - mcp__claude_ai_Figma__get_libraries
  - mcp__claude_ai_Figma__search_design_system
  - Read
paths:
  - "**/*.css"
  - "**/*.scss"
  - "**/*.figma"
  - "**/*.sketch"
  - "**/design/**"
  - "**/ui/**"
  - "**/components/**"
---

# Design Critique

Provide structured, actionable design feedback across multiple dimensions.

## When Triggered

Activate when the user says "critique", "review this design", "give me feedback", "what do you think of this design", or shares a design asking for opinions.

## Usage

```
/design-critique $ARGUMENTS
```

Review the design: @$1

If a Figma URL is provided, pull the design using Figma MCP. If a file is referenced, read it. Otherwise, ask the user to describe or share their design.

## What to Ask (if missing)

- **The design**: Figma URL, screenshot, or detailed description
- **Context**: What is this? Who is it for? What stage (exploration, refinement, final)?
- **Focus** (optional): "Focus on mobile" or "Focus on the onboarding flow"

## Critique Framework

### 1. First Impression (2 seconds)
- What draws the eye first? Is that correct?
- What's the emotional reaction?
- Is the purpose immediately clear?

### 2. Usability
- Can the user accomplish their goal?
- Is the navigation intuitive?
- Are interactive elements obvious?
- Are there unnecessary steps?

### 3. Visual Hierarchy
- Is there a clear reading order?
- Are the right elements emphasized?
- Is whitespace used effectively?
- Is typography creating the right hierarchy?

### 4. Consistency
- Does it follow the design system?
- Are spacing, colors, and typography consistent?
- Do similar elements behave similarly?

### 5. Accessibility
- Color contrast ratios (>= 4.5:1 normal text, >= 3:1 large text)
- Touch target sizes (>= 44x44px)
- Text readability
- Alternative text for images

## Feedback Principles

- **Be specific**: "The CTA competes with the navigation" not "the layout is confusing"
- **Explain why**: Connect feedback to design principles or user needs
- **Suggest alternatives**: Don't just identify problems, propose solutions
- **Acknowledge what works**: Good feedback includes positive observations
- **Match the stage**: Early exploration gets different feedback than final polish

## Output Format

```markdown
## Design Critique: [Design Name]

### Overall Impression
[1-2 sentence first reaction — what works, what's the biggest opportunity]

### Usability
| Finding | Severity | Recommendation |
|---------|----------|----------------|
| [Issue] | Critical / Moderate / Minor | [Fix] |

### Visual Hierarchy
- **What draws the eye first**: [Element] — [Is this correct?]
- **Reading flow**: [How does the eye move through the layout?]
- **Emphasis**: [Are the right things emphasized?]

### Consistency
| Element | Issue | Recommendation |
|---------|-------|----------------|
| [Typography/spacing/color] | [Inconsistency] | [Fix] |

### Accessibility
- **Color contrast**: [Pass/fail for key text]
- **Touch targets**: [Adequate size?]
- **Text readability**: [Font size, line height]

### What Works Well
- [Positive observation 1]
- [Positive observation 2]

### Priority Recommendations
1. **[Most impactful change]** — [Why and how]
2. **[Second priority]** — [Why and how]
3. **[Third priority]** — [Why and how]
```

## Figma Integration

If the user provides a Figma URL, use the Figma MCP to pull the design and inspect components, tokens, and layers. Compare against the existing design system for consistency.

## Local Code Integration

When working with local files:
- Read CSS/SCSS files to check token usage and consistency
- Read component files to verify implementation matches design intent
- Check recent git changes for design-related modifications that may need review
