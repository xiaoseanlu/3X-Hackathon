# TurboTax Business Tax Assistant
**Intuit × Anthropic Hackathon · May 2026 · Team Malumin**

## 🚀 <a href="https://github.intuit.com/pages/xlu02/TurboTax-Assistant/" target="_blank">Live prototype → github.intuit.com/pages/xlu02/TurboTax-Assistant</a>
*No installation. Click the link, then click the TurboTax icon in the simulated menu bar.*

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

**<a href="https://github.intuit.com/pages/xlu02/TurboTax-Assistant/" target="_blank">→ Open the live prototype</a>**

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
The widget simulates a full TurboTax Business tax assistant that lives in the macOS menu bar. It opens centered below the menu bar icon with a smooth animation, and works both as a browser prototype and as a real Electron menu bar app.

### Views and flows

**Year-round hub (`v-main`)** — the default state when no active tax season is underway. Shows business health stats pulled from QuickBooks (revenue, expenses, estimated tax, refund projection), a year-round tax calendar with upcoming deadlines, and quick-access action rows. Susan Larsen's expert footer card is pinned at the bottom for one-tap access.

**In tax season (`stage1`)** — activates when a tax season is in progress. Shows a progress stepper, business context card (Acme Design Co.), and conditional action rows that change based on workflow state: meet your expert → expert booked → join meeting → review file → filed.

**Expert matching (`v-expert-list`, `v-expert-match`)** — browse a list of matched CPAs with credentials, ratings, and specialties. Tap to view a full expert profile. Susan Larsen is the featured match (CPA, EA, ★ 4.9, 847 returns filed).

**Expert profile (`v-expert`)** — full expert view with booking CTA, availability calendar, activity timeline showing past interactions, and a "Switch Expert" option.

**Meeting booking (`v-book-meeting`)** — date/time selection with confirmation flow. Post-booking, the stage1 view updates to show Susan's status and upcoming meeting.

**Video call (`v-video-call`)** — simulated in-widget meeting experience with a 10-minute notification toast that pulses the menu bar icon.

**Document upload (`v-upload`, `v-upload-review`)** — drag-and-drop zone for tax documents (W-2, 1099, K-1, etc.). After upload, shows a categorized review screen with file details and Susan's review status.

**QuickBooks data (`v-data-in`)** — connected accounts view showing synced financial institutions (Chase, Bank of America, QuickBooks), with a detail drill-down showing recent transactions and account balances.

**Review & File (`v-review-file`, `v-filed`)** — end-to-end filing arc: summary of return, confirm and file CTA, animated success state with refund amount and confirmation ID.

**AI chat** — context-aware ask input pinned to the bottom of every view. Placeholder text adapts to the current view. Smart demo mode with pre-scripted responses (no API key needed for demos).

**Settings** — account info, notification preferences, connected accounts, demo controls for jumping to any flow state, and quit widget.

---

## Demo Flow

The fastest way to walk someone through the full experience:

1. Open the widget → **year-round hub** (QB stats, calendar, action rows)
2. Settings → Demo Controls → **"Tax Season"** → see stage1 activate
3. Tap **"Meet your expert"** → expert list → Susan's profile → book meeting
4. Demo Controls → **"Meeting Starting"** → 10-min toast fires, join meeting card appears
5. Tap **"Join meeting"** → video call experience
6. Demo Controls → **"Upload Docs"** → upload view with drag-drop
7. Demo Controls → **"Review & File"** → filing arc → filed success state

---

## Using the Widget

**Opening/closing**
- Click the TurboTax icon in the menu bar → opens widget centered below icon
- Click the × button (top right of widget) → closes widget
- Right-click the tray icon → **Quit** removes it from the menu bar entirely

**Navigation**
- Tap any action row → drills into detail view
- Back arrow (top left) → returns to previous view
- Gear icon (top right) → Settings
- Susan's footer card (bottom) → her full profile

**Keyboard shortcuts** (Electron app only)
| Shortcut | Action |
|----------|--------|
| `Cmd+R` | Reload prototype — picks up any edits instantly |
| `Cmd+Option+I` | Open DevTools |

---

## Folder Structure

