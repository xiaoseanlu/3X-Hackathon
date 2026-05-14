# Demo Script + Elevator Pitch
**Team Malumin · TurboTax Business Tax Assistant · May 14, 2026**

> Use this file for: the 60-second submission video, the Demo & Delight shareout (May 19), and any hallway/Slack explanation of what you built.

---

## Elevator Pitch (30 seconds — for Slack messages, hallway convos, quick intros)

> TurboTax Business has always promised customers a year-round expert relationship. But every product we have only gets opened at tax time. So the relationship resets every year — same context rebuild, same scramble, same feeling that the expert is a last resort instead of a trusted advisor.
>
> We built a macOS menu bar widget that makes the expert continuously present in the customer's day. No browser, no login. Your expert, your tax situation, always one click away. It lives where you already work.

**Shorter version (one sentence):**
> A macOS menu bar widget that turns TurboTax Business from a once-a-year product into a year-round expert relationship — no browser, no login, always one click away.

---

## 60-Second Video Scripts — Three Concepts

---

### Concept A — "The Context Rebuild Problem"
*Angle: open with the pain, not the product. The strongest rubric play on Customer Problem & Impact (30%).*

**[0:00–0:12] — The problem**
> Every year, TurboTax Business customers open TurboTax in April and start from zero. They dig for documents. They brief their expert — again. They scramble on quarterly payments they missed. The relationship was supposed to be year-round. The product experience is not.

**[0:12–0:22] — The reframe**
> The issue isn't information. It's presence. The expert exists. The data exists. Neither is connected to the customer's day.

**[0:22–0:48] — The product**
> We built a macOS menu bar widget. It lives next to your clock. Always there. Click it — your tax situation, your deductions, your expert, your next action. No login. No browser. Susan, your CPA, is one tap away for a question, a meeting, or a file review.
>
> During tax season: a 5-step progress tracker shows exactly where your return stands. Your expert flags items, you approve them, you file — all from the widget.
>
> Year-round: QuickBooks data flows in automatically. Deductions are tracked. Quarterly estimates surface before the deadline, not after.

**[0:48–0:60] — The outcome**
> From a seasonal transaction to a trusted relationship. The expert your customers pay for, finally present in the moments that matter.

---

### Concept B — "One Click Away"
*Angle: product-forward, demo-driven. Best if you can do a live screen recording of the widget in action.*

**[0:00–0:08] — Hook**
> What if your tax expert lived in your menu bar?

**[0:08–0:20] — The gap**
> TurboTax Business customers have a dedicated CPA. But they only talk to them at tax time. Between January and April — missed deductions, missed quarterly payments, missed opportunities. The relationship goes dark.

**[0:20–0:48] — Live demo narration**
> This is the TurboTax Business Tax Assistant. It sits in your macOS menu bar. Click it.
>
> Here's Acme Design Co. — revenue, deductions found, estimated tax. The return is in review: three items need your sign-off. Tap one — approve it. Done.
>
> Susan, your CPA, is right here. Ask her a question. Book a call. She already has your full context — connected accounts, uploaded documents, every interaction in the timeline.
>
> When you're ready to file: one button. Federal and state, reviewed and approved, filed from the menu bar.

**[0:48–0:60] — Outcome**
> No login. No tab-switching. No context rebuild. Just the expert relationship TurboTax Business was always supposed to deliver — ambient, always-on, one click away.

---

### Concept C — "The Relationship That Doesn't Reset"
*Angle: emotional, relationship-forward. Best for Demo & Delight audience who thinks about customer trust.*

**[0:00–0:15] — The tension**
> Business owners pay for TurboTax Full Service because they want an expert relationship. What they get is an expert transaction. Every engagement starts with: "Here's my situation. Here's what changed. Here's what I need." Every year, from scratch.

**[0:15–0:30] — The insight**
> Relationships accumulate through small moments. A quick question. A flagged deduction. A deadline reminder that lands on time. We don't have a surface for those moments. Until now.

**[0:30–0:50] — The product**
> The Tax Assistant lives in the macOS menu bar — ambient, persistent, zero friction to open. Your expert sees the same data you do. Your return moves through prep, review, filing, and year-round planning in one continuous thread.
>
> Every small moment — a question answered, an item approved, a quarterly payment confirmed — builds the relationship instead of resetting it.

**[0:50–0:60] — The bet**
> We built this in two days with Claude. The prototype is live. The expert relationship your customers were promised? It looks like this.

---

## Recording Guide

**What to capture (all three required by rubric):**
1. **(a) Problem statement** — use the opening lines from whichever script you choose
2. **(b) Working product** — screen record the live prototype at `github.intuit.com/pages/xlu02/TurboTax-Assistant/`
3. **(c) From/to outcome** — seasonal transaction → year-round relationship

**Technical:**
- Record screen + voiceover with QuickTime (built into Mac). File → New Screen Recording.
- Open the prototype in Chrome full-screen before starting. Use Demo Controls to jump to the right stage.
- Keep it under 60 seconds. The rubric scores it as a criterion (20% weight) — treat it seriously.
- Upload to Google Drive, share with "Anyone at Intuit and Credit Karma."

**Recommended demo flow for screen recording:**
1. Open widget from menu bar icon
2. Show year-round hub (QB stats, deductions card, Susan footer)
3. Jump to Tax Review via stepper — show pending approvals
4. Jump to Ready to File — show hero + file CTA
5. Jump to Susan's profile — show activity timeline
6. Close with the filed confirmation screen

---

## Key Messages (for Q&A or follow-up)

**What's the core insight?**
> The year-round expert relationship TurboTax Business promises can't be delivered through a product customers open three times a year. Relationships need frequency. This gives them frequency without friction.

**What did you build with Claude?**
> A fully interactive macOS menu bar widget — single HTML file, ~5,500 lines, all CSS and JS inline. Complete tax flow from onboarding through filing. Built end-to-end in two days using Claude Cowork.

**What's the "from" state?**
> Customer opens TurboTax in April, rebuilds context with their expert, scrambles for documents, misses quarterly payments, files and forgets.

**What's the "to" state?**
> Expert is always present in the menu bar. Context is kept current automatically. The relationship accumulates through small moments year-round. Filing is the last step of a continuous process, not the whole experience.

**Why a menu bar widget?**
> Business owners work at a desktop. The menu bar is where ambient tools live — Dropbox, calendar, Slack notifications. Tax should be there too. It respects attention: invisible until it matters, one click when it does.
