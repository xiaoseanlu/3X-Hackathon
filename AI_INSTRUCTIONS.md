# AI Collaborator Instructions — TurboTax Business Tax Assistant
**Team Malumin · Intuit × Anthropic Hackathon · May 2026**
**Current prototype version: v12**

> **How to use this file:** At the start of every Claude session, say:
> *"Read AI_INSTRUCTIONS.md before we start."*
> Claude will read it automatically if it's in the project root (Cowork or Claude Code).
> This file is the single source of truth for project structure, design rules, component specs, and sprint goals. It overrides any assumptions Claude might have from prior sessions.

---

## Team & Roles

| Role | Person | Owns |
|------|--------|------|
| XD | Sean Lu | Component Inventory, Component Gallery, prototype visual design, design decisions |
| XD | Hailey | Design contributions, interaction features, prototype updates |
| PM | Armin Naghashzadeh | Product direction, sprint goals, submission |

All design changes follow the workflow in this file. Either XD can drive any part of the project.

---

## What This Project Is

A macOS menu bar widget for TurboTax Business customers. It provides always-available access to:
- Year-round tax strategy (Q2 payments, tax law updates, business changes, 2026 return drill-down)
- A persistent CPA expert (Susan Larsen) with booking scheduler and async messaging
- Context-aware AI chat (TurboTax Assistant for general, Susan for expert)
- Full tax calendar, settings, past returns

The widget is a **single self-contained HTML file** — `prototype/index.html`. No build step. No framework. No external dependencies. Open it in a browser and it works. Electron loads the same file as a real macOS menu bar app.

---

## File Structure

```
TurboTax-Assistant/
├── README.md                             ← Team onboarding guide (read this first)
├── AI_INSTRUCTIONS.md                    ← This file — load at the start of every session
├── CHANGELOG.md                          ← Every change documented: what, why, files touched
├── Launch Widget.command                 ← Double-click to start the Electron app
│
├── prototype/
│   ├── index.html                        ← THE widget — all HTML/CSS/JS in one file
│   ├── Susan.png                         ← Expert photo (place here for photo to render)
│   └── design-system/
│       ├── Component Inventory.md        ← SOURCE OF TRUTH: design tokens + component specs
│       ├── Component Gallery.html        ← Visual reference: every component rendered live
│       └── Product Design Requirements.md
│
└── electron-app/
    ├── main.js                           ← Tray icon, BrowserWindow, right-click menu, app.quit
    ├── preload.js                        ← contextBridge API — extend for Claude API, file I/O
    ├── package.json
    └── assets/
        ├── menubar-icon.png              ← 16×16 white PNG for macOS tray
        └── app-icon-1024.png
```

**Critical rule:** `prototype/index.html` is a single self-contained file. Never create external CSS or JS files. Never introduce a build step or framework.

---

## The Design Workflow — Follow This Every Time, No Exceptions

Every change, no matter how small, follows these steps in order:

1. **Read the Component Gallery first** — Before writing any code, open `Component Gallery.html` and find the relevant section. This is the visual spec. Code must match it, not the other way around.
2. **Component Inventory** — If the change introduces a new token, component, or spec change, update `Component Inventory.md` first.
3. **Prototype** — Apply the change to `prototype/index.html`.
4. **Gallery sync** — Update the corresponding Gallery section to match. This is non-negotiable (see Gallery ↔ Prototype Sync Rule below).
5. **Holistic audit** — Check the entire system for inconsistencies (see Holistic Audit Rule below).
6. **CHANGELOG** — Write a version entry documenting: what changed, why, which files were touched.

**Never apply a change directly to the prototype without checking the Gallery spec first.**

---

### Holistic Audit Rule — The Most Important Rule

**Every change triggers a full audit of the entire design system. Never change one thing and leave related things inconsistent.**

After any change, ask every question on this list before calling the task done:

- **Color changed?** → Find every place that color (or a visually similar one) appears in the system. Update for consistency.
- **Spacing/size changed?** → Find every other spacing value that's now off the 4px grid or inconsistent with the changed component.
- **Component redesigned?** → Find every component that shares the same pattern or references this one. Update them cohesively.
- **Interaction/function changed?** → Find every other interaction that now conflicts or is broken by this change. Update all callers.
- **Copy or data changed?** → Find every place that value appears (other views, Gallery, Inventory, CHANGELOG). Update everywhere.
- **IA pattern changed?** → Find every layer-2 view that follows the same structure. Apply the change universally.

**The test:** Can you say "the entire design system is coherent and non-contradictory"? If not, the task is not done.

---

### Gallery ↔ Prototype Sync Rule — Non-Negotiable

**The Component Gallery is a mirror of the prototype. They must always be identical after every session.**

- Component changes in prototype → update Gallery in the same pass
- Copy/data changes → update both files
- New view added → add matching Gallery section
- After every edit: grep key values in prototype, confirm they match Gallery

To find the Gallery section for a prototype view: search `Component Gallery.html` for the `sec-label` that matches. Example: `#v-settings` → search `Settings view`.

---

## Current Prototype State (v12)

### Views (all IDs in `viewTitles` JS object)

| View ID | Title | Layer |
|---------|-------|-------|
| `main` | *(no header title — shows brand mark)* | 1 |
| `tax-2026` | 2026 Tax Return | 2 — drill-down from 2026 Tax Year section |
| `action-q2` | Q2 Estimated Tax | 2 — from Q2 action row |
| `action-laws` | New Tax Laws | 2 — from tax laws action row |
| `action-biz` | Business Changes | 2 — from business changes row |
| `calendar` | Tax Calendar | 2 — from any cal-item in Coming Up section |
| `expert` | Susan Larsen | 2 — from Susan footer card |
| `chat` | Ask anything / Ask Susan | 2 — from ask input submit |
| `settings` | Settings | 2 — from gear icon |

### Navigation
```javascript
navigate(viewId)  // push new view onto stack
goBack()          // pop to previous view
quitWidget()      // full state reset + hide widget + hide menu bar icon
closeAll()        // hide widget only (used by click-outside handler)
toggleWidget()    // show/hide widget (menu bar icon left-click)
```

**Footer visibility rules:**
- `#expertFooterCard` hides in: `expert`, `chat`, `settings` views
- `#expertFooterCard` shows in: all other views
- The bottom bar (ask input) is **always visible** — global input for the entire widget

**Scroll fade:**
- `.views-host::after` — 48px gradient fade at bottom of scroll area
- `updateFade()` — toggles `.at-bottom` class to hide fade when view is scrolled to bottom
- Called on: `navigate()`, `goBack()`, scroll event on every `.view`, init

---

## Design Principles

### Flat Widget Doctrine
The widget lives on a macOS desktop. Inside it:
- **No card shadows** — use background tints and hairline dividers instead
- **No nested cards** — flat list items only
- **Three surface layers:**
  - Sticky chrome (header + footer): `rgba(255,255,255,0.88)` + `backdrop-filter: blur(12px)` + `border-top: 1px solid var(--color-border)` on footer
  - Scroll area: `#F4F6F9`
  - Section surfaces: `#FFFFFF`
- **Section dividers:** `border-bottom: 4px solid #fff` on `.w-sec` — creates visible white band between major sections on the gray scroll background
- **Internal dividers:** `0.5px solid var(--color-border)` between rows within a section

### Spacing Scale (4px grid — always use tokens)
```
--s1: 4px   --s2: 8px   --s3: 12px  --s4: 16px
--s5: 20px  --s6: 24px  --s7: 28px  --s8: 32px
```
Never hardcode pixel values. Every spacing decision maps to this scale.

### Color Tokens (never hardcode hex in component code)
```css
--color-brand:          #1B4F8A    /* TurboTax blue — text, links, brand elements */
--color-success:        #00875A    /* Confirmed/positive states */
--color-warning:        #FF8B00    /* Caution/pending states */
--color-danger:         #DE350B    /* Errors, overdue, quit actions */
--color-bg:             #FFFFFF
--color-border:         #E3E8EF    /* Hairline dividers */
--color-text-primary:   #0A2540
--color-text-secondary: #425466
--color-text-tertiary:  #8792A2
```

