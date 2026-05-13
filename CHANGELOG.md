# Tax Assistant Widget — Changelog

---

## [v12] — May 12, 2026 · Icon color, settings layout, quit/right-click menu

### Prototype — TurboTax icon color (both locations)
- **Menu bar icon + widget header icon**: Both `<circle fill="#1B4F8A">` → `fill="#D52B1E"`. Correct TurboTax brand red, matching the Gallery `sb-icon` spec set in v8. Was previously the brand blue in both the simulated macOS tray icon (`#ttIcon`) and the widget header brand mark.

### Prototype — Settings Company Info layout
- **`About` row**: Changed from inline `acct-row` (label left, multiline value right — caused dense wrapping) to stacked block layout: `<span display:block>About</span>` label above `<span color:text-secondary>` value. Matches Gallery spec exactly.
- **Field row dividers**: Added `border-bottom:0.5px solid var(--color-border)` to Owner, Size, Type, and About rows in the Company Info section. Previously rows had no separators (only padding). Now matches Gallery pattern.

### Prototype — Quit widget (icon removal)
- **`quitWidget()` now hides `#ttIcon`**: Added `icon.style.display = 'none'` — the menu bar icon disappears entirely when quitting, simulating real Electron `app.quit()` behavior (tray icon removed from menu bar).

### Prototype — Right-click context menu on menu bar icon
- **IIFE wires up `contextmenu` event on `#ttIcon`**: Prevents default browser context menu. Shows a custom macOS-style dropdown: "Open widget" (brand blue hover) + separator + "Quit TurboTax widget" (danger red hover).
- **"Open widget"**: Restores `#ttIcon` visibility (in case it was hidden), then calls `toggleWidget()` if widget is closed.
- **"Quit TurboTax widget"**: Calls `quitWidget()` — full state reset + hide icon.
- Menu dismisses on any outside click.

### Electron — Right-click tray menu (`electron-app/main.js`)
- **Added `Menu` to Electron imports**.
- **`tray.on('right-click', ...)` handler**: Calls `tray.popUpContextMenu(contextMenu)` with a native macOS tray menu: "Open widget" (shows and focuses the BrowserWindow) + separator + "Quit TurboTax widget" (Cmd+Q accelerator, calls `app.quit()` — removes tray icon and terminates the process entirely).

### Files touched
- `prototype/index.html` (icon color ×2, settings About layout, field borders, quitWidget, right-click context menu)
- `electron-app/main.js` (Menu import, right-click tray menu with app.quit)
- `CHANGELOG.md` (this entry)

---

## [v11] — May 12, 2026 · Expert view redesign + quit widget fix

### Prototype — Expert profile view (#v-expert)

- **`ep-hero-action` row added inside `ep-hero`**: Available now indicator + "Book a Meeting" compact button now appear immediately in the first screen region, before stats or tags. User sees a clear engagement path before scrolling. New elements: `.ep-hero-action` (flex row, border-top separator), `.ep-book-btn-compact` (32px height, brand fill, `#susanBookBtn` id).
- **`ep-bio` removed**: The static paragraph biography is gone. Trust is now carried by stats (19 yrs / 4.9 / 847 returns) + tags + the timeline below.
- **`ep-avail` row removed from `ep-body`**: Availability moved up into `ep-hero-action`. `ep-body` now contains only `ep-tags`.
- **Old `ep-book-btn` (full-width) removed**: Replaced by `ep-book-btn-compact` inside the hero action row.
- **Activity timeline added** (`.ep-activity`): Vertical list of 5 dated entries showing Susan's real work history with Acme Design Co. Pattern: dot column (`.ep-tl-dot-col` > `.ep-tl-dot` + `.ep-tl-line`) + content column (`.ep-tl-date`, `.ep-tl-title`, `.ep-tl-desc`). Last item omits `.ep-tl-line`. Brand dot = advisory/review action; success dot = confirmed filing or payment.
  - May 12, 2026 · Reviewed Q1 books (missed home office deduction)
  - Apr 13, 2026 · 2025 return accepted by IRS (Federal + CA)
  - Mar 15, 2026 · Q1 estimated payment confirmed ($3,840 Federal · $960 CA)
  - Feb 3, 2026 · S Corp salary structure reviewed (60/40 safe harbor)
  - Jan 8, 2026 · Year-end planning session ($4,320 additional deductions found)

### Prototype — Quit widget fix

