# TurboTax Business Tax Assistant
**Intuit x Anthropic Hackathon · May 2026 · Team Malumin**

A macOS menu bar widget for TurboTax Business customers. Always-on access to tax strategy, a persistent CPA expert, document parsing, and AI-powered chat — right from your menu bar.

**Team**
| Role | Person |
|------|--------|
| XD (Design) | Sean Lu |
| Eng | Hailey |

---

## Quick Start

### Option A — Browser preview (fastest, no install)
```bash
git clone https://github.intuit.com/xlu02/TurboTax-Assistant.git
cd TurboTax-Assistant
open prototype/index.html
```
That's it. The widget opens in your browser. Place `prototype/Susan.png` (already included) in the same folder for the expert photo.

---

### Option B — macOS menu bar app (Electron)
**Prerequisites:** Node.js 18+ ([download](https://nodejs.org))

```bash
git clone https://github.intuit.com/xlu02/TurboTax-Assistant.git
cd TurboTax-Assistant/electron-app
npm install
npm start
```

A TurboTax icon appears in your menu bar. Click it to open the widget. Press `Cmd+Option+I` to open DevTools.

**To build a distributable `.dmg`:**
```bash
npm run build
# Output: electron-app/dist/TurboTax Business Tax-0.1.0.dmg
```

> **Icon note:** Place a 16×16 white PNG at `electron-app/assets/menubar-icon.png` before building. See `electron-app/assets/ICON_INSTRUCTIONS.txt` for details.

---

## Folder Structure

```
TurboTax-Assistant/
│
├── README.md                        ← You are here
├── AI_INSTRUCTIONS.md               ← Feed to Claude before any session
├── CHANGELOG.md                     ← Full version history
├── .gitignore
│
├── prototype/                       ← Self-contained HTML widget
│   ├── index.html                   ← Main prototype (open in browser or Electron)
│   ├── Susan.png                    ← Expert photo
│   └── design-system/               ← Design reference (read before changing anything)
│       ├── Component Gallery.html   ← Live visual reference for all components
│       ├── Component Inventory.md   ← Source of truth for design tokens + specs
│       └── Product Design Requirements.md
│
└── electron-app/                    ← macOS app wrapper
    ├── main.js                      ← Electron main process (tray + window)
    ├── preload.js                   ← API bridge (extend for Claude API, file parsing)
    ├── package.json                 ← Dependencies + build config
    └── assets/
        ├── menubar-icon.png         ← Tray icon (add yours here)
        └── app-icon.icns            ← App icon for .dmg (add yours here)
```

---

## 2-Day Sprint Plan (May 12–14)

### Day 1 (May 12) — Foundation ✅ + Electron setup
- [x] Prototype v7 — multi-view nav, Susan expert card, context-aware chat, booking, notification toast
- [x] Electron scaffold — menu bar app wrapper
- [ ] Demo financial data — QBO-style P&L and cash flow summary
- [ ] Drag and drop document upload UI

### Day 2 (May 13) — Intelligence
- [ ] Real Claude API for chat (swap hardcoded responses for actual AI)
- [ ] Document parsing — drop a PDF/image, Claude parses and returns a tax summary
- [ ] Expert review workflow — "Pending Susan's review" → reviewed → customer approves
- [ ] Wire `preload.js` API bridge for Claude calls from Electron

### May 14 — Polish + Ship
- [ ] Buffer, bug fixes
- [ ] Package `.dmg` for both arm64 (Apple Silicon) and x64 (Intel)
- [ ] Demo video recording
- [ ] Hackathon submission

---

## Design Workflow (for both contributors)

Every change follows this order — no exceptions:

1. **Component Inventory** (`prototype/design-system/Component Inventory.md`) — update spec first
2. **Component Gallery** (`prototype/design-system/Component Gallery.html`) — update visual reference
3. **Prototype** (`prototype/index.html`) — apply the change
4. **Audit** — check for design system inconsistencies
5. **Fix cohesion** — update any related components that are now inconsistent
6. **CHANGELOG.md** — document what changed and why

Read `AI_INSTRUCTIONS.md` for the full rules before starting any Claude session.

---

## Contributing

1. Pull latest: `git pull origin main`
2. Work on your changes
3. Follow the design workflow above
4. Commit with a descriptive message
5. Push and open a PR: `git push origin your-branch-name`

For questions on design decisions, ping Sean (XD). For Electron/API questions, ping Hailey.
