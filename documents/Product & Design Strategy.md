# TurboTax Business Tax Assistant — Product & Design Strategy
**Team Malumin · Intuit × Anthropic Hackathon · May 2026**

---

## The Problem We're Solving

TurboTax Business has staked its future on a promise: year-round, expert-centered service for small business owners. The problem is that no current product can actually deliver it.

The products customers use today — TurboTax, QuickBooks — are opened three times a year at most. Relationships don't accumulate that way. Trust doesn't either. What TurboTax Business is selling as a year-round relationship is being experienced by customers as a seasonal transaction. They log in when they have to, hand off their documents, and disappear again. Their CPA goes dark between seasons. Neither side builds the context or continuity that makes the relationship actually valuable.

**The result:** small business owners feel anxious about their taxes, not confident. They don't know if they're making the right calls year-round — whether that $500 dinner is deductible, whether they're setting aside enough for Q2, whether the new tax law affects them. By the time they finally open TurboTax, it's April and the best moves are already behind them.

The deeper problem — and this is Armin's framing, which the whole team aligned around — is structural: **the relationship requires frequent small moments, and our surfaces can't host them.** No product at Intuit currently lives where the customer works.

---

## Customer Problems & How We're Addressing Them

These five problems — and the design responses to them — are the core of the project. They came out of the team's pre-hackathon alignment work and are the lens through which every feature decision was made.

---

**Presence**

*Customer problem.* Between filings, I have no sense that anyone is actually working on my tax situation. I pay for year-round expert service but I only hear from my expert when I reach out or when a deadline forces it. The rest of the time, it feels like I'm on my own.

*How might we.* Make the expert continuously visible in the customer's workspace, so the relationship feels active even when nothing is happening.

*What we built.* Susan Larsen's card lives in the widget's sticky footer across every view. After the customer books their first meeting, Susan's name, availability, and upcoming meeting are always one glance away — not buried in a product they have to log into. The widget lives in the macOS menu bar, in the same row as Slack and calendar. Susan is present even when the customer isn't thinking about taxes.

---

**Frequency**

*Customer problem.* When something comes up, I have to decide whether it's worth bothering my expert about. Most of the time I decide it isn't, and then I forget. By the time we talk, the small things have piled up and we have to work through them all at once, or we just miss them.

*How might we.* Create small moments between the expert and the customer often enough that trust and context accumulate, without overwhelming either side.

*What we built.* The widget surfaces lightweight touch points — a notification badge, a quick document upload, an "Ask Susan" input — that lower the cost of reaching out to near zero. Customers don't need to compose a message and wait for a reply. They can drop a W-2, tap a question, or approve a Q2 payment in under 30 seconds. Each small interaction keeps the thread alive between the big ones.

---

**Reachability**

*Customer problem.* Reaching my expert means logging in, finding the right place, writing a message, and then waiting. The cost of asking is high enough that I save up my questions, which means I'm making decisions without input from the person who's supposed to help me make them.

*How might we.* Make the expert reachable from inside the customer's day, so a question or decision doesn't require the customer to stop what they're doing.

*What we built.* The widget requires no login after the initial setup. It lives in the menu bar and opens in one click. The "Ask Susan" input is visible from every view — type a question without navigating anywhere. For anything requiring a real conversation, joining Susan's video call is a single tap from the home screen the moment she's ready.

---

**Proactivity**

*Customer problem.* I make decisions that affect my taxes all the time — a purchase, a hire, a distribution — without realizing they affect my taxes. By the time my expert sees the consequences, the decision is already made and we're just cleaning up.

*How might we.* Surface tax-relevant moments to the customer as they happen in their work, so decisions are made with the expert's input instead of regret.

*What we built.* The widget's main view surfaces year-round events as they become relevant: Q2 estimated tax due, new tax laws affecting S Corps, business changes that need categorization. These aren't reports — they're actionable cards that appear at the moment of relevance, with a direct path to Susan or an approval flow. The widget monitors the customer's connected accounts (QuickBooks, bank) and flags anything that matters before it becomes a problem.

---

**Trust**

*Customer problem.* Every time I do reach out, I have to re-explain my business, my year, what's changed. My expert is starting from scratch each time, which makes me feel like a ticket rather than a client. So I hesitate to reach out, which makes the next conversation start from even further behind.

*How might we.* Eliminate the context-rebuild cost on both sides, so the customer doesn't hesitate to reach out and the expert can be useful the moment they engage.

*What we built.* Susan's profile in the widget shows her full history with Acme Design Co.: every review, filing, payment, and planning session going back years. When the customer uploads documents or connects accounts, that context is available to Susan before the meeting starts. The video call begins with Susan already reviewing their 2025 return — not with "so, remind me, what kind of business do you run?" The widget holds the relationship's memory so neither side has to.

---

## The Strategy: Ambient Presence

The insight driving this project came from a design conversation on May 11:

> *"The solution isn't more presence, it's smarter presence. Persistent but invisible — running in the background, surfacing only when something actually matters. Event-driven, not weekly-cadence."* — Haley

The Tax Assistant Widget is a macOS menu bar app. It lives in the top-right corner of the customer's screen — the same real estate as Slack, Dropbox, and their calendar. It's always there. It doesn't require a login, a new tab, or a context switch. A customer working on their invoice in QuickBooks can glance up, see a notification badge, click, and handle a tax decision in 15 seconds without ever opening a browser.

This is not a mini version of TurboTax. It's a different kind of surface entirely: **ambient, glanceable, expert-anchored.** The product doesn't ask customers to do tax prep. It asks them to make small decisions at the moment they arise, with their expert already in the loop.