- **`quitWidget()` function added**: Replaces `closeAll()` as the handler for the "Quit widget" settings button. Performs full state reset before closing: resets all `.view` classes back to clean (only `v-main` gets `v-active`), resets `viewStack = ['main']`, calls `updateHeader()`, restores `expertFooterCard` to visible, resets chat mode to AI, clears chat messages, resets booking scheduler open/close state. Then calls `closeAll()`.
- **Root cause of prior bug**: `closeAll()` only hid the widget and removed the `.active` class from the TT icon, but left `viewStack` as `['main', 'settings']` and `v-settings` as the active view. On re-open via the icon, the widget appeared in the settings view in an unexpected state — appearing as if "nothing happened."
- **Settings button updated**: `onclick="closeAll()"` → `onclick="quitWidget()"`.

### Gallery — Expert profile sync

- **Susan Larsen card (Available)**: `ep-avail` + `ep-bio` + `ep-book-btn` removed from `ep-body`. `ep-hero-action` (avail + `ep-book-btn-compact`) added inside `ep-hero`. Activity timeline (`ep-activity` + 5 `.ep-tl-item` entries) added between `ep-body` and `ep-scheduler`. Matches prototype `#v-expert` exactly.
- **Marcus Reid card (Busy)**: Same structural update — `ep-avail` + `ep-bio` + `ep-book-btn` removed from `ep-body`. `ep-hero-action` (warning avail + `ep-book-btn-compact`) added inside `ep-hero`. No timeline (secondary expert, no established business history). `ep-body` contains tags only.
- Both profiles now demonstrate the `ep-hero-action` pattern in two availability states: `success` (Available now) and `warning` (Responds within 2 hours).

### Files touched
- `prototype/index.html` (expert view restructure, quitWidget function, button handler)
- `prototype/design-system/Component Gallery.html` (Susan + Marcus ep-hero-action, activity timeline)
- `CHANGELOG.md` (this entry)

---

## [v10] — May 12, 2026 · Polish pass + 2026 drill-down + settings fixes

### Prototype — Scroll fade
- **Fade hides at scroll bottom**: `updateFade()` function added. Adds `.at-bottom` class to `.views-host` when active view is scrolled to within 4px of bottom. `.views-host.at-bottom::after { opacity: 0 }` with 200ms transition. Scroll listeners wired to all `.view` elements. Called on init + in `navigate()` + in `goBack()`. View scroll position also reset to 0 on `navigate()`.

### Prototype — Coming Up calendar strip
- **`cal-link` removed**: "View full tax calendar" text link gone. Each of the 4 `cal-item` entries now has `onclick="navigate('calendar')"` — clicking any item navigates to the full calendar layer 2 view.
- **Cal-item hover**: `.cal-item` now has `cursor:pointer`, hover `background: #fff`, and uses negative margin / explicit padding to create a full-bleed hover area matching action rows.

### Prototype — Section dividers
- **`.w-sec { border-bottom: 4px solid #fff; }`**: White band between the 2026 Tax Year section and 2027 Strategy section, and between Strategy and Coming Up. Creates visible major-section separation on the gray scroll background.
- **`.s-sec { border-bottom: 4px solid #fff; background: var(--color-bg); }`**: Same pattern applied to Settings sections. Removed inner `overflow-y: auto; height: 100%` from `.s-body` — parent `.view` handles scrolling.

### Prototype — Hover consistency (holistic audit)
- **`.action-row:hover`**: `#F6F8FA` → `#fff`. Items on gray background now hover to white — clear contrast, consistent with flat widget doctrine.
- **`.cal-item:hover`**: New — `background: #fff`, same white-lift pattern.
- **`.expert-footer-card:hover`**: `#F6F8FA` → `rgba(27,79,138,.06)`. Brand-tinted hover on frosted glass chrome — clearly distinguishable from scroll area.

### Prototype — Susan CTA copy (detail views)
- **Buttons removed** from all 4 detail views (`v-action-q2`, `v-action-laws`, `v-action-biz`, `v-calendar`). Susan's sticky footer card + global ask bar are the actual CTAs; button rows were redundant.
- **Copy remains** as leading text. `.ad-susan-label` bumped from 11px to 13px (`--text-sm`). `.ad-susan-cta` container simplified: no background or branded box — just a `border-top: 1px solid var(--color-border)` separator with padding.

