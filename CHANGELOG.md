# Tax Assistant Widget — Changelog

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
