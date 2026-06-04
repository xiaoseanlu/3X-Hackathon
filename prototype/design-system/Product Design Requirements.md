# Tax Assistant — Product Design Requirements

**Team Malumin · TurboTax Business · Hackathon 2026 · v1.1 · May 11, 2026**

> Covers: product concept, design principles, interaction model, build approach, and quality bar.
> Purpose: align the team before coding starts. Everything here should be agreed on before a line is written.

---

## 1. Product Overview

Tax Assistant is a macOS-style desktop widget for self-employed business owners and S Corp operators who use TurboTax Business with an expert. It lives in the status bar and creates a continuous, ambient presence for the TurboTax experience year-round — eliminating the seasonal, episodic relationship customers currently have with both their taxes and their expert.

The product has two phases:

- **Phase 1 — Data In:** Guided onboarding to connect financial accounts and collect documents, with immediate expert matching. Think Dropbox for your tax documents.
- **Phase 2 — Year Round:** Ambient monitoring, proactive notifications, and always-on access to the expert throughout the year.

### Name Candidates

The working name "Tax Assistant" is a placeholder. Top candidates for final naming:

| Name | Rationale |
|:-----|:----------|
| **Retainer** | Business owners already pay lawyers and accountants on retainer. Names exactly what this product is: your expert, always on call. |
| **Basis** | Every S Corp owner knows this word — it's the most consequential concept in their tax life. Double meaning: the foundation of the expert relationship. |
| **Thread** | The continuous, unbroken connection between customer and expert. Never resets. |
| **Evergreen** | Year-round, never seasonal — the direct antithesis of the problem being solved. |
| **Groundwork** | The prep work happening in the background all year so filing season isn't a scramble. |

**Recommendation:** Retainer or Basis. Decide before recording the demo video.

---

## 2. Problem Statement

> *"The year-round, expert-centered relationship TurboTax Business has committed to cannot be delivered through products customers open three times a year. Relationships accumulate through frequent small moments, and our current surfaces structurally cannot host them. The result is a year-round contract the customer experiences as a seasonal transaction."*
> — Armin, #malumin

### The Context Rebuild Problem (Sean's addition)

On top of presence and frequency, there is a second structural failure: **every time a customer reaches out to their expert, both sides rebuild context from scratch.** "Here's where things are. Here's what changed since we last spoke." That friction makes customers hesitant to reach out at all, and it makes the expert less useful than they could be. The widget solves this by keeping context current automatically — connected accounts, uploaded documents, flagged items — so every interaction starts from a shared foundation rather than zero.

### Specific Pain Points

- Business owners have no continuous visibility into their tax situation. Problems accumulate silently until filing season.
- Expert relationships go dark between engagements. Reaching your expert requires stopping what you're doing and logging in.
- Data collection is point-in-time and friction-heavy. Customers scramble for documents at filing because nothing guided them to collect throughout the year.
- Quarterly tax obligations (estimated payments, form changes, new laws) surface too late to act on.
- The customer-expert relationship never deepens because there are no small moments between the big ones.

---

## 3. Target Customer

**Primary:** Self-employed business owners and S Corp operators filing TurboTax Business with an expert.

Key characteristics:

- Works primarily at a desktop — not a mobile-first workflow
- Business financials spread across multiple institutions, Google Drive, email, and paper
- Files once a year and regularly misses or scrambles on quarterly estimated tax deadlines
- Values expert guidance but finds the current engagement model episodic and passive
- Familiar with ambient desktop tools: Dropbox, calendar widgets, notification centers
- Thinks in terms of quarterly payments, deductions, entity structure, and keeping the books clean

---

## 4. Strategic Framing (HMWs)

Synthesized from Armin's May 11 post and team discussion:

- **Presence.** How might we make the expert continuously visible in the customer's workspace, so the relationship feels active even when nothing is happening?
- **Frequency.** How might we create small moments between the expert and the customer often enough that trust and context accumulate, without overwhelming either side?
- **Reachability.** How might we make the expert reachable from inside the customer's day, so a question or decision doesn't require the customer to stop what they're doing?
- **Proactivity.** How might we surface tax-relevant moments to the customer as they happen in their work, so decisions are made with the expert's input instead of regret?
- **Trust.** How might we build a trusted relationship between the customer and their expert by eliminating the cost of context? *(Added by Sean — the widget keeps both sides current automatically so every touchpoint starts from shared understanding, not zero.)*

