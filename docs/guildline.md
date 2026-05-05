## UX Writing Guideline
 
Use the following rules to generate all UX copy for the Banking Digital platform. The goal is to be professional and reliable while remaining approachable and easy to understand.
 
---
 
### **1. Voice and Tone**

* **Professional & Polished:** Use sincere, confident language to build trust.

* **Approachable & Human:** Use plain language and avoid robot-like phrasing.

* **Polite but Not Playful:** Maintain respect without becoming too formal or using humor/slang.

* **Helpful:** Offer clear, easy-to-follow solutions when users might be in doubt.
 
---
 
### **2. Style and Grammar (English)**

* **American English:** Use American spelling (e.g., "Favorite," "Canceled").

    * **Exception:** Use British terms for banking concepts familiar to Thai users (e.g., "Current account," "Cheque").

* **Active Voice:** Always use active voice to be direct. 

    * **Exception:** Use passive voice to soften negative messages or when the subject is unknown (e.g., "Company limits will be deducted").

* **Tense Usage:** * **Present Simple:** Describe general product behavior.

    * **Present Perfect:** Inform users of recently completed actions.

    * **Future Simple:** Only use for actual future outcomes; avoid for standard product behavior.

* **Capitalization:** * **Title Case:** Headers, page titles, sub-headers, email subjects, empty state titles, and secondary buttons (e.g., Next, Done).

    * **Sentence Case:** Pop-up headers, descriptions, tooltip messages, inline errors, placeholders, and toast messages.

    * **Uppercase:** Primary action buttons only (e.g., APPLY, APPROVE, CONFIRM, CANCEL, EXPORT).

* **No Contractions:** Do not use contractions (e.g., use "cannot" instead of "can't") to ensure clarity for skimmers.

* **Action-Oriented:** Start sentences with the objective or the required action (e.g., "To proceed with this transaction, please...").
 
---
 
### **3. Punctuation Rules**

* **Periods:** Use at the end of every sentence.

    * **Exception:** Do not use periods for headers, sub-headers, buttons, or sentences ending in numbers.

* **Commas:** Always use the **Oxford Comma** (serial comma) in English lists

* **Exclamation Marks:** **Strictly forbidden.** Avoid them at all costs to remain informative and non-opinionated.

* **Question Marks:** Use in English for questions; do not use in Thai copy.

* **Ampersands (&):** Use in page titles or headers to save space, with a space before and after.

* **Quotation Marks:** Use double quotes (" ") to refer to specific page names, menus, or CTAs (e.g., Please select "PROCEED").
 
---
 
### **4. Formatting & Components**

* **Numbers:** Use numerals (1, 2, 3) instead of words as much as possible for quick scanning.

* **Dates & Times:** * Abbreviate months (e.g., Aug, Dec) and use four-digit years.

    * Use 24-hour time without "am/pm" (except for maintenance/operating hour alerts).

    * Example when used together is 02 Aug 2020 - 13:00

* **Currencies:** * **English:** Use 3-letter codes (e.g., THB, USD).

    * **Thai:** Use full names (e.g., บาท, ดอลลาร์สหรัฐ).

* **Toasts / Snackbars:**

    * **Success:** EN: `Successfully [past verb].` / TH: `[action]สำเร็จ` (e.g., "Successfully exported." / "ส่งออกข้อมูลสำเร็จ").

    * **Fail:** EN: `Unable to [verb].` / TH: `ไม่สามารถ[action]ได้` (e.g., "Unable to export." / "ไม่สามารถส่งออกข้อมูลได้").

    * **Fail + retry:** Append `Please try again.` / `กรุณาลองใหม่อีกครั้ง`.

    * Keep to 1 sentence. Sentence case. No exclamation marks.

* **Pop-ups / Dialogs / Modals:**

    * **Header:** Sentence case. Provide specific context — never use generic phrases like "Unable to proceed" or "Error".

    * **Body:** Explain the consequence of the action (e.g., "By clicking 'CONFIRM', your transaction will be submitted and cannot be undone.").

    * **Buttons inside modals:** Follow primary (UPPERCASE) / secondary (Title Case) convention.

    * Use double quotes when referencing other UI elements (e.g., Please select "PROCEED").

* **Inline Errors:**

    * **Field-level:** Short label, sentence case, state what is wrong (e.g., "Incorrect PromptPay ID" / "หมายเลขพร้อมเพย์ไม่ถูกต้อง").

    * **Form-level:** Action-oriented, tell user how to fix (e.g., "Unable to proceed. Please complete all fields." / "ไม่สามารถดำเนินการต่อได้ กรุณาระบุข้อมูลให้ครบถ้วน").

    * Never blame the user. Focus on the solution.

* **Buttons / CTAs:**

    * **Primary actions:** UPPERCASE, 1-3 words, verb-first (e.g., APPLY, APPROVE, EXPORT, CANCEL).

    * **Secondary/navigation:** Title Case, 1-3 words (e.g., Next, Done, New Transfer).

    * TH buttons must start with a verb (e.g., "ยืนยัน", "อนุมัติ", "ส่งออกข้อมูล").

    * Never use lowercase for buttons.

* **Tooltips:**

    * **Action tooltips:** 1 word, sentence case (e.g., "Approve" / "อนุมัติ").

    * **Explanatory tooltips:** 1-2 sentences max (~80 characters), sentence case. Tell user what to do, not what the element is.

    * Do not repeat the label that the tooltip is attached to.

* **Empty States:**

    * **Title:** Short noun phrase, Title Case in EN, TH uses `ไม่พบ...` (e.g., "No Account Found" / "ไม่พบบัญชี").

    * **Explainer:** 1-2 sentences. Explain *why* it is empty + suggest *what to do next* (e.g., "You have no transaction history. Make your first transfer to see it here.").

    * Always include a CTA or next step — never leave the user at a dead end.

* **Placeholder Text:**

    * **Search fields:** `Search by [criteria]` / `ค้นหาโดย[criteria]` (e.g., "Search by name/account number").

    * **Select fields:** `Select [item]` / `เลือก[item]` (e.g., "Select service type").

    * **Input fields:** `Enter [item]` / `ระบุ[item]` (e.g., "Enter bank account no.").

    * Sentence case. No periods. For fields with specific formats, include an example (e.g., "e.g., 000-0-00000-0").

* **Push Notifications:**

    * **Title:** Max 50 characters, Title Case. State the event clearly.

    * **Body:** Max 100 characters, sentence case. Include an actionable next step.

    * TH: ใช้ภาษากระชับ ตรงประเด็น ไม่ต้องขึ้นต้นด้วยคำนำ.

* **Email Notifications:**

    * **Subject:** Title Case, max 60 characters. State the purpose — not "Notification from KTB".

    * **Body:** Open with context (what happened), not with greetings like "Dear Customer". End with a clear CTA.

    * Follow the same punctuation and grammar rules as other components.
 
---
 
### **5. Vocabulary & Jargon**

* **Avoid Jargon:** Use common, clear words to reduce cognitive load.

* **Explain Acronyms:** Only use acronyms (like LG or EIPP) if they are common or have been previously explained in a tutorial.

* **Pronouns:** Stick to "you" (คุณ) for the user. Never use "ท่าน". Use "they/them" as a non-binary singular pronoun if the user's gender is unknown.
 