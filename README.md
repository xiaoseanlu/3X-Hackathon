# TurboTax Business Tax Assistant
**Intuit × Anthropic Hackathon · May 2026 · Team Malumin**

## 🚀 <a href="https://github.intuit.com/pages/xlu02/TurboTax-Assistant/prototype/" target="_blank">Live prototype → github.intuit.com/pages/xlu02/TurboTax-Assistant/prototype/</a>
*No installation. Click the link, then click the TurboTax icon in the simulated menu bar.*

![TurboTax Business Tax Assistant](sample.png)

---

A macOS menu bar widget that gives TurboTax Business customers always-on access to their tax situation — year-round strategy, a dedicated CPA expert, AI-powered chat, and a complete tax filing workflow. Right from the menu bar, without opening a browser or app.

**Team**
| Role | Person |
|------|--------|
| XD | Sean Lu |
| XD | Hailey |
| PM | Armin Naghashzadeh |

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
>
> *(Do NOT double-click the first time — right-click → Open is the key.)*

---

### Option C — Run from terminal

```bash
cd electron-app
npm install          # first time only
npm start
```

---

### Option D — Build a distributable .dmg

```bash
cd electron-app
npm run build
# Output: electron-app/dist/TurboTax Business Tax-0.1.0.dmg
```

---

## What's Built

### Core experience
A macOS menu bar widget simulating a full TurboTax Business tax assistant. Opens centered below the menu bar icon with a smooth animation. Works as both a browser prototype and a real Electron menu bar app. The widget is a single self-contained HTML file (~5,500 lines) with all CSS and JS inline.

### Views and flows

**Year-round hub (`v-main`)** — the default state between tax seasons. Shows business health stats (revenue, expenses, estimated tax, refund projection), a year-round tax calendar with upcoming deadlines, quick-access action rows for Q2 estimates, new tax laws, and business changes. Susan Larsen's expert footer card is pinned at the bottom.

**In tax season (`stage1`)** — activates during tax season. Shows a 5-step global progress stepper (Prep → Review → Ready to File → Filed → Year Round), business context card (Acme Design Co.), and conditional action rows that update based on workflow state.

**Tax Review hub (`v-tax-review`)** — review stage overview with pending approval items (income classification, equipment deduction, home office), a Financial Summary card showing deductions found with category bars, and a Recent Activity feed. Each section is clickable into its own detail view.

**Deductions detail (`v-deductions`)** — full deductions breakdown by category (Software, Equipment, Meals, Office, Travel) with individual line items and amounts.

**Activity timeline (`v-activity`)** — chronological log of all review actions, approvals, and flag resolutions.

**Tax Summary (`v-review-summary`)** — consolidated return summary with refund/balance grid, deductions list, and business financials. Accessible from review stage.

**Ready to File (`v-filing`)** — expert-approved filing screen with green checkmark hero, refund amount, forms included in the return, and a "Schedule a final review with Susan" link. File Federal & State Return CTA advances to the Filed stage.

**Filed (`v-filed`)** — success confirmation with refund tracker (Filed → Processing → Approved → Deposited), confirmation IDs, and "Continue to tax planning" CTA that returns to the year-round hub.

**Expert matching (`v-expert-list`, `v-expert-match`)** — browse matched CPAs with credentials, ratings, and specialties. Susan Larsen is the featured match (CPA, EA, ★ 4.9, 847 returns filed).

**Expert profile (`v-expert`)** — full expert view with booking CTA, availability, credential tags, and an activity timeline that grows with the relationship stage: prep shows an empty state, year-round shows full history, review adds a "tax review started" entry, filing adds "review complete", filed adds "return filed ✓".

**Meeting booking (`v-book-meeting`)** — date/time/method selection with confirmation. Post-booking updates the stage1 view to show Susan's status and meeting details.

**Video call (`v-video-call`)** — simulated in-widget meeting experience with a 10-minute notification toast that pulses the menu bar icon.

**Document upload (`v-upload`, `v-upload-review`)** — drag-and-drop zone for tax documents. After upload, shows a categorized review screen with file details and Susan's review status.

