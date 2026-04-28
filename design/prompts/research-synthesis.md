---
name: research-synthesis
description: Synthesize user research into themes, insights, and recommendations. Use when analyzing interview transcripts, survey results, usability tests, or any user feedback data.
argument-hint: "<research data, transcripts, or survey results>"
paths:
  - "**/research/**"
  - "**/user-research/**"
  - "**/interviews/**"
  - "**/surveys/**"
  - "**/feedback/**"
  - "**/*.csv"
  - "**/*.tsv"
---

# Research Synthesis

Synthesize user research data into actionable insights.

## When Triggered

Activate when the user says "research synthesis", "synthesize research", "analyze interviews", "summarize user research", "survey results", "usability findings", or shares research data (transcripts, survey CSV, usability notes, support tickets, NPS/CSAT responses, app store reviews).

## Usage

```
/research-synthesis $ARGUMENTS
```

Synthesize research from: @$1

If a file path or directory is provided, read and analyze the data. If data is pasted directly, work from that.

## What This Skill Accepts

- Interview transcripts or notes
- Survey results (CSV, pasted data)
- Usability test recordings or notes
- Support tickets or feedback
- NPS/CSAT responses
- App store reviews

## Research Methods Reference

| Method | Best For | Sample Size | Time |
|--------|----------|-------------|------|
| User interviews | Deep understanding of needs and motivations | 5-8 | 2-4 weeks |
| Usability testing | Evaluating a specific design or flow | 5-8 | 1-2 weeks |
| Surveys | Quantifying attitudes and preferences | 100+ | 1-2 weeks |
| Card sorting | Information architecture decisions | 15-30 | 1 week |
| Diary studies | Understanding behavior over time | 10-15 | 2-8 weeks |
| A/B testing | Comparing specific design choices | Statistical significance | 1-4 weeks |

## Interview Guide Structure

1. **Warm-up** (5 min): Build rapport, explain the session
2. **Context** (10 min): Understand their current workflow
3. **Deep dive** (20 min): Explore the specific topic
4. **Reaction** (10 min): Show concepts or prototypes
5. **Wrap-up** (5 min): Anything we missed? Thank them.

## Analysis Framework

- **Affinity mapping**: Group observations into themes
- **Impact/effort matrix**: Prioritize findings
- **Journey mapping**: Visualize the user experience over time
- **Jobs to be done**: Understand what users are hiring your product to do

## Key Principles

- **Separate observations from interpretations**: "5 of 8 users clicked the wrong button" is an observation. "The button placement is confusing" is an interpretation.
- **Quantify where possible**: "Most users" is vague. "7 of 10 users" is specific.
- **Include raw quotes**: Direct participant quotes make insights credible and memorable.

## Output Format

```markdown
## Research Synthesis: [Study Name]
**Method:** [Interviews / Survey / Usability Test] | **Participants:** [X]
**Date:** [Date range]

### Executive Summary
[3-4 sentence overview of key findings]

### Key Themes

#### Theme 1: [Name]
**Prevalence:** [X of Y participants]
**Summary:** [What this theme is about]
**Supporting Evidence:**
- "[Quote]" — P[X]
- "[Quote]" — P[X]
**Implication:** [What this means for the product]

#### Theme 2: [Name]
[Same format]

### Insights to Opportunities
| Insight | Opportunity | Impact | Effort |
|---------|-------------|--------|--------|
| [What we learned] | [What we could do] | High/Med/Low | High/Med/Low |

### User Segments Identified
| Segment | Characteristics | Needs | Size |
|---------|----------------|-------|------|
| [Name] | [Description] | [Key needs] | [Rough %] |

### Recommendations
1. **[High priority]** — [Why, based on which findings]
2. **[Medium priority]** — [Why]
3. **[Lower priority]** — [Why]

### Questions for Further Research
- [What we still don't know]

### Methodology Notes
[How the research was conducted, any limitations or biases to note]
```

## Local Code Integration

When working with local files:
- Read CSV/TSV files directly for survey data analysis — count responses, calculate distributions
- Read text/markdown files for interview transcripts and notes
- Scan research directories for all available data files before synthesizing
- Cross-reference multiple data sources in the same directory for richer insights
- Output synthesis as a markdown file in the research directory if the user asks to save it