```
TurboTax-Assistant/
│
├── README.md                        ← You are here
├── AI_INSTRUCTIONS.md               ← Read before starting a Claude session
├── CHANGELOG.md                     ← Full version history (v1–v13+)
├── Launch Widget.command            ← Double-click to run the menu bar app
│
├── prototype/                       ← The widget (single self-contained HTML file)
│   ├── index.html                   ← Everything: HTML + CSS + JS in one file (~3,800 lines)
│   ├── Susan.png                    ← Expert photo
│   ├── wallpaper.png                ← macOS Sonoma Blue desktop wallpaper
│   ├── menubar-icon.png             ← TurboTax menu bar icon
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
│       ├── menubar-icon.png
│       ├── menubar-icon@2x.png
│       └── app-icon-1024.png
│
└── .github/
    └── workflows/
        └── deploy.yml               ← Auto-deploys prototype/ to GitHub Pages on push to main
```

---

## Design System

All visual decisions live in a single source of truth across three files:

| File | Role |
|------|------|
| `Component Inventory.md` | Every design token, spacing rule, and component spec in plain text |
| `Component Gallery.html` | Visual reference — open in browser to see every component live |
| `prototype/index.html` | The prototype — must always match the Gallery |

**Core principles**
- **Flat Robinhood-style doctrine** — no shadows, no nested cards, no borders on gray backgrounds. Navigation uses flat action-rows. Cards are reserved for structured data display (numbers, confirmations, grids).
- **4px spacing grid** — `--s1` through `--s8` tokens only. No hardcoded pixel values.
- **Color tokens** — `var(--color-brand)`, `var(--color-success)`, `var(--color-text-primary)`, etc. No hardcoded hex.
- **Typography** — 13px body (`--text-sm`), 11px minimum. Labels use uppercase + letter-spacing.
- **Two-layer IA** — Layer 1: summary action rows on the main view. Layer 2: full detail views. Every layer-2 view ends with a path to Susan's footer card.
- **Action-row pattern** — flat rows with negative side margins, border-bottom separator, hover tint. Used for all navigation on gray backgrounds.

---

## Contributing with Claude

Every change to this project is made by talking to Claude in a Cowork session.

**Starting a session:**
Open the project folder in Cowork and say:
> *"Read AI_INSTRUCTIONS.md and let's work on [feature/fix]."*

Claude reads the instructions, loads the design system context, and picks up exactly where you left off.

**What Claude does automatically on every change:**
1. Reads the Component Gallery as visual reference before writing any code
2. Updates the Component Gallery when anything changes in the prototype
3. Runs a holistic audit — checks that nothing else in the system is now inconsistent
4. Writes a CHANGELOG entry

**To suggest a feature:** describe it in plain language. Claude will ask clarifying questions if needed, then build it following the design system.

**To make a design change:** share a screenshot and describe what feels off. Claude will diagnose, propose a fix, and implement it holistically.

---

## Sprint Plan

### ✅ Completed (v1–v13, May 12–13)
- Full end-to-end prototype: all views, all flows, complete navigation
- Year-round hub with QuickBooks stats, tax calendar, action rows
- In-tax-season flow with stepper, expert matching, booking, meeting
- Video call demo experience with 10-min notification toast
- Document upload: drag-and-drop, file categorization, review screen
- Complete filing arc: review → confirm → file → success state with refund amount
- Expert profiles: Susan Larsen, David, Maria — all with booking CTAs
- AI chat with smart demo mode (context-aware, no API key required)
- Flat Robinhood-style design system — all action rows, cards only for data
- macOS Sonoma Blue wallpaper + real TurboTax menu bar icon
- Widget centers below menu bar icon on open
- Component Gallery fully synced with prototype
- Electron menu bar app: tray icon, right-click quit, IPC bridge
- `Launch Widget.command` one-double-click setup
- GitHub Pages live at <a href="https://github.intuit.com/pages/xlu02/TurboTax-Assistant/" target="_blank">github.intuit.com/pages/xlu02/TurboTax-Assistant</a>

### 🔲 May 14 — Final Polish + Ship
- Merge Hailey's features: Decision Cards (expense anomaly detection), Tax Readiness % bar, Deductions tab, Activity timeline
- Final presentation polish pass
- Record demo video
- Hackathon submission

---

## Questions?

- **Design** → Sean Lu or Hailey (XD)
- **Product direction + submission** → Armin Naghashzadeh
- **Prototype / Electron** → Sean Lu