### Prototype — 2026 Tax Year drill-down
- **`$4,187` hero reduced**: `.status-hero` `font-size` from `var(--text-xl)` (28px) → 20px.
- **Section clickable**: 2026 Tax Year `w-sec` gets `class="w-sec clickable"` + `onclick="navigate('tax-2026')"`. Badge row now has inline chevron. "Access tax documents" status-link removed from main view.
- **New `#v-tax-2026` view** (layer 2): Shows Federal/CA/Total tax cards at top. Deductions applied (home office, mileage, health ins, professional services, software — total −$19,100). Credits applied (R&D, payroll). Business summary (gross revenue, W-2 salary, distributions, net profit Schedule E). Access Tax Documents button → `window.open('https://myturbotax.intuit.com','_blank')`. `'tax-2026': '2026 Tax Return'` added to `viewTitles`.

### Prototype — Settings
- **"Update company info →" text link → icon button**: Replaced with `.s-edit-btn` (pencil icon + "Update company info" label), `onclick="window.open('https://myturbotax.intuit.com','_blank')"`. Consistent with flat design — no full-text external link.
- **Log out + Quit widget**: New section at bottom of settings. Log out row (sign-out icon, secondary text color), Quit widget row (X icon, danger color, calls `closeAll()`).

### Gallery — Sync
- Settings section: "Update company info →" → pencil icon button with "Opens TurboTax login in browser" annotation. Log out + Quit section added below Notifications. Multi-view nav spec updated (view IDs list now includes `tax-2026`).

### Files touched
- `prototype/index.html` (all above changes)
- `prototype/design-system/Component Gallery.html` (settings section sync)
- `CHANGELOG.md` (this entry)

---

## [v9] — May 12, 2026 · IA restructure, full tax calendar, Susan CTA pattern, flat scroll area

### Prototype — Information Architecture restructure
- **Tax law cards removed from layer 1**: The `law-section` block (two law cards surfaced directly on `#v-main`) has been removed. Law cards now live exclusively in layer 2 (`#v-action-laws`), accessed via the "3 new tax laws may affect you" action row. Main view shows only the action row summary.
- **New `#v-calendar` view** (layer 2): "View full tax calendar" chevron link now calls `navigate('calendar')`. The new view shows the full year broken into Q2/Q3/Q4 sections, each event with dot indicator, title, date, description, and days remaining. Added `calendar: 'Tax Calendar'` to the `viewTitles` JS object.
- **Susan CTA pattern** (`.ad-susan-cta`): All three detail views now end with a consistent "Connect with Susan" (primary, navigates to `expert`) + "Ask AI" (secondary, navigates to `chat`) CTA block:
  - `#v-action-q2` — added Susan CTA after payment detail
  - `#v-action-laws` — redesigned with `law-detail-card` blocks (tag, title, Susan-reviewed badge, body, IRS source link) + Susan CTA
  - `#v-action-biz` — updated subtitle, added Susan CTA
  - `#v-calendar` — new view, Susan CTA at bottom
- **New CSS classes**: `.ad-susan-cta`, `.ad-susan-label`, `.ad-susan-btn`, `.ad-susan-btn-alt`, `.law-detail-card`, `.law-detail-tag`, `.law-detail-title`, `.law-detail-badge`, `.law-detail-body`, `.law-detail-source`, `.cal-full-section`, `.cal-full-label`, `.cal-full-item`, `.cal-full-dot-col`, `.cal-full-dot`, `.cal-full-content`, `.cal-full-title`, `.cal-full-date`, `.cal-full-desc`, `.cal-full-days`

### Prototype — Scroll area (`.views-host`)
- **Removed**: `margin: 4px 6px` and `border-radius: 10px` — scroll area is now flat, full-width, no card shell
- **Added `::after` fade**: 48px bottom gradient `rgba(244,246,249,0) → #F4F6F9`, `pointer-events: none`, `z-index: 3` — content dissolves visually into the expert footer rather than cutting off at a hard edge

### Gallery — Sync
- **Year-round calendar section**: Updated to two-column layout showing Layer 1 (4-event coming-up strip) and Layer 2 (full calendar by quarter with Susan CTA). "View full tax calendar" uses chevron icon, navigates to `v-calendar`.
- **Tax law section**: Renamed to "Tax law detail cards — layer 2". Redesigned with `law-detail-card` blocks showing IRS source links, expert-reviewed badge, and Susan CTA. IA rule documented: law cards in layer 2 only.
- **Multi-view navigation section**: Added all 8 view IDs (`main`, `expert`, `chat`, `settings`, `action-q2`, `action-laws`, `action-biz`, `calendar`). Added Susan CTA rule ("every layer-2 detail view ends with the Susan CTA block"). Added scroll area rules (flat `.views-host`, `::after` fade).