**QuickBooks data (`v-data-in`)** — connected accounts view with synced financial institutions, transaction feed, and account balances.

**AI chat** — context-aware ask input pinned to the bottom of every view. Shows a chat bubble icon on Susan's profile views, Intuit Assist icon elsewhere. Placeholder text adapts to context. Smart demo mode with pre-scripted responses.

**Settings + Demo Controls** — account info, notification preferences, connected accounts, and a full demo control panel for jumping to any stage (Prep, Review, Ready to File, Filed, Year Round) or specific view.

---

## Navigation System

The widget uses a two-function navigation model:

- **`navigate(viewId)`** — pushes a view onto the stack. Back button appears. Used for drilling into sub-flows.
- **`stepTo(viewId)`** — resets to a single-item stack. No back button. Used for top-level stage transitions (stepper clicks, CTAs that advance to a new stage).

The sticky header shows the brand name on hub/stage views and a view title on deep views. The menu bar pill updates per stage: `Tax Assistant` → `3 pending · Review` → `Ready to File` → `Filed ✓`.

Susan's sticky footer card is always visible during review and filing stages, and after expert booking.

---

## Demo Flow

The fastest walk-through of the full experience:

1. Open widget → **year-round hub** (QB stats, calendar, Susan card)
2. Demo Controls → **Tax Review Hub** → see review stage with pending items
3. Tap **Deductions** → full deductions breakdown
4. Tap back → tap **Ready to File** in stepper → review and file screen
5. Tap **File Federal & State Return** → filed success + refund tracker
6. Tap **Continue to tax planning** → back to year-round hub
7. Tap **Susan's footer card** → expert profile with full activity timeline

---

## Using the Widget

**Opening/closing**
- Click the TurboTax icon in the menu bar → opens widget
- Click the × button → closes widget
- Right-click the tray icon → **Quit** removes it from the menu bar

**Navigation**
- Tap any clickable section → drills into detail view
- Back arrow (top left) → returns to previous view (only visible in sub-flows)
- Stepper dots → jump to any stage (no back button — stage-level transition)
- Gear icon → Settings / Demo Controls
- Susan's footer card → her full profile

**Keyboard shortcuts** (Electron app only)
| Shortcut | Action |
|----------|--------|
| `Cmd+R` | Reload prototype |
| `Cmd+Option+I` | Open DevTools |

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
- **Hover system** — all clickable sections use `background: #F4F6F9` on hover via CSS class (`hub-section.clickable`, `w-sec.clickable`). No inline `onmouseover/onmouseout`
- **Typography** — 13px body (`--text-sm`), 11px minimum
- **Two-layer IA** — Layer 1: summary cards and action rows. Layer 2: full detail views

---

## Sprint Summary

### ✅ v1–v13 (May 12–13) — Foundation
- Full end-to-end prototype: all views, all flows, complete navigation
- Year-round hub, expert matching, booking, video call, document upload
- Complete filing arc, AI chat, settings, demo controls
- Electron menu bar app + GitHub Pages live deploy

### ✅ v14–v15 (May 13–14) — Tax Review Arc + Polish
- Full tax review stage: Review Hub, Deductions, Activity, Tax Summary
- 5-step global stepper across all stages
- Financial Summary component (deductions overview with bar chart)
- Ready to File screen: hero, forms list, Susan link, file CTA
- Filed screen: refund tracker with progress steps
- Expert profile activity timeline grows by stage (prep → yearround → review → filing → filed)
- Chat bubble icon in Susan's profile views
- Menu bar pill text: stage-aware copy, always white
- Header label fix: stage transitions use `stepTo()` for clean stack reset
- Removed orphaned `filing-summary` screen
- CSS hover system audit: all sections use consistent `#F4F6F9` class-based hover

### 🔲 May 14 — Final Stretch
- Merge Hailey's features: Decision Cards, Tax Readiness % bar
- Record demo video
- Hackathon submission

---

## Questions?

- **Design** → Sean Lu or Hailey (XD)
- **Product direction + submission** → Armin Naghashzadeh
- **Prototype / Electron** → Sean Lu
