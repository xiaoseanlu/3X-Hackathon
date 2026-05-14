# TurboTax Business Tax Assistant
**Intuit × Anthropic Hackathon · May 2026 · Team Malumin**

## 🚀 [**Live prototype → pages.github.intuit.com/xlu02/TurboTax-Assistant**](https://github.intuit.com/pages/xlu02/TurboTax-Assistant/)
*No installation. Click the link, then click the TurboTax icon in the simulated menu bar.*

---

A macOS menu bar widget that gives TurboTax Business customers always-on access to their tax situation — year-round strategy, a persistent CPA expert (Susan Larsen), and AI-powered chat. Right from the menu bar, without opening a browser or app.

**Team**
| Role | Person |
|------|--------|
| XD | Sean Lu |
| XD | Hailey |
| PM | Armin Naghashzadeh |

---

## Getting Started

### Option A — Live link (zero setup) ⭐ Fastest

**[→ Open the live prototype](https://github.intuit.com/pages/xlu02/TurboTax-Assistant/)**

Auto-deploys whenever anything is pushed to `main`. No cloning, no installs.

> **To use it:** click the TurboTax icon in the simulated menu bar at the top of the page.

---

### Option B — Double-click to launch as a menu bar app

**Prerequisite:** Node.js 18+ — [download here](https://nodejs.org) if you don't have it.

1. Clone the repo
2. Double-click **`Launch Widget.command`** in Finder

That's it. The first time you run it, it installs dependencies (~30 seconds). After that it launches instantly. A TurboTax icon appears in your actual macOS menu bar.

> **⚠️ First-run security warning — you WILL see this:** macOS will show a popup saying it "cannot verify" the file. This is expected for any unsigned developer tool downloaded from the internet.
>
> **To bypass it (one-time only):**
> 1. **Right-click** `Launch Widget.command` in Finder → click **Open**
> 2. A new dialog appears with an **Open** button — click it
> 3. The widget launches. You won't see this warning again.
>
> *(Do NOT double-click the first time — that triggers the block with no bypass option. Right-click → Open is the key.)*

---

### Option C — Run from terminal (developer mode)

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

Install the `.dmg` and the app lives in your Applications folder like any macOS app.

---

## Using the Widget

### Opening and closing
- **Click** the TurboTax icon in the menu bar → opens the widget
- **Click outside** the widget → closes it (returns to main view on reopen)
- **Right-click** the icon → context menu: **Open widget** or **Quit TurboTax widget**

### Navigation
- **Tap any action row** → drills into a detail view (layer 2)
- **Back arrow** (top left) → returns to previous view
- **Gear icon** (top right) → Settings
- **Susan's footer card** → tap to open her full profile and book a meeting
- **Ask input** (bottom bar) → AI chat from any view; switches to Susan chat when on her profile

### Keyboard shortcuts (while widget is in focus)
| Shortcut | Action |
|----------|--------|
| `Cmd+R` | **Reload the prototype** — picks up any edits you made to `prototype/index.html` instantly. Use this after every change. |
| `Cmd+Option+I` | Open DevTools (inspect + debug) |

### Quitting
- Settings → **Quit widget** → removes the icon from the menu bar entirely
- Right-click the icon → **Quit TurboTax widget** → same result
- To reopen after quitting: run `Launch Widget.command` again (or `npm start`)

---

## Folder Structure

```
TurboTax-Assistant/
│
├── README.md                        ← You are here
├── AI_INSTRUCTIONS.md               ← Read this before starting a Claude session
├── CHANGELOG.md                     ← Full version history (v1–v12+)
├── Launch Widget.command            ← Double-click to run the menu bar app
│
├── prototype/                       ← The widget (single self-contained HTML file)
│   ├── index.html                   ← Everything: HTML + CSS + JS in one file
│   ├── Susan.png                    ← Expert photo (place here for photo to appear)
│   └── design-system/
│       ├── Component Gallery.html   ← Visual reference for every component ← READ THIS
│       ├── Component Inventory.md   ← Design token + spec source of truth
│       └── Product Design Requirements.md
│
└── electron-app/                    ← macOS app wrapper (Electron)
    ├── main.js                      ← Tray icon + window management
    ├── preload.js                   ← API bridge (extend for Claude API calls)
    ├── package.json
    └── assets/
        ├── menubar-icon.png         ← Menu bar tray icon
        └── app-icon-1024.png        ← App icon
```

---

## Contributing with Claude

Every change to this project is made by talking to Claude in a Cowork session. Claude reads `AI_INSTRUCTIONS.md` at the start of each session to understand the project, the design system, and the rules it must follow.

### Starting a session

Open the project folder in Cowork, then say something like:

> *"Read AI_INSTRUCTIONS.md and let's work on [feature/fix]."*

Claude will read the instructions and pick up exactly where you left off.

### What Claude does automatically

Claude follows the **design workflow** on every change without being asked:

1. Reads the Component Gallery as the visual reference before writing any code
2. Updates the Component Gallery when anything changes in the prototype
3. Runs a **holistic audit** after every change — checks that nothing else in the system is now inconsistent
4. Writes a CHANGELOG entry for every version

You don't need to remind Claude of these rules every session — `AI_INSTRUCTIONS.md` covers them. But if something seems off, you can always say *"do a holistic audit"* and Claude will sweep the entire system.

### Suggesting new features

Just describe what you want in plain language. Examples:

> *"Add a document upload zone to the main view where I can drop a PDF"*
> *"The Q2 action row should show a progress bar when the payment is pending"*
> *"Change Susan's availability to show a calendar week view instead of a date strip"*

Claude will ask clarifying questions if needed, then build it following the design system — using the right tokens, matching the existing patterns, updating the Gallery, and logging the change.

### Making design changes

When reviewing a view or component, take a screenshot and share it:

> *"Here's a screenshot of the expert view. The booking scheduler feels too cramped — can we give it more breathing room and make the confirm button more prominent?"*

Claude will diagnose the issue, propose a fix, and implement it holistically.

### After making changes

After Claude makes a change, hit `Cmd+R` in the widget to reload and see your update immediately. No restart needed.

---

## The Design System

This project has a **single source of truth** for every visual decision. Before touching anything, understand the three layers:

| File | Role |
|------|------|
| `Component Inventory.md` | Defines every design token (colors, spacing, typography, radius) and component spec in text |
| `Component Gallery.html` | The visual reference — open this in a browser to see every component rendered exactly as it appears in the widget |
| `prototype/index.html` | The working prototype — must always match the Gallery |

**The Gallery and prototype are mirrors of each other.** If they disagree, the Gallery is the intended design and the prototype needs updating. Claude enforces this automatically.

### Design principles in brief

- **Flat widget doctrine:** No shadows inside the widget. No nested cards. Use background tints and hairline dividers instead.
- **4px spacing grid:** Always use `--s1` through `--s8` tokens. Never hardcode pixel values.
- **Color tokens:** Always use `var(--color-brand)`, `var(--color-text-primary)`, etc. Never hardcode hex.
- **Typography:** Body text is 13px (`--text-sm`). Minimum 11px. Labels use uppercase + letter-spacing.
- **Two-layer IA:** Layer 1 = summary action rows on the main view. Layer 2 = full detail views. Every layer-2 view ends with copy that leads to Susan's footer card.

---

## Sprint Plan

### ✅ Done (v1–v12)
- Full widget prototype: multi-view navigation, all layer-2 views, Susan expert profile, booking scheduler, AI/Susan chat, 10-min meeting notification toast
- Year-round calendar, tax law detail cards, 2026 tax return drill-down, settings view
- Flat design system: tokens, Component Inventory, Component Gallery (fully synced)
- Electron menu bar app with right-click quit, reload shortcut, click-outside dismiss
- Launch script (`Launch Widget.command`) for one-double-click setup

### 🔲 Day 2 (May 13) — Intelligence
- **Real Claude API chat:** replace hardcoded AI responses with live `fetch()` calls to Anthropic API
- **Document parsing:** drop a PDF → Claude parses → returns structured tax summary → "Pending Susan's review" state
- **Expert review workflow:** Susan reviews → customer approves flow
- **Wire `preload.js`** for Claude API calls when running in Electron

### 🔲 May 14 — Polish + Ship
- Bug fixes and presentation polish
- Build `.dmg` for arm64 (Apple Silicon) + x64 (Intel)
- Record demo video
- Hackathon submission

---

## Questions?

- **Design questions** → Sean or Hailey (both XD)
- **Electron / API / engineering** → Sean or Hailey
- **Product direction + submission** → Armin
