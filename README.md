# TurboTax Business Tax Assistant
**Intuit × Anthropic Hackathon · May 2026 · Team Malumin**

## 🚀 <a href="https://github.intuit.com/pages/xlu02/TurboTax-Assistant/prototype/" target="_blank">Live prototype → github.intuit.com/pages/xlu02/TurboTax-Assistant/prototype/</a>
*No installation. Click the link, then click the TurboTax icon in the simulated menu bar.*

![TurboTax Business Tax Assistant](sample.png)

---

## The Problem

Small business owners who use TurboTax Business Full Service log in to TurboTax an average of **1.8 times a year.** That means for most customers, expert tax help effectively shows up for two weeks — and disappears for the other fifty.

The problem isn't that small business owners don't care about taxes. They do. It's that tax decisions don't only happen at filing time. They happen every day — through a purchase, a hire, a new expense category, a regulatory change. But expert guidance is completely disconnected from those moments.

The result is a pattern we heard over and over in customer research:

> *"I've kind of always had the feeling that, like, did we get everything? Did I give you everything? Was there anything else I could have done?"*
> — Keisha W., small business owner

> *"I had a really bad day last February. My accountant looked at me with a not-so-friendly face and asked if I had more deductions. I ended up owing more than I expected. It was a sad day."*
> — Monika, yoga instructor

> *"It feels overwhelming. It feels confusing. I never really feel like I have a good grasp on things."*
> — Jessica, health & wellness business owner

Customers pay for expert tax help. But they're only experiencing it as a stressful, once-a-year event — when it's almost too late to do anything meaningful with the advice.

---

## The Idea

What if your tax expert was actually with you all year?

Not as a portal you log into. Not as an app you have to remember to check. Just quietly present — surfacing what matters, when it matters — while you get on with running your business.

**TurboTax Business Tax Assistant** is a macOS menu bar widget that makes year-round expert tax management feel effortless. It lives in your menu bar alongside your Wi-Fi icon and battery indicator. It watches for things that need your attention. And when something comes up, it's one tap to handle it — right there, without switching context or opening a browser.

> *"If I can have somebody else there just to always make sure that I'm on top of it — help me carry that weight a little bit — that would be helpful on an ongoing basis."*
> — Tyson K., small business owner

---

## Product Design Strategy

### The menu bar as a new interaction layer
The menu bar is the one place on a Mac that's always visible, always accessible, and never requires a context switch. By living there, the TurboTax Assistant creates a new interaction layer for tax management — one that fits around the way small business owners already work, rather than asking them to adopt new habits.

### Two-layer information architecture
Every view follows a consistent two-layer model. Layer 1 surfaces a summary — the key number, the upcoming deadline, the item that needs a decision. Layer 2 provides the full context when the user wants to go deeper. This keeps the widget fast and scannable at a glance, while making full detail available in one tap.

### Every drill-down ends with a human
Every detail view — every layer-2 deep-dive into a deduction, a tax law, a calendar entry — terminates with a direct path to Susan, the customer's assigned expert. The design principle is that AI surfaces and organizes; the expert validates and advises. The widget always returns the customer to a human connection point.

### Expert presence as a constant
Susan Larsen's footer card is pinned to the bottom of every view. This is a deliberate design decision: the expert isn't buried in a settings screen or a separate tab. She's always visible, always one tap away. Her availability status updates in real time. When you open the widget, Susan is there.

### Year-round continuity
The experience is designed around the idea that tax preparation is already finished by the time filing season arrives — because the work happened continuously throughout the year. The assistant tracks decisions, categorizes expenses, flags issues early, and builds a complete picture of the business over time. By April, there's no scramble. It's already organized.

---

## What's Built

### The Widget Shell
A fully functional macOS menu bar widget built as a single self-contained HTML file (~5,500 lines of HTML, CSS, and JS). Runs as a live prototype in any browser via GitHub Pages, and as a real Electron menu bar app that installs a TurboTax icon in your actual macOS menu bar. The widget opens centered below the icon with a smooth slide animation, scroll-fades content into the expert footer, and handles push/pop navigation with parallax transitions between views.

### Year-Round Hub
The default state between tax seasons. Shows the customer's complete tax picture at a glance: business health stats (revenue, expenses, estimated tax owed, refund projection), a live view of the last filed return, and a 2027 Tax Year Strategy section with upcoming deadlines and action items. The hub is the anchor the customer returns to after handling anything — the place that makes it clear that tax work is continuous, not seasonal.