**TurboTax icon color:** `#D52B1E` (official TurboTax red). Used in the menu bar icon circle and widget header brand mark. **Not** `--color-brand` (blue).

### Typography
```
--text-xs: 11px    section labels (uppercase, weight 600, letter-spacing .06em)
--text-sm: 13px    body text, action rows, Susan CTA copy
--text-base: 14px  company name in settings
--text-md:  16px   (reserved)
--text-xl:  28px   (reserved — NOT used for hero stats)
```
- Hero stat values (ep-stat-val): 24px, weight 700
- `$4,187` tax due hero: 20px, weight 700 (`.status-hero`)
- Minimum font size: 11px. Never go below.
- Never hardcode font sizes — use the tokens.

### Hover States
- Items on gray scroll background (`#F4F6F9`) → hover to `#fff` (white lift)
- Susan footer card (frosted glass chrome) → hover to `rgba(27,79,138,.06)` (brand tint)
- `.w-sec.clickable` → hover to `#fff`
- Pattern: white lift on gray bg = clear contrast without shadows

---

## Component Naming Prefixes

| Prefix | Component |
|--------|-----------|
| `ep-*` | ExpertProfileCard (full Susan profile — `#v-expert`) |
| `efc-*` | ExpertFooterCard (sticky footer — `#expertFooterCard`) |
| `ar-*` | ActionRow (list items with chevron → drill-down) |
| `w-*` | Widget-level layout (sections, section wrappers) |
| `ad-*` | Action detail view content (layer 2 views) |
| `tx-*` | Tax return summary rows (`#v-tax-2026`) |
| `cal-*` | Calendar items (Coming Up strip on main view) |
| `s-*` | Settings (sections, rows, labels) |
| `chat-*` | Chat UI elements |
| `ep-tl-*` | Expert profile activity timeline |

---

## Key Component Specs

### IA Model (Two-Layer Architecture)
- **Layer 1 (main view):** Summary action rows only — headline + one-line sub. No detail content.
- **Layer 2 (detail views):** Full content, source links, expert context.
- **Every layer-2 view ends with:** 13px `var(--text-sm)` leading copy separated by `border-top: 1px solid var(--color-border)`. **No buttons.** Susan's sticky footer card and the ask input bar are the permanent CTAs — no redundant buttons in detail views.

### Susan CTA Pattern (`.ad-susan-cta`)
```html
<div style="margin-top:var(--s5);padding-top:var(--s4);border-top:1px solid var(--color-border)">
  <div style="font-size:var(--text-sm);color:var(--color-text-secondary);line-height:1.6">
    [Leading copy guiding user toward Susan's footer card or ask input]
  </div>
</div>
```
**Never add buttons here.** The copy is a natural nudge, not a CTA.