### Design system — IA model documented
Layer 1 = summary action rows (headline + sub only). Layer 2 = full detail + source links + Susan CTA. Every drill-down terminates with a human expert connection moment. This model is now documented in `AI_INSTRUCTIONS.md` and reflected in the Component Gallery.

### Files touched
- `prototype/index.html` (IA restructure, new view, Susan CTAs, scroll area)
- `prototype/design-system/Component Gallery.html` (calendar section, tax law section, multi-view nav spec)
- `CHANGELOG.md` (this entry)

---

## [v8] — May 12, 2026 · Icon system, Expert Booking Sheet, Settings view, Gallery sync

### Icon System — Lucide (prototype + Gallery)
- **Settings gear icon**: Replaced hand-drawn path with Lucide `settings` icon (viewBox 0 0 24 24). Applies to `#gearBtn` in `prototype/index.html` and the icon system section in `Component Gallery.html`. All icons now sourced from Lucide (MIT) for visual consistency.

### Gallery — Status Bar Icon
- **TurboTax icon color**: `.sb-icon svg { color: }` `#1B4F8A` → `#D52B1E` (official TurboTax red). Pulse dot in "Expert message" state likewise `#D52B1E`. Menu bar template icon (white) unchanged.

### Gallery — Expert Booking Sheet (replaces Expert Connection Sheet)
- **Section renamed**: "Expert connection sheet — context travels automatically" → "Expert booking sheet — Book a Meeting opens a layer with Call or Video options"
- **Old design removed**: Three-column Chat/Call/Video channel picker with a single Start Chat CTA.
- **New design**: "Book a Meeting" button expands a layer inline. Layer shows:
  1. Availability row — green dot + "Available now · Mon–Fri · 9am–6pm PT"
  2. Two-column type picker: **Schedule a Call** (Lucide phone icon) | **Schedule a Video Chat** (Lucide video icon)
  3. After type selected: date strip → time slots → confirm button
- Two Gallery states shown: closed (default) and open (call selected, date/time visible).
- New CSS: `.bl-body`, `.bl-avail`, `.bl-avail-dot`, `.bl-type-grid`, `.bl-type`, `.bl-type.sel`, `.bl-type-icon`, `.bl-type-label`
- New JS: `toggleBookingGallery()`, `selBlType()`

### Prototype — Settings View
- **Business section → Company Info**: Added Owner, Size, Business Type, About description, "Update company info →" link. Name changed from "Acme Design Co." placeholder with just entity type to full structured company block.
- **Account section**: Name `Sean Xiao` → `Sean Lu`; Plan `TT Live Full Service` → `TurboTax Business Tax Full Service`

### Files touched
- `prototype/index.html` (settings view, gear icon)
- `prototype/design-system/Component Gallery.html` (sb-icon color, gear icon, Expert Booking Sheet CSS+HTML+JS)

---

## [v7] — May 12, 2026 · Design system sync + YearRoundCalendar + TaxLawUpdate + NotificationBanner

### Gallery — Design system token sync (v3.3 → v4.0)
- Root CSS tokens aligned with Component Inventory source of truth: `--text-primary` `#0D1117` → `#0A2540`, `--text-secondary` `#4B5563` → `#425466`, `--text-tertiary` `#9CA3AF` → `#8792A2`, `--border` `rgba(0,0,0,.08)` → `#E3E8EF`, `--border-strong` `rgba(0,0,0,.14)` → `#C1C9D2`, `--bg-surface` `#F9FAFB` → `#F6F8FA`
- Expert names: All "Kelly Larsen" / "Kelly" / "KL" references → "Susan Larsen" / "Susan" / "SL"
- Action row padding/gap: `14px 16px / 14px` → `12px 16px / 12px`
- Chevron stroke-width: `1.3` → `1.4` (ar-chev, efc-chev)
- Susan review count: 312 → 372; tags: "Sole Proprietor, Real Estate, California, Crypto" → "Sole Prop, Small Business, California, English, Spanish"
- ep-avail: Added `margin-top: 12px`
- Mini-widget section: marked deprecated (`opacity:.45;pointer-events:none`)
- Added Chat View section (AI mode + Susan mode examples, arrow-right send button)