### Quick-Tap Action Cards
The year-round hub surfaces pending items that need a decision — upcoming estimated payments, new tax law alerts, business change flags — as compact action cards. Each card shows exactly what's needed: the amount, the deadline, the context. One tap dismisses it after handling. The menu bar icon badge updates in real time as items are resolved, giving a persistent signal of what's waiting without requiring the widget to be open.

### The Tax Review Arc
A complete review workflow spanning three linked views. The **Tax Review Hub** shows a high-level overview of the review stage: pending approval items (income classification, equipment deductions, home office categorization), a Financial Summary card showing total deductions found with a category breakdown, and a Recent Activity feed. Drilling into **Deductions Detail** shows a full breakdown by category — software, equipment, meals, office, travel — with individual line items and amounts. The **Activity Timeline** shows a chronological log of everything that's been reviewed, approved, or flagged across the engagement.

### The Filing Arc
When the review is complete, the **Ready to File** view shows the expert-approved filing package: a green-checkmark hero, the refund amount, every form included in the return, and a direct link to schedule a final review with Susan. Filing advances to the **Filed** view — a success confirmation with a live refund tracker (Filed → Processing → Approved → Deposited), confirmation IDs, and a "Continue to tax planning" CTA that returns to the year-round hub. The arc is designed so that filing feels like a milestone, not a scramble.

### Five-Step Global Progress Stepper
A persistent stepper spanning Prep → Review → Ready to File → Filed → Year Round appears across all active tax season views. Every dot is clickable and navigates directly to that stage — giving the customer a clear sense of where they are and what's coming next, without requiring them to find their way through menus.

### Susan Larsen — Your Dedicated Expert
Susan isn't a generic support agent. She's a CPA with 19 years of experience, 847 returns filed, and a 4.9 rating — and the prototype treats her as a real, continuous relationship. Her **expert profile** shows her full credentials and a stage-aware activity timeline that grows as the engagement deepens: a year-round check-in becomes a review session becomes a filed return becomes ongoing tax planning. The **booking sheet** lets the customer schedule a call or video chat with date and time selection. Post-booking, Susan's status updates across every view to reflect the upcoming meeting.

### Expert Matching
For customers who haven't yet been matched, the **Expert List** view lets them browse matched CPAs by specialty, rating, availability, and background. Susan's profile is the featured match, with Marcus Reid available as an alternative. Selecting a match navigates to the full expert profile.

### QuickBooks Data Sync
The **Connected Accounts** view shows every linked financial institution and app in a fully-connected state — Chase Business Checking, Mercury, Stripe, QuickBooks — with a transaction analysis feed. Tapping any institution surfaces account balances and a document list of what's been automatically pulled and categorized. This view represents the assistant's always-on data collection: it knows the business because it's been watching it all year.

### Document Upload
A **drag-and-drop upload** view for tax documents that aren't automatically synced. After upload, a categorized review screen shows the file details and Susan's review status. The upload experience is designed to feel like sending something to an expert, not filing it in a folder.

### Tax Calendar
A full-year tax calendar accessible from the year-round hub, broken into quarterly sections. Each event includes a description, date, and days-remaining countdown. Every calendar entry is also a Susan connection point — the event context travels automatically into the conversation.

### AI Chat
A context-aware ask input is pinned to the bottom of every view. The AI icon switches to Susan's photo when the customer is in her profile views, creating a natural transition between AI-assisted self-service and expert-directed guidance. Smart demo mode provides pre-scripted responses that demonstrate real tax advisory scenarios.

### Tax-2026 Drill-Down
The **2026 Tax Year** summary section is tappable and navigates to a full return breakdown: federal and state tax cards, every deduction applied (home office, mileage, health insurance, professional services, software — $19,100 total), credits applied (R&D, payroll), and a business financial summary with gross revenue, W-2 salary, and net profit. A direct link opens TurboTax for document access.

### Settings and Demo Controls
Account info, plan details, company profile (Acme Design Co., S Corp), notification preferences, and connected accounts — all editable inline. A full demo control panel allows jumping to any stage or view instantly, making the prototype easy to walk through in any order during a presentation.