### ExpertFooterCard 3.9b (`.expert-footer-card`)
- 56px avatar (layered: gradient+initials z:0, photo z:1)
- Name 15px semibold, ★ 4.9 (372) · 19 yrs exp at 11px
- Green availability dot + "Available now" at 11px
- `border-top: 1px solid var(--color-border)` on `.widget-footer` — separates from scroll fade
- Hover: `rgba(27,79,138,.06)` (brand tint — NOT white, it's on frosted glass)

### ExpertProfileCard (`#v-expert`)
**`ep-hero` contains:**
1. Avatar (56px, layered photo/initials)
2. Name (`ep-name`)
3. Credentials (`ep-creds` with `ep-badge` spans)
4. `ep-hero-action` row: `ep-avail` (dot + text) + `ep-book-btn-compact` (32px, brand fill)

**After `ep-hero`:** `ep-stats` (19 yrs · 4.9/372 · 847 returns) → `ep-body` (just `ep-tags`) → `ep-activity` (timeline) → `ep-scheduler` (booking) → `ep-scheduled` (confirmation)

**Activity timeline (`ep-activity`):**
- Label: "With your business" (10px uppercase tertiary)
- Each item: `ep-tl-dot-col` (dot + line) + `ep-tl-content` (date/title/desc)
- Last item: no `ep-tl-line` (no connector below last entry)
- Dot colors: `--color-brand` = advisory/review; `--color-success` = confirmed filing/payment

**Do not add** `ep-avail`, `ep-bio`, or `ep-book-btn` (full-width) to `ep-body`. These were removed in v11.

### Settings View (`#v-settings`)
**Company Info section:**
- Company name: 14px weight 600, subtitle: 11px tertiary
- Field rows (Owner, Size, Type): `display:flex; justify-content:space-between; padding:4px 0; border-bottom:0.5px solid var(--color-border)`
- **About field:** stacked layout — `<span display:block>About</span>` label above `<span color:text-secondary>` value. NOT inline.
- Update button: `.s-edit-btn` (pencil icon + text, opens TurboTax in browser)

**Section dividers:** `border-bottom: 4px solid #fff; background: var(--color-bg)` on `.s-sec` — white band between sections

**Log out / Quit section:**
- Log out: `color:var(--color-text-secondary)` with sign-out icon
- Quit widget: `color:var(--color-danger)` with × icon, calls `quitWidget()`
- `quitWidget()` resets ALL state (view stack, chat, scheduler) then hides widget AND `#ttIcon`

### Menu Bar Icon (`#ttIcon`)
- Right-click → custom context menu: "Open widget" | separator | "Quit TurboTax widget"
- Left-click → `toggleWidget()`
- After `quitWidget()`: icon is hidden (`display:none`)
- Icon circle: `fill="#D52B1E"` (TurboTax red) — NOT `--color-brand` blue

### Cal-items (Coming Up section)
- All 4 cal-items are individually clickable → `navigate('calendar')`
- Full-bleed hover: negative margin + explicit padding pattern (same as action rows)
- No "View full tax calendar" text link — removed. The cal-items are the entry point.

---

## Susan Larsen — Expert Identity (Do Not Change)

| Property | Value |
|----------|-------|
| Name | Susan Larsen |
| Initials | SL |
| Credentials | CPA · EA · S Corp |
| Rating | ★ 4.9 · 372 reviews |
| Experience | 19 years |
| Returns filed | 847 |
| Specializations | S Corp · Sole Prop · Small Business · California · English · Spanish |
| Availability | Available now · Mon–Fri · 9am–6pm PT |

**Avatar pattern (always use layered approach — never `onerror` JS):**
```html
<div class="ep-avatar" style="background:linear-gradient(135deg,#1B4F8A,#2D6BC4);position:relative;overflow:hidden;">
  <span style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700;color:#fff;z-index:0">SL</span>
  <img src="Susan.png" alt="Susan Larsen" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:50%;z-index:1">
</div>
```
Gradient + initials always render. Photo overlays at z-index:1 when file is present.

---

## Demo Data (Do Not Change)

All persona/business data is fixed across prototype and Gallery:

| Field | Value |
|-------|-------|
| Business | Acme Design Co. |
| Entity | S Corp · California · Est. 2018 |
| Owner | Sean Lu |
| Email | xiao_lu@intuit.com |
| Plan | TurboTax Business Tax Full Service |
| Size | 1–5 employees |
| About | Brand identity, product design, and UX consulting for tech startups. |
| Total taxes due | $4,187 (2026 Tax Year) |
| 2025 return | −$4,187 Federal + CA |
| 2024 return | +$1,240 Federal + CA |
| 2023 return | −$2,950 Federal + CA |
| 2022 return | +$3,820 Federal only |

---

## Chat System

Two modes, one chat view. **One global input field** — `#askInput` in the bottom bar. No second input in the chat view.

| Mode | Trigger | Identity shown |
|------|---------|----------------|
| `ai` | Any ask from main or action views | "TT" red circle, "Ask anything" |
| `susan` | Ask from Susan's expert profile view | "SL" + Susan.png, "Ask Susan" |

`chatMode` is a global JS variable. Reset to `'ai'` on widget close and on `quitWidget()`.

---

## Electron App

`electron-app/main.js` loads `prototype/index.html` in a frameless `BrowserWindow`.

**Key behaviors:**
- Hides from Dock (`app.dock.hide()`) — menu bar only
- Left-click tray → `toggleWindow()` (show/hide)
- Right-click tray → native macOS context menu: "Open widget" + "Quit TurboTax widget" (`app.quit()`)
- Widget hides on window blur (click outside), but does **not** reset state (unlike `quitWidget`)
- `Cmd+R` in widget → `win.loadFile(PROTOTYPE_PATH)` — reload prototype instantly
- `Cmd+Option+I` → DevTools in detached window

**To add a backend feature (e.g. Claude API):**
1. Expose it in `preload.js` via `contextBridge.exposeInMainWorld('electronAPI', { yourMethod })`
2. Handle it in `main.js` via `ipcMain.handle('your-channel', ...)`
3. Call `window.electronAPI.yourMethod()` from `prototype/index.html`

---

## Hard Constraints

- **Single HTML file** — `prototype/index.html` contains all HTML, CSS, and JS. No external files.
- **No npm, no bundler, no framework** — vanilla HTML/CSS/JS only.
- **Widget dimensions** — `width: 340px`, `height: 532px` fixed. Use `height:` not just `max-height`.
- **No localStorage** — all state in-memory, resets on widget close/quit.
- **No shadows inside widget** — flat widget doctrine. Outer panel only (`--shadow-panel`).
- **No font sizes below 11px.**
- **No hardcoded hex or pixel values** — always use design tokens.

---

## Do Not Change Without Checking with Sean (XD)

- Susan's identity: name, credentials, ratings, specializations
- The view stack navigation architecture (`navigate` / `goBack`)
- The two-layer IA model (layer 1 = summary rows, layer 2 = detail + Susan CTA)
- The spacing token scale (4px grid)
- The flat widget doctrine (no shadows, no nested cards)
- The chatMode system (`ai` vs `susan` distinction)
- Widget width (340px) and the frosted glass chrome treatment
- The holistic audit and Gallery sync rules

---

## How to Preview Changes

1. Edit `prototype/index.html`
2. If widget is open in Electron: press `Cmd+R` to reload instantly
3. If in browser: `Cmd+R` or refresh to see changes
4. No server, no build step required

For Electron DevTools: `Cmd+Option+I` while widget is focused.

---

## Working with Claude (Cowork) — Required Protocol

### File writes must use Desktop Commander, not Edit/Write tools
The Cowork Edit and Write tools operate on a sandbox buffer — they do **not** write to the Mac filesystem. All changes to `prototype/index.html` must go through **Desktop Commander Python scripts**:
1. Write the script with `mcp__Desktop_Commander__write_file`
2. Run it with `mcp__Desktop_Commander__start_process` + `interact_with_process`
3. Verify with a Desktop Commander grep or line-count

### Always verify HTML structure after any insertion
After every Python script that inserts or removes HTML, run a div-balance check before committing. A single misplaced `</div>` can close the `views-host` container early, pushing all subsequent views out of their `overflow:hidden` parent into normal document flow — which manifests as a full-screen side-panel layout blowout on every screen.

Use `check2.py`-style verification (saved in the project root):
```bash
python3 check2.py  # confirms all 8 major views open and close correctly
```

### Use maximally specific anchor strings in str.replace()
The prototype has many similar comment markers. Always include enough surrounding context in anchor strings to guarantee a single match — never use a short string that could match multiple locations.

### Deploy to GitHub Pages — orphan branch method
GitHub Actions is blocked on Intuit GHE. Always deploy manually:
```bash
# 1. Commit prototype/index.html to main first (required)
git add prototype/index.html && git commit -m "..."

# 2. Create orphan branch, add prototype files, push
git checkout --orphan gh-pages-clean
git rm -rf --cached . --quiet
git add prototype/index.html prototype/Susan.png prototype/wallpaper.png prototype/menubar-icon.png prototype/intuit-assist.svg prototype/turbotax-logo.svg prototype/design-system/
git commit -m "Deploy prototype"
git push origin gh-pages-clean:gh-pages --force

# 3. Clean up (use -f, not stash — project files are untracked on orphan branch)
git checkout -f main
git branch -D gh-pages-clean
```
Live URL: https://github.intuit.com/pages/xlu02/TurboTax-Assistant/prototype/