### Prototype — New main-view components
- **YearRoundCalendarCard** (§3.14): 4-event coming-up timeline with dot-connector pattern. Events: Q2 Tax (35d/warning), K-1 Vanguard (50d/tertiary), Expert check-in (82d/brand), Q3+S Corp (127d/danger).
- **TaxLawUpdateCard** (§3.15): Two law cards with left warning border, expert-reviewed badge, law action links.
- **NotificationBanner** (§3.10): Event-driven, slide-in animation, dismissible, warning variant. Hidden by default.
- All three components: CSS added before `/* ── Expert Profile Card */`, HTML added to `#v-main` after action rows.

### Prototype — ep-avatar fixes
- Size: `72px` → `56px`; background: gray tint → `linear-gradient(135deg,#1B4F8A,#2D6BC4)`; text: `#1B4F8A` → `#fff`
- `ep-avatar-dot` CSS and HTML removed (availability shown via `.ep-avail` row only)
- Dead `.channel-card` CSS block removed

---

## [v6] — May 12, 2026 · ExpertFooterCard 3.9b + Expert Profile Refinements

### ExpertFooterCard: 3.9a → 3.9b

**Motivation:** The 52px compact footer strip gave no trust signal before the user tapped through. Replacing with a richer card mirrors the TurboTax Live reference and makes Susan's presence feel more substantial from the first glance.

**Changes:**
- Height: `52px` fixed → auto via `padding: 12px 16px` (~80px rendered)
- Avatar: `36px` → `56px` circle; layered pattern (gradient+initials z:0, photo z:1)
- Status dot: `9px` → `11px`, border `1.5px` → `2px`
- Added `.efc-stats` row: ★ gold + `4.9 (372)` + `·` separator + `19 yrs exp` at 11px
- Added `.efc-avail` row: 6px green dot + "Available now" at 11px success color
- Name: `13px` → `15px`, same semibold weight

### Expert Profile View (#v-expert) — Susan Larsen

**Stat grid consistency**
- `4.9` rating value: inline `font-size: 13px` → `.ep-stat-val` class (`24px`) — now matches "19" and "847" flanking columns

**Specialization badges updated**
- Removed: Mandarin
- Added: Sole Prop, English, Spanish
- Full set: S Corp · Sole Prop · Small Business · California · English · Spanish

**Available now — padding**
- Added `margin-top: var(--s3)` (12px) above `.ep-avail` row for breathing room above the availability indicator

**Channel cards removed**
- Removed: Message (redundant — ask input handles async), Call, Video, "Connect with Susan" section header
- Kept: Book a Meeting (sole scheduling CTA, no duplication)

### Bottom Bar

**Ask input**
- Placeholder: "Ask anything…" → "Ask Susan…" (both main ask input and chat view input)
- Added `.ask-async-note` below input row: "Async · Susan responds in ~2 hrs" in 10px tertiary text
- Bottom bar restructured to flex-column with `.bottom-bar-row` wrapping the input + send button

### Main View (#v-main)

- Removed "Your Expert" scroll section (`.expert-snap` + `es-*` block) — Susan's presence is now exclusively in the sticky ExpertFooterCard 3.9b

### Spacing System

- Extended `--s` scale: added `--s6: 24px`, `--s7: 28px`, `--s8: 32px` to `:root`
- Full scale: `--s1: 4px` · `--s2: 8px` · `--s3: 12px` · `--s4: 16px` · `--s5: 20px` · `--s6: 24px` · `--s7: 28px` · `--s8: 32px`

### Component Gallery

- Updated to v3.3 (from v3.2)
- ExpertFooterCard spec updated from 3.9a to 3.9b in both CSS and HTML demo instances
- Placeholder text updated to "Ask anything…" → "Ask Susan…"
- Spec notes updated to reflect new avatar sizing, layered pattern, and visibility rules

### Component Inventory

- ExpertFooterCard bumped from 3.9a to 3.9b spec

---

## [v5] — May 12, 2026 · Chat UI + Height Fix + Susan Avatar

- Widget height: `max-height` only → `height: 760px` + `max-height: calc(100vh - 80px)` fix
- Susan avatar: onerror JS pattern → layered z-index (gradient+initials behind, photo on top)
- "Ask a tax question" → "Ask anything" with full chat UI (back-and-forth, typing indicator, context-aware AI responses)

## [v4] — May 12, 2026 · Multi-view navigation + interaction patterns

- Multi-view slide nav: push/pop with parallax behind (-28% translateX)
- Notification badge with glow pulse animation
- Action rows with full-row hover pattern
- ExpertProfileCard synced with Component Gallery ep-* system

## [v3] — May 12, 2026 · Component Gallery v3 + design system sync

## [v1–v2] — May 12, 2026 · Initial prototype + flat widget design system