---

## The Before / After

**Before:** Customers log in 1.8×/year. Expert contact is limited to filing season. Deductions are missed. Tax surprises are common. The expert rebuilds context from scratch every year. Filing is a scramble.

**After:** Tax management is built into the customer's workday. Small decisions get handled in seconds. The assigned expert builds continuous context across the year. When April arrives, the work is already done.

---

## Getting Started

### Option A — Live link (zero setup) ⭐ Fastest

**<a href="https://github.intuit.com/pages/xlu02/TurboTax-Assistant/prototype/" target="_blank">→ Open the live prototype</a>**

Click the TurboTax icon in the simulated macOS menu bar at the top of the page to open the widget. No cloning, no installs, works in any browser.

---

### Option B — Run as a real macOS menu bar app

**Prerequisite:** Node.js 18+ — [download here](https://nodejs.org) if you don't have it.

1. Clone the repo
2. Double-click **`Launch Widget.command`** in Finder

The first run installs dependencies (~30 seconds). After that it launches instantly. The TurboTax icon appears in your actual macOS menu bar.

> **⚠️ First-run security warning:** macOS will say it "cannot verify" the file. This is expected for unsigned developer tools.
>
> **To bypass it (one-time only):** Right-click `Launch Widget.command` → click **Open** → click **Open** again in the dialog. You won't see this warning again.

---

### Option C — Run from terminal

```bash
cd electron-app
npm install          # first time only
npm start
```

---

## Demo Flow

The fastest walk-through of the full experience:

1. Open widget → **year-round hub** (QB stats, 2027 strategy, Susan card)
2. Demo Controls → **Tax Review Hub** → see review stage with pending approval items
3. Tap **Deductions** → full deductions breakdown by category
4. Tap back → tap **Ready to File** in stepper → filing screen with forms list
5. Tap **File Federal & State Return** → success screen + refund tracker
6. Tap **Continue to tax planning** → back to year-round hub
7. Tap **Susan's footer card** → expert profile with full activity timeline

---

## Folder Structure

```
TurboTax-Assistant/
│
├── README.md                        ← You are here
├── AI_INSTRUCTIONS.md               ← Read before starting a Claude session
├── CHANGELOG.md                     ← Full version history
├── Launch Widget.command            ← Double-click to run the menu bar app
│
├── prototype/                       ← The widget (single self-contained HTML file)
│   ├── index.html                   ← Everything: HTML + CSS + JS (~5,500 lines)
│   ├── Susan.png                    ← Expert photo
│   ├── wallpaper.png                ← macOS Sonoma Blue desktop wallpaper
│   ├── menubar-icon.png             ← TurboTax menu bar icon
│   ├── intuit-assist.svg            ← Intuit Assist AI icon
│   ├── turbotax-logo.svg            ← TurboTax logo
│   └── design-system/
│       ├── Component Gallery.html   ← Visual reference for every component
│       ├── Component Inventory.md   ← Design token + component spec source of truth
│       └── Product Design Requirements.md
│
├── electron-app/                    ← macOS app wrapper (Electron)
│   ├── main.js                      ← Tray icon + window management
│   ├── preload.js                   ← IPC bridge
│   ├── package.json
│   └── assets/
│
└── .github/
    └── workflows/
        └── deploy.yml               ← Auto-deploys prototype/ to GitHub Pages on push to main
```

---

## Design System

| File | Role |
|------|------|
| `Component Inventory.md` | Every design token, spacing rule, and component spec |
| `Component Gallery.html` | Visual reference — open in browser to see every component live |
| `prototype/index.html` | The prototype — must always match the Gallery |

**Core principles**
- **Flat design doctrine** — no shadows on inner components, no nested cards, no borders on gray backgrounds
- **4px spacing grid** — `--s1` through `--s8` tokens only
- **Color tokens** — `var(--color-brand)`, `var(--color-success)`, etc. No hardcoded hex
- **Two-layer IA** — Layer 1: summary cards and action rows. Layer 2: full detail views, always terminating in a Susan connection point
- **Expert as constant** — Susan's footer card is pinned to every view

---

## Team

| Role | Person |
|------|--------|
| XD | Sean Lu |
| XD | Hailey |
| PM | Armin Naghashzadeh |

*Questions? Design → Sean or Hailey · Product → Armin*
