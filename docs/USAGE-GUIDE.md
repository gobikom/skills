# UX Writing & Brand Voice — Usage Guide

Complete guide for using the **ux-writing** and **brand-voice** skills with and without UX Copy MCP server.

| Skill | Role |
|-------|------|
| **ux-writing** | Universal copy principles + MCP workflow (search, generate, batch) |
| **brand-voice** | Banking Digital platform rules (capitalization, punctuation, component formats) |

---

## Table of Contents

- [Overview](#overview)
- [Setup Modes](#setup-modes)
- [Use Cases — ux-writing](#use-cases--ux-writing)
  - [1. Write Copy for a New Screen](#1-write-copy-for-a-new-screen)
  - [2. Search Existing Copy](#2-search-existing-copy)
  - [3. Generate Copy with Context](#3-generate-copy-with-context)
  - [4. Batch Process a Full Screen](#4-batch-process-a-full-screen)
  - [5. Multi-Screen Consistency Review](#5-multi-screen-consistency-review)
  - [6. Figma URL to Copy Spec](#6-figma-url-to-copy-spec)
  - [7. Error Messages](#7-error-messages)
  - [8. Empty States](#8-empty-states)
  - [9. Push Notifications](#9-push-notifications)
  - [10. Confirmation Dialogs](#10-confirmation-dialogs)
  - [11. Onboarding Flow](#11-onboarding-flow)
  - [12. Accessibility Labels from Design](#12-accessibility-labels-from-design)
- [Use Cases — brand-voice](#use-cases--brand-voice)
  - [13. Review Copy Against Guideline](#13-review-copy-against-guideline)
  - [14. Write Component-Specific Copy](#14-write-component-specific-copy)
  - [15. Audit Locale Files](#15-audit-locale-files)
  - [16. Combined Workflow: ux-writing + brand-voice](#16-combined-workflow-ux-writing--brand-voice)
- [Output Formats](#output-formats)
- [Tips & Best Practices](#tips--best-practices)

---

## Overview

The ux-writing skill helps you write, review, and manage UX copy for any interface. It operates in two modes:

| Mode | Requirements | Capabilities |
|------|-------------|--------------|
| **With MCP** | UX Copy MCP server registered | Search langpack, AI generation, batch processing, Frontitude CSV export, cross-screen consistency |
| **Without MCP** | None (local files only) | Manual search via grep, write copy using principles, review locale files |

Both modes follow the same UX writing principles and output format. The MCP adds speed, existing copy reuse, and automated consistency checks.

---

## Setup Modes

### Mode A: With UX Copy MCP (recommended)

```bash
# Register in Claude Code
claude mcp add ux-copy \
  --transport sse \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -s user \
  ux-copy https://your-server.example.com/sse
```

After registration, restart the Claude Code session. Verify with:
> "Search for UX copy about transfer success"

### Mode B: Without MCP (local fallback)

No setup needed. The skill uses local files:
- Reads from `locales/`, `i18n/`, `translations/`, `strings/` directories
- Greps for existing patterns
- Writes copy manually following built-in principles

### Mode C: With Figma MCP + UX Copy MCP (full power)

Both MCPs registered enables the Figma URL workflow:
1. Figma MCP extracts design context and text fields
2. UX Copy MCP searches/generates copy for each field
3. Output: complete copy spec with i18n keys

---

## Use Cases

### 1. Write Copy for a New Screen

Write all copy needed for a new screen from scratch.

#### Prompt

```
/ux-writing Transfer Confirmation screen — title, subtitle, amount label, 
recipient label, confirm button, back button, success toast
```

#### With MCP

```
Step 1: match_copy searches langpack for each field
Step 2: Fields with <70% confidence → generate_copy creates 3 options
Step 3: Output includes existing keys + new suggestions + Frontitude CSV
```

**Result:**

| Field | Copy (TH) | Copy (EN) | Key | Status |
|-------|-----------|-----------|-----|--------|
| title | ยืนยันการโอน | Confirm Transfer | `transfer.confirm.title` | Existing |
| subtitle | ตรวจสอบรายละเอียดก่อนกดยืนยัน | Review details before confirming | `transfer.confirm.subtitle` | Existing |
| button_primary | ยืนยัน | Confirm | `common.btn.confirm` | Existing |
| button_secondary | ย้อนกลับ | Back | `common.btn.back` | Existing |
| toast_success | โอนเงินสำเร็จ | Transfer successful | `transfer.confirm.toast.success` | **New** |

#### Without MCP

```
Step 1: grep locale files for "transfer", "confirm", "โอน"
Step 2: Check existing keys and patterns in i18n JSON
Step 3: Write new copy following principles (clear, concise, consistent)
```

**Result:**

```markdown
## UX Copy: Transfer Confirmation

### Recommended Copy
**Title**: ยืนยันการโอน / Confirm Transfer
**Subtitle**: ตรวจสอบรายละเอียดก่อนกดยืนยัน / Review details before confirming
**Button (primary)**: ยืนยัน / Confirm
**Button (secondary)**: ย้อนกลับ / Back
**Toast**: โอนเงินสำเร็จ / Transfer successful

### Rationale
- Button uses verb "ยืนยัน" consistent with other confirmation flows
- Toast follows success pattern: [action]สำเร็จ
```

---

### 2. Search Existing Copy

Find copy that already exists in the system before writing new.

#### Prompt

```
/ux-writing search existing copy for "unable to proceed" in popup dialog
```

#### With MCP

```
match_copy(text="unable to proceed", placement="Popup / Dialog")
```

**Result:**

```json
{
  "query": "unable to proceed",
  "total_matches": 3,
  "matches": [
    {
      "key": "lg_request_detail_error_header",
      "th": "ไม่สามารถดำเนินการได้",
      "en": "Unable to Proceed",
      "confidence": 95.2,
      "source": "langpack"
    },
    {
      "key": "lg_common_error_cannot_process",
      "th": "ไม่สามารถทำรายการได้",
      "en": "Cannot Process Request",
      "confidence": 78.5,
      "source": "langpack"
    }
  ]
}
```

**Action**: Confidence >= 95% → reuse `lg_request_detail_error_header` directly.

#### Without MCP

```bash
# Grep locale files
grep -ri "unable\|cannot\|ไม่สามารถ" locales/*.json | grep -i "proceed\|process\|ดำเนินการ"
```

**Result**: Manual search results — review matches and decide which key to reuse.

---

### 3. Generate Copy with Context

Generate new copy with specific context, placement, and tone.

#### Prompt

```
/ux-writing generate copy for success toast after fund transfer completed, 
mobile app, formal tone, max 40 characters
```

#### With MCP

```
generate_copy(
  context="User just completed a fund transfer successfully",
  placement="Toast / Snackbar",
  intent="Success",
  device="Mobile",
  product="Transfer"
)
```

**Result:**

| Option | TH | EN | Tone |
|--------|----|----|------|
| A | โอนเงินสำเร็จแล้ว | Transfer successful | Clear & Reassuring |
| B | ส่งเงินไปยังบัญชีปลายทางเรียบร้อย | Funds sent to recipient | Informative |
| C | ทำรายการโอนเงินสำเร็จ | Transfer complete | Warm & Confirmatory |

Plus: Frontitude CSV row ready for import, guideline rule reference.

#### Without MCP

Apply writing principles manually:

```markdown
## UX Copy: Transfer Success Toast

### Recommended Copy
**Toast**: โอนเงินสำเร็จแล้ว / Transfer successful

### Alternatives
| Option | TH | EN | Tone | Best For |
|--------|----|----|------|----------|
| A | โอนเงินสำเร็จแล้ว | Transfer successful | Formal | Default |
| B | โอนเรียบร้อย | Transfer done | Casual | Younger audience |
| C | ส่งเงินสำเร็จ ดูรายละเอียดได้ที่ประวัติ | Sent! View in history. | Actionable | When next step matters |

### Rationale
- Option A: follows success pattern "[action]สำเร็จแล้ว", under 40 chars
- Toast = transient → must be scannable in 3 seconds
```

---

### 4. Batch Process a Full Screen

Process all text fields on a screen in one call.

#### Prompt

```
/ux-writing process screen: Payment Details
- title: "รายละเอียดการชำระเงิน"
- amount_label: "จำนวนเงิน"
- recipient_label: "ผู้รับเงิน"  
- date_label: "วันที่ทำรายการ"
- button_pay: "ชำระเงิน"
- button_cancel: "ยกเลิก"
```

#### With MCP

```
process_screen(
  screen_context="Payment details review before executing payment",
  fields=[
    {"component": "title", "placement": "Title", "context": "screen header", "current_text": "รายละเอียดการชำระเงิน"},
    {"component": "amount_label", "placement": "Label", "context": "amount field", "current_text": "จำนวนเงิน"},
    {"component": "recipient_label", "placement": "Label", "context": "recipient field", "current_text": "ผู้รับเงิน"},
    {"component": "date_label", "placement": "Label", "context": "transaction date", "current_text": "วันที่ทำรายการ"},
    {"component": "button_pay", "placement": "Button / CTA", "context": "primary action", "current_text": "ชำระเงิน", "intent": "Confirm"},
    {"component": "button_cancel", "placement": "Button / CTA", "context": "secondary action", "current_text": "ยกเลิก", "intent": "Confirm"}
  ],
  device="Mobile",
  product="Payment"
)
```

**Result per field:**

| Field | Match Type | Existing Key | Confidence | Action |
|-------|-----------|--------------|------------|--------|
| title | exact | `payment.detail.title` | 98% | Reuse as-is |
| amount_label | exact | `common.label.amount` | 96% | Reuse as-is |
| recipient_label | partial | `common.label.recipient` | 82% | Show match + alternatives |
| date_label | exact | `common.label.date` | 95% | Reuse as-is |
| button_pay | partial | `common.btn.pay` | 88% | Show match + alternatives |
| button_cancel | exact | `common.btn.cancel` | 99% | Reuse as-is |

#### Without MCP

```bash
# Check each field against locale files
grep -r "รายละเอียดการชำระ\|payment.*detail" locales/
grep -r "จำนวนเงิน\|amount" locales/
grep -r "ผู้รับเงิน\|recipient" locales/
# ... for each field
```

Then manually compile the results into the same table format.

---

### 5. Multi-Screen Consistency Review

Review copy across multiple screens for consistency.

#### Prompt

```
/ux-writing review consistency across transfer flow:
- Screen 1: Enter Amount (button: "ถัดไป")
- Screen 2: Select Recipient (button: "ถัดไป") 
- Screen 3: Review Details (button: "ยืนยันการโอน")
- Screen 4: OTP Verification (button: "ยืนยัน")
- Screen 5: Success (button: "เสร็จสิ้น")
```

#### With MCP

```
process_screens(
  screens=[
    {name: "Enter Amount", context: "...", fields: [...]},
    {name: "Select Recipient", context: "...", fields: [...]},
    {name: "Review Details", context: "...", fields: [...]},
    {name: "OTP Verification", context: "...", fields: [...]},
    {name: "Success", context: "...", fields: [...]}
  ],
  product="Transfer"
)
```

**Consistency checks (automatic):**

```
⚠️ CTA Verb Sprawl Detected:
  - Screen 1-2: "ถัดไป" (Next)
  - Screen 3: "ยืนยันการโอน" (Confirm Transfer)  
  - Screen 4: "ยืนยัน" (Confirm)
  - Screen 5: "เสร็จสิ้น" (Done)
  
  Issue: Screen 3 and 4 use different "confirm" variants
  Recommendation: Standardize to "ยืนยัน" for both, 
  or "ยืนยันการโอน" for screen 3 (final action) and "ยืนยัน OTP" for screen 4

✅ Tone: Consistent formal tone across all screens
✅ Terminology: "โอนเงิน" used consistently (no "ส่งเงิน" / "โอน" mixing)
```

#### Without MCP

Manual review:

```markdown
## Consistency Review: Transfer Flow

### CTA Buttons Across Flow
| Screen | CTA (TH) | CTA (EN) | Consistent? |
|--------|-----------|-----------|-------------|
| Enter Amount | ถัดไป | Next | ✅ |
| Select Recipient | ถัดไป | Next | ✅ |
| Review Details | ยืนยันการโอน | Confirm Transfer | ⚠️ Different pattern |
| OTP Verification | ยืนยัน | Confirm | ⚠️ Shortened |
| Success | เสร็จสิ้น | Done | ✅ (terminal) |

### Issues Found
1. **CTA verb inconsistency**: "ยืนยันการโอน" vs "ยืนยัน" — pick one pattern
2. **Recommendation**: Use full action verb for irreversible actions ("ยืนยันการโอน"), 
   short form for verification steps ("ยืนยัน")

### Terminology Check
- "โอนเงิน" ✅ — used consistently, no variants like "ส่งเงิน"
- "ผู้รับ" ✅ — used consistently, no variants like "ปลายทาง"
```

---

### 6. Figma URL to Copy Spec

Extract all copy from a Figma design and produce a complete spec.

#### Prompt

```
/ux-writing figma.com/design/abc123/TransferFlow?node-id=12:34
```

#### With MCP (Figma + UX Copy)

```
1. Figma MCP → get_design_context(fileKey="abc123", nodeId="12:34")
   Output: all text layers, constraints, layout info

2. Identify text fields from design:
   - title: "Transfer Confirmation"
   - subtitle: "Please review before confirming"
   - label_amount: "Amount"
   - label_recipient: "To"
   - button_primary: "Confirm"
   - button_secondary: "Cancel"

3. UX Copy MCP → process_screen(fields=[...])
   For each field: search existing → generate if needed

4. Output: Complete copy spec + Frontitude CSV
```

**Result:**

```markdown
## Copy Spec: Transfer Confirmation
**Source**: figma.com/design/abc123/TransferFlow?node-id=12:34
**Extracted**: 6 text fields | 4 existing | 2 new

### Field Mapping

| # | Layer (Figma) | Copy (TH) | Copy (EN) | i18n Key | Status |
|---|---------------|-----------|-----------|----------|--------|
| 1 | title | ยืนยันการโอน | Transfer Confirmation | `transfer.confirm.title` | ✅ Existing |
| 2 | subtitle | กรุณาตรวจสอบก่อนยืนยัน | Please review before confirming | `transfer.confirm.subtitle` | ✅ Existing |
| 3 | label_amount | จำนวนเงิน | Amount | `common.label.amount` | ✅ Existing |
| 4 | label_to | ผู้รับ | To | `common.label.recipient` | ✅ Existing |
| 5 | btn_confirm | ยืนยันการโอน | Confirm Transfer | `transfer.confirm.btn.primary` | 🆕 New |
| 6 | btn_cancel | ยกเลิก | Cancel | `common.btn.cancel` | ✅ Existing |

### Missing States (not in design)
| State | Recommended Copy (TH) | Recommended Copy (EN) | Proposed Key |
|-------|----------------------|----------------------|--------------|
| Success toast | โอนเงินสำเร็จ | Transfer successful | `transfer.toast.success` |
| Error: insufficient | ยอดเงินไม่เพียงพอ | Insufficient balance | `transfer.error.insufficient` |
| Error: network | ไม่สามารถโอนได้ ลองใหม่อีกครั้ง | Transfer failed. Try again. | `transfer.error.network` |
| Loading | กำลังดำเนินการ... | Processing... | `transfer.loading` |

### Frontitude CSV
File: `frontitude-export-transfer-confirm-20260505.csv` (ready for import)

```csv
Name,Unique key,Context,Value,Value (English - en),Value (Thai - th),Status,Tags,Copy guidelines,Updated at,Last Edited By,Frontitude link
Krungthai Business / 03 Title / Transfer Confirmation / 001 Title_mobile,Krungthai Business / 03 Title / Transfer Confirmation / 001 Title_mobile,Transfer confirmation screen,Transfer Confirmation,Transfer Confirmation,ยืนยันการโอน,Review,"Transfer, Mobile",Title Case for headers,2026-05-05,,
Krungthai Business / 05 Button / Confirm Transfer / 005 Button_mobile,Krungthai Business / 05 Button / Confirm Transfer / 005 Button_mobile,Primary CTA,CONFIRM TRANSFER,CONFIRM TRANSFER,ยืนยันการโอน,Draft,"Transfer, Mobile, AI Generated",UPPERCASE for primary buttons,2026-05-05,,
Krungthai Business / 08 Informing / Transfer Success / 006 Toast_mobile,Krungthai Business / 08 Informing / Transfer Success / 006 Toast_mobile,Success toast,Successfully transferred.,Successfully transferred.,โอนเงินสำเร็จ,Draft,"Transfer, Mobile, AI Generated","Success: EN 'Successfully [past verb].'",2026-05-05,,
Krungthai Business / 06 Error / Insufficient Balance / 007 Error_mobile,Krungthai Business / 06 Error / Insufficient Balance / 007 Error_mobile,Error state,Insufficient balance,Insufficient balance,ยอดเงินไม่เพียงพอ,Draft,"Transfer, Mobile, AI Generated",Sentence case for errors,2026-05-05,,
```

### Design Notes
- ⚠️ Button width: 140px — Thai text fits (6 chars), verify with longer alternatives
- ⚠️ No error state designed — recommend adding to Figma
- ✅ Toast component exists in design system
```

#### Without MCP (Figma only)

```
1. Figma MCP → get_design_context (still works)
2. Extract text fields manually from design layers
3. Grep local locale files for matches
4. Write new copy following principles
5. Output same format but without confidence scores or CSV
```

#### Without any MCP (fully manual)

```
User describes the screen → skill writes copy based on context provided.
No automated extraction from design.
```

---

### 7. Error Messages

Write clear, empathetic error messages.

#### Prompt

```
/ux-writing error messages for payment failure scenarios:
- Card declined
- Insufficient balance  
- Network timeout
- Daily limit exceeded
```

#### With MCP

```
For each error:
1. match_copy("card declined", placement="Popup / Dialog") → check existing
2. If not found → generate_copy(intent="Error", placement="Popup / Dialog")
```

**Result:**

| Scenario | TH | EN | Key |
|----------|----|----|-----|
| Card declined | บัตรถูกปฏิเสธ กรุณาใช้บัตรใบอื่นหรือติดต่อธนาคาร | Card declined. Try another card or contact your bank. | `payment.error.card_declined` |
| Insufficient balance | ยอดเงินไม่เพียงพอ กรุณาเติมเงินหรือลดจำนวน | Insufficient balance. Top up or reduce the amount. | `payment.error.insufficient` |
| Network timeout | ไม่สามารถเชื่อมต่อได้ กรุณาลองใหม่อีกครั้ง | Connection failed. Please try again. | `payment.error.network` |
| Daily limit | เกินวงเงินรายวัน กรุณาทำรายการใหม่พรุ่งนี้หรือปรับวงเงิน | Daily limit reached. Try again tomorrow or increase your limit. | `payment.error.daily_limit` |

#### Without MCP

```markdown
## UX Copy: Payment Error Messages

### Pattern: What happened + Why + How to fix

| Scenario | Copy (TH) | Copy (EN) |
|----------|-----------|-----------|
| Card declined | บัตรถูกปฏิเสธ กรุณาใช้บัตรใบอื่นหรือติดต่อธนาคาร | Card declined. Try another card or contact your bank. |
| Insufficient balance | ยอดเงินไม่เพียงพอ กรุณาเติมเงินหรือลดจำนวน | Insufficient balance. Top up or reduce the amount. |
| Network timeout | ไม่สามารถเชื่อมต่อได้ กรุณาลองใหม่อีกครั้ง | Connection failed. Please try again. |
| Daily limit | เกินวงเงินรายวัน กรุณาทำรายการใหม่พรุ่งนี้หรือปรับวงเงิน | Daily limit reached. Try again tomorrow or increase your limit. |

### Rationale
- Each message: cause + action (no "An error occurred")
- TH uses polite particle where appropriate
- Actionable: user knows what to do next
```

---

### 8. Empty States

Guide users from "nothing here" to their first action.

#### Prompt

```
/ux-writing empty state for Transaction History — first-time user, no transactions yet
```

#### With MCP

```
generate_copy(
  context="First-time user viewing transaction history, no transactions yet",
  placement="Empty State",
  intent="Guide / Instruct",
  product="Transfer"
)
```

**Result:**

| Option | Title (TH) | Description (TH) | CTA (TH) |
|--------|-----------|-------------------|-----------|
| A | ยังไม่มีรายการ | เริ่มโอนเงินครั้งแรกเพื่อดูประวัติที่นี่ | โอนเงิน |
| B | ประวัติรายการว่างเปล่า | ทำรายการโอนหรือชำระเงินเพื่อเริ่มต้น | ทำรายการ |
| C | ไม่พบรายการ | รายการจะแสดงที่นี่เมื่อคุณโอนเงินหรือชำระเงิน | เริ่มโอนเงิน |

#### Without MCP

```markdown
## UX Copy: Empty State — Transaction History

### Structure: What this is + Why it's empty + How to start

### Recommended
**Title**: ยังไม่มีรายการ / No transactions yet
**Description**: รายการจะแสดงที่นี่เมื่อคุณทำรายการโอนหรือชำระเงิน / Your transactions will appear here once you make a transfer or payment.
**CTA**: โอนเงิน / Make a Transfer

### Rationale
- Title acknowledges the empty state without blame
- Description sets expectations (what will appear)
- CTA is specific action, not generic "Get Started"
```

---

### 9. Push Notifications

Write short, scannable notification copy.

#### Prompt

```
/ux-writing push notification — transfer of ฿5,000 received from John, mobile
```

#### With MCP

```
generate_copy(
  context="User received ฿5,000 transfer from John",
  placement="Push Notification",
  intent="Inform",
  device="Mobile",
  product="Transfer"
)
```

**Result:**

| Option | Title | Body | Chars |
|--------|-------|------|-------|
| A | ได้รับเงินโอน ฿5,000 | จาก John เข้าบัญชี xxx-x-x1234 | title: 18, body: 25 |
| B | รับเงิน ฿5,000 สำเร็จ | โอนจาก John ถึงแล้ว | title: 16, body: 17 |
| C | 💰 ฿5,000 เข้าบัญชีแล้ว | โอนจาก John — ดูรายละเอียด | title: 17, body: 22 |

#### Without MCP

```markdown
## UX Copy: Push Notification — Transfer Received

### Constraints
- Title: max 50 chars (iOS) / 65 chars (Android)
- Body: max 100 chars
- Must be scannable in lock screen glance

### Recommended
**Title**: ได้รับเงินโอน ฿5,000
**Body**: จาก John เข้าบัญชี xxx-x-x1234

### Rationale
- Amount in title (most important info)
- Sender in body (context)
- Account number partially masked (security)
```

---

### 10. Confirmation Dialogs

Make consequences clear, label buttons with actions.

#### Prompt

```
/ux-writing confirmation dialog for deleting a saved beneficiary account
```

#### With MCP

```
generate_copy(
  context="User wants to delete a saved beneficiary from their transfer favorites list",
  placement="Popup / Dialog",
  intent="Confirm",
  product="Transfer"
)
```

**Result:**

| Element | TH | EN |
|---------|----|----|
| Title | ลบบัญชีผู้รับ "ชื่อ"? | Delete beneficiary "Name"? |
| Body | บัญชีนี้จะถูกลบออกจากรายการโปรด คุณสามารถเพิ่มกลับได้ภายหลัง | This account will be removed from favorites. You can add it back later. |
| Primary button | ลบบัญชี | Delete |
| Secondary button | ยกเลิก | Cancel |

#### Without MCP

```markdown
## UX Copy: Confirmation Dialog — Delete Beneficiary

### Pattern: Make action clear + Describe consequences + Action buttons

### Recommended
**Title**: ลบบัญชีผู้รับ "[name]"?
**Body**: บัญชีนี้จะถูกลบออกจากรายการโปรด คุณสามารถเพิ่มกลับได้ภายหลัง
**Primary**: ลบบัญชี (destructive style)
**Secondary**: ยกเลิก

### Anti-patterns to avoid
- ❌ "Are you sure?" — vague, doesn't describe what happens
- ❌ "OK / Cancel" — doesn't tell user what OK does
- ❌ "This action cannot be undone" — only say if actually irreversible
```

---

### 11. Onboarding Flow

Progressive disclosure — one concept per step.

#### Prompt

```
/ux-writing onboarding flow for biometric login feature, 4 steps, mobile
```

#### With MCP

```
process_screens(
  screens=[
    {name: "Step 1 - Intro", context: "Introduce biometric feature", fields: [title, description, cta]},
    {name: "Step 2 - Permission", context: "Request biometric permission", fields: [title, description, cta, skip]},
    {name: "Step 3 - Setup", context: "Scan fingerprint/face", fields: [title, description, instruction]},
    {name: "Step 4 - Success", context: "Biometric registered", fields: [title, description, cta]}
  ],
  device="Mobile"
)
```

**Result with consistency check:**

| Step | Title (TH) | CTA (TH) |
|------|-----------|-----------|
| 1 - Intro | เข้าสู่ระบบด้วยใบหน้าหรือลายนิ้วมือ | เริ่มตั้งค่า |
| 2 - Permission | อนุญาตการใช้งาน Biometric | อนุญาต |
| 3 - Setup | สแกนใบหน้าหรือลายนิ้วมือ | — (auto-proceed) |
| 4 - Success | ตั้งค่าสำเร็จ! | เริ่มใช้งาน |

```
✅ Tone: Consistent friendly-formal across all steps
✅ CTA progression: เริ่มตั้งค่า → อนุญาต → (auto) → เริ่มใช้งาน (logical flow)
✅ No jargon: "Biometric" used only once, rest uses "ใบหน้าหรือลายนิ้วมือ"
```

#### Without MCP

Write each step manually following progressive disclosure principles:
- 1 concept per screen
- Short title + brief description
- CTA that matches the next action
- Allow skip for non-essential steps

---

### 12. Accessibility Labels from Design

Generate ARIA labels and alt text for unlabeled design elements.

#### Prompt

```
/ux-writing generate accessibility labels for:
figma.com/design/abc123/Dashboard?node-id=5:10
```

#### With MCP (Figma + UX Copy)

```
1. Figma MCP → get_design_context → find elements without text labels
   - Icon button (transfer icon, no label)
   - Chart (bar chart showing monthly spending)
   - Avatar image (user profile)
   
2. UX Copy MCP → generate_copy for each:
   generate_copy(
     context="Transfer icon button on dashboard",
     placement="Accessibility Label",
     intent="Inform"
   )
```

**Result:**

| Element | Type | Label (TH) | Label (EN) |
|---------|------|-----------|-----------|
| Transfer icon | `aria-label` | โอนเงิน | Transfer funds |
| Bar chart | `aria-describedby` | กราฟแสดงยอดใช้จ่ายรายเดือน มกราคม ถึง มิถุนายน | Monthly spending chart, January to June |
| Profile avatar | `alt` | รูปโปรไฟล์ของ [ชื่อ] | [Name]'s profile photo |
| Notification bell | `aria-label` | การแจ้งเตือน (3 รายการใหม่) | Notifications (3 new) |

#### Without MCP

```markdown
## Accessibility Labels: Dashboard

### Guidelines
- Icon buttons: describe the action, not the icon ("Transfer funds" not "Arrow icon")
- Charts: describe what data is shown, not how it looks
- Images: describe the content and purpose
- Include dynamic state in labels when relevant (badge count, status)

### Labels
| Element | Attribute | Label |
|---------|-----------|-------|
| Transfer icon | aria-label | "โอนเงิน" / "Transfer funds" |
| Chart | aria-describedby | "กราฟยอดใช้จ่ายรายเดือน" / "Monthly spending chart" |
| Avatar | alt | "รูปโปรไฟล์ของ [ชื่อ]" / "[Name]'s profile photo" |
```

---

## Use Cases — brand-voice

### 13. Review Copy Against Guideline

Check if existing copy follows all brand rules.

#### Prompt

```
/brand-voice review "Successfully transferred! Your money is on its way."
```

#### Result

```markdown
## Brand Voice Review: Toast Message

### Copy Reviewed
"Successfully transferred! Your money is on its way."

### Violations Found
| # | Rule | Violation | Fix |
|---|------|-----------|-----|
| 1 | Exclamation marks | "!" is strictly forbidden | Remove exclamation mark |
| 2 | Toast pattern | Should follow "Successfully [past verb]." | Use "Successfully transferred." |
| 3 | Sentence count | Toast must be 1 sentence | Remove second sentence |
| 4 | Contractions | Informal tone not matching brand | N/A (no contraction here) |

### Corrected Copy
**EN**: Successfully transferred.
**TH**: โอนเงินสำเร็จ

### Compliance Score
4/10 — 3 violations found in a single toast message
```

---

### 14. Write Component-Specific Copy

Write copy that follows the exact format for a specific component type.

#### Prompt

```
/brand-voice write inline-error for invalid PromptPay ID
```

#### Result

```markdown
## Brand Voice Copy: Inline Error — Invalid PromptPay ID

### Copy
**EN (field-level)**: Incorrect PromptPay ID
**TH (field-level)**: หมายเลขพร้อมเพย์ไม่ถูกต้อง

**EN (form-level)**: Unable to proceed. Please enter a valid PromptPay ID.
**TH (form-level)**: ไม่สามารถดำเนินการต่อได้ กรุณาระบุหมายเลขพร้อมเพย์ที่ถูกต้อง

### Rules Applied
- Sentence case (inline error)
- Field-level: state what is wrong (not how to fix)
- Form-level: action-oriented, tell how to fix
- Never blame user ("Incorrect" not "You entered wrong")
- No exclamation marks
```

#### More component examples

**Toast (success):**
```
/brand-voice write toast success for export report
→ EN: "Successfully exported."  |  TH: "ส่งออกข้อมูลสำเร็จ"
```

**Toast (fail + retry):**
```
/brand-voice write toast fail-retry for export report
→ EN: "Unable to export. Please try again."  |  TH: "ไม่สามารถส่งออกข้อมูลได้ กรุณาลองใหม่อีกครั้ง"
```

**Button (primary):**
```
/brand-voice write button primary for approve transaction
→ EN: "APPROVE"  |  TH: "อนุมัติ"
```

**Empty state:**
```
/brand-voice write empty-state for no transactions found
→ Title EN: "No Transaction Found"  |  Title TH: "ไม่พบรายการ"
→ Body EN: "You have no transaction history. Make your first transfer to see it here."
→ Body TH: "ยังไม่มีประวัติรายการ ทำรายการโอนเงินครั้งแรกเพื่อดูที่นี่"
```

**Placeholder:**
```
/brand-voice write placeholder for search account
→ EN: "Search by account number or name"  |  TH: "ค้นหาโดยเลขบัญชีหรือชื่อ"
```

**Push notification:**
```
/brand-voice write push-notification for payment due reminder
→ Title EN: "Payment Due Tomorrow" (Title Case, <50 chars)
→ Body EN: "Your credit card payment of THB 15,000 is due tomorrow. Pay now to avoid late fees." (<100 chars)
→ Title TH: "ครบกำหนดชำระพรุ่งนี้"
→ Body TH: "ยอดบัตรเครดิต 15,000 บาท ครบกำหนดพรุ่งนี้ ชำระเลยเพื่อหลีกเลี่ยงค่าปรับ"
```

---

### 15. Audit Locale Files

Scan locale/i18n files for guideline violations.

#### Prompt

```
/brand-voice audit
```

#### Result

```markdown
## Brand Voice Audit: locales/en.json + locales/th.json

### Summary
**Files scanned**: 2 | **Keys checked**: 342 | **Violations**: 18 | **Score**: 85/100

### Violations by Rule
| Rule | Count | Severity | Examples |
|------|-------|----------|---------|
| Exclamation marks | 5 | High | `toast.success.transfer`: "Transfer complete!" → "Successfully transferred." |
| Button capitalization | 4 | High | `btn.submit`: "Submit" → "SUBMIT" (primary) or keep Title Case (secondary) |
| Contraction | 3 | Medium | `error.auth`: "can't login" → "cannot log in" |
| Toast pattern | 3 | Medium | `toast.fail.export`: "Export failed" → "Unable to export." |
| Pronoun (ท่าน) | 2 | Medium | `welcome.msg`: "ท่านสามารถ..." → "คุณสามารถ..." |
| Missing Oxford comma | 1 | Low | `info.fields`: "name, email and phone" → "name, email, and phone" |

### Top Fixes (batch)
1. **Remove all exclamation marks** — grep `!` in locale files, replace with period
2. **Uppercase primary buttons** — grep `btn.primary.*` keys, apply UPPERCASE
3. **Replace contractions** — grep `can't|don't|won't|isn't`, expand to full form
```

---

### 16. Combined Workflow: ux-writing + brand-voice

The most powerful workflow uses both skills together.

#### Prompt

```
/ux-writing write copy for transfer confirmation screen
/brand-voice review [output from ux-writing]
```

#### Flow

```
Step 1: ux-writing (workflow)
├── match_copy → find existing copy
├── generate_copy → create new options
└── Output: copy spec with alternatives

Step 2: brand-voice (validation)
├── Check capitalization rules
├── Check punctuation (no !, Oxford comma)
├── Check component format (toast pattern, button case)
├── Check vocabulary (no contractions, no ท่าน)
└── Output: compliance report + corrected copy

Step 3: Final output
├── Copy that passes both universal quality AND brand rules
├── i18n keys (existing + new)
└── Frontitude CSV ready for import
```

#### Example: Toast comes back from MCP with "!"

```
ux-writing generates: "Transfer successful!"
brand-voice catches:
  ⚠️ Exclamation mark forbidden
  ⚠️ Should follow pattern: "Successfully [past verb]."
brand-voice corrects: "Successfully transferred."
```

---

## Output Formats

### Standard Copy Spec (default)

```markdown
## UX Copy: [Context]

### Recommended Copy
**[Element]**: [Copy TH] / [Copy EN]

### Alternatives
| Option | TH | EN | Tone | Best For |
|--------|----|----|------|----------|
| A | [Copy] | [Copy] | [Tone] | [When to use] |
| B | [Copy] | [Copy] | [Tone] | [When to use] |
| C | [Copy] | [Copy] | [Tone] | [When to use] |

### Rationale
[Why this copy works]

### Localization Notes
[Notes for translators]
```

### i18n Key Mapping (with MCP)

```markdown
| Field | Copy (TH) | Copy (EN) | Key | Status |
|-------|-----------|-----------|-----|--------|
| [field] | [th] | [en] | [key] | Existing/New |
```

### Frontitude CSV File (auto-generated after bulk process)

After `process_screen` or `process_screens`, a CSV file is created in the Frontitude import format:

```csv
Name,Unique key,Context,Value,Value (English - en),Value (Thai - th),Status,Tags,Copy guidelines,Updated at,Last Edited By,Frontitude link
Krungthai Business / 03 Title / Transfer Confirmation / 001 Title_mobile,Krungthai Business / 03 Title / Transfer Confirmation / 001 Title_mobile,Transfer confirmation screen,Confirm Transfer,Confirm Transfer,ยืนยันการโอน,Review,"Transfer, Mobile, AI Generated",Title Case for headers,2026-05-05,,
Krungthai Business / 05 Button / Confirm Transfer / 002 Button_mobile,Krungthai Business / 05 Button / Confirm Transfer / 002 Button_mobile,Primary CTA on confirmation,CONFIRM,CONFIRM,ยืนยัน,Draft,"Transfer, Mobile, AI Generated",UPPERCASE for primary buttons,2026-05-05,,
Krungthai Business / 08 Informing / Transfer Success / 003 Toast_mobile,Krungthai Business / 08 Informing / Transfer Success / 003 Toast_mobile,Success toast after transfer,Successfully transferred.,Successfully transferred.,โอนเงินสำเร็จ,Draft,"Transfer, Mobile, AI Generated","Success: EN 'Successfully [past verb].' / TH '[action]สำเร็จ'",2026-05-05,,
```

**File output**: `frontitude-export-{screen}-{date}.csv` — ready for direct import into Frontitude.

**Column mapping**:

| Column | Source |
|--------|--------|
| Name | `{platform} / {category} / {copy_name} / {id}` |
| Unique key | Same as Name |
| Context | Screen/flow context from input |
| Value | EN copy (default value) |
| Value (English - en) | EN copy |
| Value (Thai - th) | TH copy |
| Status | `Draft` (new) or `Review` (partial match) |
| Tags | Product, device, "AI Generated" |
| Copy guidelines | Guideline rule applied |
| Updated at | Current date |

---

## Tips & Best Practices

### General

1. **Be specific about context** — "Error message when payment fails due to insufficient balance" is better than "error message"
2. **Mention constraints** — Character limits, platform (iOS/Android), audience (new user vs power user)
3. **Share brand voice** — "We're professional but warm" helps match tone
4. **Include user emotional state** — Error messages need empathy, success can celebrate

### With MCP

1. **Always search first** — `match_copy` before `generate_copy` to avoid duplicating existing keys
2. **Use batch tools for screens** — `process_screen` is more efficient than individual calls
3. **Leverage consistency checks** — `process_screens` for multi-screen flows catches drift automatically
4. **Review confidence scores** — >= 95% reuse directly, 70-95% review carefully, < 70% write new

### Without MCP

1. **Grep before writing** — Check locale files for existing patterns
2. **Document new keys** — When you write new copy, propose the i18n key name
3. **Cross-reference manually** — Check other screens in the same flow for consistency
4. **Follow the patterns** — Error = What + Why + Fix, Empty = What + Why + Start, CTA = Verb + Object

### With Figma MCP

1. **Check character limits** — Auto-layout vs fixed width affects how much text fits
2. **Note missing states** — Flag error/loading/empty states not in design
3. **Verify text expansion** — Thai is often longer than English, German is 2-3x longer
4. **Map to components** — Link copy to design system components for reuse

### With brand-voice

1. **Run review after writing** — Always validate ux-writing output against brand rules
2. **Know your component** — Different components have different capitalization and format rules
3. **Audit before PR** — Run `/brand-voice audit` on locale files to catch violations early
4. **Most common violations** — Exclamation marks, wrong button capitalization, contractions, wrong toast pattern
5. **TH-specific rules** — No question marks, verb-first buttons, คุณ not ท่าน, full currency names