*Note: Suite Cohesion (Armin's original 5th HMW) was pulled out by team consensus — it's a separate workstream.*

---

## 5. Product Structure

### Phase 1: Data In (Onboarding)

The Dropbox analogy: the widget appears in the macOS status bar and guides the customer through setup without requiring them to open a browser or log into TurboTax directly.

**Financial Institution Linking**
- Connect banks, investment accounts, credit cards directly from the status bar panel
- Connection flow similar to Plaid / QB Bank Feed — no browser redirect
- Connection status visible at a glance; unconnected accounts appear as recommended actions

**Document Collection**
- Drag and drop tax documents (W-2s, 1099s, K-1s) from Finder directly into the widget
- Google Drive integration: accept documents without manual download/re-upload
- Each document acknowledged and categorized on receipt
- Missing documents flagged by type: *"We expect a 1099-DIV from Vanguard. Have you received it?"*

**Expert Matching**
- Once initial data is connected, widget offers to match customer with a business tax expert
- Match based on industry, entity type (S Corp, LLC, etc.), and state
- Expert introduced with a brief profile; customer can message immediately or schedule a call
- This is the key differentiator: expert feels available from minute one, not as a last resort

---

### Phase 2: Year Round (Ongoing)

Once data is in and the expert relationship is established, the widget shifts to ambient mode. Runs in the background, surfaces only when something actually matters.

**Expert Access**

Customers reach their expert directly from the widget:
- Async text chat (synced with TurboTax in-product messaging)
- Phone call
- Live text chat
- Video call with screen share

Customer chooses the channel. Expert responses appear in the same thread. Lightweight actions (confirm a categorization, approve a deduction) can be handled with a single tap — no login required.

**Status and Progress**
- Widget header always shows current return status across all applicable returns (Business S Corp, Personal 1040)
- Progress indicator: Preparing → Expert Review → Ready to File → Filed
- Overview metrics: deductions found, estimated liability, next action

**Proactive Notifications**

The widget surfaces only what actually matters, event-driven (not on a weekly schedule per Haley's direction):
- Quarterly estimated tax reminders with calculated amount and due date
- New tax law changes relevant to the customer's business structure or industry
- New forms expected (K-1 not yet received, etc.)
- Bookkeeping alerts: flagged transactions, potential deductions based on spending
- Expert-triggered items: actions the expert has flagged for the customer to confirm
- When and how to schedule the next expert check-in, based on the filing calendar

**Deep-Link Navigation**
- Any action requiring more space deep-links to the exact location in the TurboTax web experience
- No extra navigation or login prompt — customer lands exactly where they need to be
- Widget reflects updated state when customer returns

---

## 6. Design Principles

**Smarter presence, not more presence** *(Haley)*
The widget earns its place by surfacing only when it matters. Event-driven behavior — not a weekly digest, not a scheduled push. Persistent but invisible until something requires attention.

**Gateway, not destination**
This is a hub that sends customers somewhere, not a place to stay. Awareness and lightweight decisions happen here. Heavy lifting happens in the web experience. Every action either resolves immediately or hands off cleanly with a deep link.

**Expert always reachable**
Ask AI and Connect with Expert are co-equal, level-1 calls to action. Neither is buried. The customer always sees both paths and chooses based on urgency. This is the visual and interaction centerpiece of the widget.

**Context travels automatically**
Connected accounts and uploaded documents keep the expert's picture current without the customer manually briefing them. Every interaction starts from shared understanding. This is what turns a seasonal transaction into a trusted relationship.

**Ambient, not intrusive**
Notification badge only for time-sensitive items. Panel opens on demand. No persistent window. No dock presence. The widget respects the customer's attention.

---

## 7. Interaction Model

### Status Bar Icon
- Small branded icon in the macOS menu bar (always present after onboarding)
- Badge states:
  - No badge → up to date
  - Numbered badge → items need attention
  - Pulsing dot → expert has sent a message
- Click to open the widget panel

### Widget Panel
- Compact floating panel, ~320px wide, ~480px tall
- Sections: return progress stepper, financial summary, action items list, quick answer prompts
- Bottom bar: "Ask" text input + "Connect with Expert" button — always visible, always accessible
- Three tabs: Overview, Deductions, Activity

### Action Items
- Scannable list: each item has one clear CTA (Connect, Upload, Confirm, Review)
- Items that need more space show a deep-link arrow → opens web experience to exact destination
- Max 5 items visible at once; rest accessible via scroll

### Expert Connection Sheet
- Tap "Connect with Expert" → contact sheet expands inline: Chat, Call, Video
- Session starts directly — no redirect, no separate login
- Chat history persists in widget and syncs with TurboTax web

### Data Visualization
- Key financial metrics shown as glanceable numbers + supporting visual (progress bar, simple chart)
- Quarterly estimated tax: shown as a countdown + amount due
- Deductions found: cumulative total with a simple bar showing category breakdown
- Return progress: horizontal stepper (not a percentage) — customers understand stages, not percentages

---

## 8. Build Approach

### Method
Built in **Claude Code** — not a Figma-to-code conversion. The team will co-build the experience directly in Claude, using natural language to direct component creation, layout, and interactions. Figma mockups (Haley's) serve as visual reference, not as the source for generated code.

### Stack
| Layer | Choice | Rationale |
|:------|:-------|:----------|
| Framework | React | Component-based, fast iteration, broad library support |
| Styling | Tailwind CSS | Utility-first, consistent spacing/color system, no custom CSS overhead |
| Components | shadcn/ui | Pre-built accessible components (dropdowns, sheets, tabs, badges) — use as-is, customize minimally |
| Charts / Data Viz | Recharts | React-native, composable, good defaults for financial data |
| Icons | Lucide React | Consistent, clean, matches the minimal aesthetic |
| Hosting | GitHub Pages | Free, fast to deploy, shareable link for demo and submission |

### Component Reuse Strategy
- Start with shadcn/ui primitives for all structural UI (panels, sheets, tabs, badges, buttons)
- Customize only at the visual/brand layer (colors, typography, radius)
- Do not build from scratch what already exists in the library
- If a component doesn't exist in shadcn/ui, check Recharts (for viz) or Lucide (for icons) before building custom

### What We're Building (Scope for 2 Days)
- [ ] Status bar icon simulation (floating trigger button in corner of browser window)
- [ ] Widget panel with Overview tab (fully built)
- [ ] Phase 1: Data In flow — account connection + document upload (2–3 screens)
- [ ] Phase 2: Year Round state — notifications, action items, expert access (widget populated with sample data)
- [ ] Expert connection sheet (Chat / Call / Video options)
- [ ] At least one data visualization (deductions summary or quarterly estimate)
- [ ] Deep-link simulation (button that "opens" a full-screen web experience view)

### What We Are Not Building
- Real bank connection (simulate with mock data)
- Real expert chat backend (simulate with pre-scripted responses)
- Native macOS app (browser-based widget simulation only)
- Mobile version (show as a static mockup slide only)

---

## 9. Quality Bar

The target is **Stripe / Robinhood** level of polish — not because we need enterprise-grade code, but because the demo experience needs to feel real and considered, not like a hackathon prototype.

### What That Means in Practice

**Typography**
- One typeface, two weights. Use Inter or system-ui. No decorative fonts.
- Clear hierarchy: metric values large and bold, labels small and light
- Stripe uses ~14–16px body with generous line-height. Match that rhythm.

**Color**
- Minimal palette: one brand color (TurboTax blue #1B4F8A), one accent (green for positive states), neutral grays for everything else
- Never use color as decoration — only to signal state (green = connected/healthy, amber = attention needed, red = action required)
- Robinhood reference: dark background with high-contrast white text and a single green accent for positive financial movement

**Spacing and Layout**
- Use Tailwind's 4px spacing scale consistently. No arbitrary pixel values.
- Every element should have breathing room. Dense UIs feel unfinished.
- Widget panel: 16px internal padding, 12px between sections, 8px between list items

**Motion**
- Subtle, purposeful transitions only: panel open/close (150ms ease), badge pop (scale from 0.8), notification slide-in (from top, 200ms)
- No looping animations. No decorative motion.
- Stripe reference: fast, confident transitions that don't draw attention to themselves

**Data Visualization**
- Numbers should be the hero, not the chart. Show the chart to give context to the number.
- Robinhood reference: the stock value is front and center; the sparkline is supporting context
- Use Recharts `ResponsiveContainer` for all charts — never fixed pixel widths
- Keep chart tooltips clean: one value, no borders, light background

**States**
- Every interactive element needs: default, hover, active, disabled states
- Every data view needs: loading state (skeleton), empty state (instructional, not just blank), error state (recoverable, with a clear action)
- Skeletons over spinners wherever possible

**Accessibility**
- All interactive elements keyboard-accessible
- Color is never the only signal (always paired with icon or text label)
- Minimum touch target 44x44px

---

## 10. Open Questions

| # | Question | Owner | Status |
|:--|:---------|:------|:-------|
| 1 | Final product name — Retainer, Basis, or other? | All | Decide May 12 AM |
| 2 | One demo or two submissions (Data In / Year Round split)? | All | Decide May 12 AM |
| 3 | Mock data set — who creates the sample customer profile and transaction data for the demo? | Armin | Before coding starts |
| 4 | How do we simulate expert messaging in the demo? Pre-scripted responses or live input? | Sean | Before Phase 2 build |
| 5 | Do we show QB data connections (books, payroll) or bank-only for the prototype? | Armin | May 12 |
| 6 | 3rd-party CPA platform disruption (Haley's push) — future-state slide or cut? | Haley | May 13 |
| 7 | GitHub repo — who sets it up and owns the Pages deploy? | Armin | May 12 AM |

---

## 11. Out of Scope

- Native macOS or iOS/Android app
- Real financial institution API connections
- Real expert routing or messaging backend
- Full TurboTax interview or tax completion flow inside the widget
- Windows support
- Expert-facing interface

---

## 12. Next Steps

| Action | Owner | When |
|:-------|:------|:-----|
| Agree on product name | All | May 12 AM |
| Agree on one-demo vs. two-submission structure | All | May 12 AM |
| Set up GitHub repo + Pages | Armin | May 12 AM |
| Create mock customer profile + sample data | Armin | May 12, before noon |
| Update Figma to reflect Phase 1 onboarding flow | Haley | May 12 |
| Start Claude Code build — widget shell + Overview tab | Sean + Armin | May 12 AM |
| Phase 1 (Data In) flow complete | Sean + Haley | May 12 EOD |
| Phase 2 (Year Round) state complete | Sean + Armin | May 13 noon |
| Demo video recorded (3 min max, customer problem first) | All | May 14 AM |
| Submit via submission form | Armin | May 14, by 4:00 PM PDT |
