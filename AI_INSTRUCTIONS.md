# AI Collaborator Instructions — TurboTax Business Tax Assistant
**Team Malumin · Intuit x Anthropic Hackathon · May 2026**
**XD: Sean Lu · Eng: Hailey**

Feed this file into your Claude at the start of any session working on this project. It tells Claude exactly how the project is structured, what rules to follow, and how Sean (XD) expects design changes to flow.

---

## What This Project Is

A macOS menu bar widget for TurboTax Business customers. It provides always-available access to:
- Year-round tax strategy (Q2 payments, tax law updates, business changes)
- A persistent CPA expert (Susan Larsen) with booking and async messaging
- Context-aware AI chat (TurboTax Assistant for general questions, Susan for expert advice)

The widget is a **single self-contained HTML file** — no build step, no dependencies, no framework. Open in a browser and it works.

---

## File Structure

```
/
├── Tax Assistant Widget Prototype.html        ← Primary deliverable (prototype, v7)
├── CHANGELOG.md                               ← Version history — update on every change
├── Susan.png                                  ← Expert photo (place alongside HTML)
└── 3X PM-XD Hackathon Resources/
    ├── Component Inventory.md                 ← SOURCE OF TRUTH for all design specs
    ├── Component Gallery.html                 ← Live visual reference for all components
    └── Tax Assistant — Product Design Requirements.md
```

---

## The Design Workflow — ALWAYS Follow This Order

Every change, no matter how small, follows these steps in order. This is Sean's workflow and is non-negotiable:

1. **Component Inventory first** — Update the spec in `Component Inventory.md` before touching any code.
2. **Component Gallery second** — Update `Component Gallery.html` to reflect the change visually.
3. **Prototype third** — Apply the change to `Tax Assistant Widget Prototype.html`.
4. **Audit for gaps** — Check if the change creates inconsistency with other components.
5. **Fix cohesion proactively** — If something breaks design system consistency, fix related components too. Don't leave the system in a state where components contradict each other.
6. **Document in CHANGELOG.md** — Log every change: what changed, why, what files were touched.

**Never** apply a change directly to the prototype without updating the Component Inventory first.

---

## Design Principles

### Flat Widget Doctrine
The widget lives on top of a macOS desktop. Inside it:
- **No card shadows** — use background tints and dividers instead
- **No nested cards** — flat list items only
- **Three surface layers:**
  - Sticky chrome (header + footer): `rgba(255,255,255,0.88)` + `backdrop-filter: blur(12px)`
  - Scroll area: `#FAFBFC` (barely-there tint)
  - Section surfaces: `#FFFFFF`
- **Dividers:** 0.5–1px at `var(--color-border)` — never decorative

### Spacing Scale (4px grid — always use tokens, never hardcode)
```
--s1: 4px  --s2: 8px  --s3: 12px  --s4: 16px
--s5: 20px --s6: 24px --s7: 28px  --s8: 32px
```

### Color Tokens (defined in prototype :root — never hardcode hex)
- Brand: `--color-brand: #1B4F8A`
- Success: `--color-success: #00875A`
- Warning: `--color-warning: #FF8B00`
- Danger: `--color-danger: #DE350B`
- Text: `--color-text-primary`, `--color-text-secondary`, `--color-text-tertiary`

### Typography
- Body: 13px (`--text-sm`), Inter, `--color-text-primary`
- Caps labels: 11px (`--text-xs`), weight 600, `letter-spacing: .06em`, uppercase
- Hero stats: 24px, weight 700 (`.ep-stat-val`)
- Never go below 11px

---

## Component Naming Prefixes

| Prefix | Component |
|--------|-----------|
| `ep-*` | ExpertProfileCard (full Susan profile view) |
| `efc-*` | ExpertFooterCard (sticky footer presence card) |
| `ar-*` | ActionRow (drill-down list items) |
| `w-*` | Widget-level layout (header, section wrappers) |
| `ad-*` | Action detail view content |
| `biz-*` | Business changes checklist |
| `chat-*` | Chat UI elements |
| `sb-*` | Status bar / menubar chrome |

---

## Multi-View Navigation

Push/pop view stack — no page reloads, no modals.

```javascript
navigate(viewId)  // pushes new view
goBack()          // pops to previous view
```

**View IDs:** `main`, `expert`, `action-q2`, `action-laws`, `action-biz`, `chat`

**Transitions:** `translateX(100%)` → `0` (in), `0` → `translateX(-28%)` (behind/parallax). Duration: `260ms cubic-bezier(0.4,0,0.2,1)`.

**Footer rules:**
- `#expertFooterCard` hides when in `expert` or `chat` views
- The bottom bar (ask input) is **always visible** — it is the single global input for the entire widget
- The async note below the input hides when in `chat` view

---

## Chat System

Two modes, one chat view (`#v-chat`). **There is only ONE input field in the entire widget** — `#askInput` in the bottom bar. The chat view has no input of its own.

| Mode | Triggered by | Avatar | Title |
|------|-------------|--------|-------|
| `ai` | Typing from main or action views | "TT" blue circle | "Ask anything" |
| `susan` | Typing from Susan's expert profile | "SL" + Susan.png | "Ask Susan" |

`chatMode` is a global JS variable (`'ai'` or `'susan'`), set in `sendAsk()` and reset on widget close.

---

## Susan Larsen — Expert Identity (Do Not Change)

| Property | Value |
|----------|-------|
| Name | Susan Larsen |
| Credentials | CPA · EA · S Corp |
| Rating | ★ 4.9 · 372 reviews |
| Experience | 19 years |
| Returns filed | 847 |
| Specializations | S Corp · Sole Prop · Small Business · California · English · Spanish |
| Availability | Available now · Mon–Fri · 9am–6pm PT |

**Avatar pattern** (layered — never use onerror JS):
```html
<div style="background:linear-gradient(135deg,#1B4F8A,#2D6BC4); position:relative; overflow:hidden;">
  <span style="position:absolute;inset:0;...;z-index:0">SL</span>
  <img src="Susan.png" style="position:absolute;inset:0;...;z-index:1">
</div>
```
Gradient + initials always render. Photo overlays at z-index:1 if file is present.

---

## Hard Constraints

- **Single HTML file** — keep everything in `Tax Assistant Widget Prototype.html`. No external JS/CSS files.
- **No npm, no bundler, no framework** — vanilla HTML/CSS/JS only.
- **Widget size** — `width: 340px`, `height: 532px`. Use explicit `height:` not just `max-height` (absolutely-positioned views don't contribute to content height).
- **No localStorage** — all state is in-memory, resets on widget close.
- **Figma CDN URLs expire** ~7 days after generation (these were fetched May 12, 2026).

---

## Do Not Change Without Checking with Sean (XD)

- Susan's identity, credentials, ratings
- The view stack navigation architecture
- The spacing token scale
- The flat widget doctrine (no shadows inside widget)
- The chatMode system (ai vs susan distinction)
- Widget width (340px) or the frosted glass chrome treatment

---

## How to Preview

Open `Tax Assistant Widget Prototype.html` in any modern browser. Place `Susan.png` in the same folder. No server needed.