---

## Why Expert-Anchored?

The team debated two directions: product-anchored (a lightweight action tool surfacing automated insights) vs. expert-anchored (a persistent CPA relationship manager). We landed on expert-anchored, and the logic matters.

The small business market has a confidence gap. These are owners who know their product deeply and their taxes shallowly. They aren't looking for better software — they're looking for someone they can trust to handle this. That's what TurboTax Business is selling with its expert offering. But the product doesn't hold the relationship between sessions. The widget does.

When Susan Larsen — your CPA — is visibly present in your menu bar, the nature of the relationship changes. You don't feel like a customer using a tax tool. You feel like someone who has a tax person. That's a felt shift, not just a feature difference. It's the difference between anxiety and confidence.

Susan is the product's north star. Every design decision flows from that:

- The first thing the widget does after login is get you matched with Susan and schedule your first call.
- Your home screen shows Susan's status, your upcoming meeting, and what she's currently working on for you.
- After uploading documents, you're waiting for Susan to review them — not for a processing queue.
- The meeting notification doesn't say "your appointment is starting." It says "Susan is ready."
- Even the ask input is context-aware: it becomes "Ask Susan" when you're inside her profile.

The product doesn't just *connect* you to an expert. It makes the expert the felt center of the experience at every step.

---

## What the Widget Is Good At

This is a scoped surface. Being clear about what it handles — and what it doesn't — is what makes it good.

**What it does well:**
- Glanceable awareness: books, payroll, tax status, business health at a glance
- Lightweight approvals: "Approve Q2 estimated payment" or "categorize this expense"
- Async messaging with Susan, synced with her full inbox
- Document uploads — drop a W-2 without opening TurboTax
- Time-sensitive events: estimated payments, filing deadlines, meetings starting
- Triggering deeper work in the web product when the task requires more real estate

**What it deliberately doesn't try to do:**
- Full tax preparation (the web product handles that)
- Deep financial dashboards (QuickBooks already does this better)
- Replace the expert — the widget exists to serve the relationship, not substitute for it

---

## The Customer Journey We're Prototyping

The prototype demonstrates a complete in-season arc for a first-year TurboTax Business customer — specifically an S Corp owner on their first full year with the product:

**1. Onboarding** — Welcome + login, widget explains what it does in plain language.

**2. Expert matching** — Customer is shown Susan Larsen, matched to their business type (S Corp) and location (California). They can browse other CPAs, but Susan is the top pick. First-time intro view sets expectations for the relationship before they commit.

**3. Book first meeting** — Customer picks a date and time for their first conversation with Susan. On confirmation, Susan's status card appears in the widget's sticky footer — persistent across every view.

**4. Data collection** — Connect financial accounts (QuickBooks, bank), upload tax forms (W-2, 1099-NEC, K-1). Documents are smart-categorized on upload. Progress tracked with a stepper.

**5. Expert review** — Susan reviews the uploaded documents. The widget shows the customer what's in review and what's been analyzed. A meeting notification fires when Susan is ready.

**6. Video call with Susan** — Customer joins directly from the widget. Susan walks through the return, explains deductions, answers questions live, and uses screen share to review documents together.

**7. Ready to file** — After the meeting, the stepper advances. Customer confirms and moves to filing. The widget reflects a new state: "Expert review complete · Ready to file."

This arc compresses what is typically a multi-week, multi-product, multi-login experience into a single coherent interface that fits in a 340 × 532px window.

---

## Design Principles

**Flat and dense, not light and airy.** The widget serves a professional context. Small business owners are busy; they don't need white space and hero illustrations. They need information density and clear hierarchy. Every pixel earns its place.

**Progressive disclosure over feature listing.** The widget's home screen shows almost nothing when the customer first logs in. As they complete each stage — booking an expert, uploading documents, completing a meeting — new cards and paths appear. The complexity reveals itself only as it becomes relevant.

**State over settings.** Nothing in the widget asks customers to configure it. Everything adapts to where they are in their journey. The stepper advances automatically. The susan footer card appears after booking. The "Join Meeting" card appears when Susan is ready. The product reflects the customer's actual state, not an abstract feature menu.

**Context-aware AI, not generic AI.** The ask input knows what view the customer is on. On Susan's profile it becomes "Ask Susan." In the main view it's "Ask anything." The AI responds as TurboTax Assistant by default, but defers to Susan's actual knowledge when she's the context. The product doesn't pretend the AI and the expert are the same thing.

**The expert is always reachable.** Susan's footer card is persistent across every view except the ones where you're already on her profile. No matter where you navigate, you're one tap away from your CPA. That's the felt promise of year-round service: she's always there.

---

## The Bigger Bet

This project is a proof of concept for something larger: the idea that TurboTax Business can maintain a felt relationship with its customers year-round without requiring customers to change their behavior.

Customers won't change how they work. They won't remember to open TurboTax in July. But they will notice a notification badge in their menu bar when they're already at their computer. They will tap a "Join meeting" card when their CPA is ready. They will upload a W-2 by dropping it into a widget they can see right now, instead of logging into a portal they'll get to later.

The widget doesn't change the customer's workflow. It inserts itself into the gaps between everything else they're doing — which is exactly where a year-round relationship needs to live.

---

*Team Malumin: Sean Lu (XD) · Armin Naghashzadeh (PM) · Haley Malucchi (XD)*
*Built during the Intuit × Anthropic Hackathon, May 12–14, 2026*
