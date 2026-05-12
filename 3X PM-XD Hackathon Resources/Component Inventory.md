# Component Inventory — Tax Assistant Widget
**Team Malumin · Build Reference · v2.3 · May 12, 2026**

> This document is the single source of truth for the widget's design system and component architecture.
> Open this alongside your code. Every decision here has a rationale tied to Stripe, Atlassian, Robinhood, or Apple HIG.

---

## 1. Design Tokens

Set these as CSS custom properties at the root of the project. Reference them everywhere — never hardcode a color, spacing value, or shadow directly.

```css
:root {
  /* ─── Brand Colors ─── */
  --color-brand:          #1B4F8A;   /* TurboTax blue — primary actions, links, brand presence */
  --color-brand-hover:    #154073;   /* Deepened 10% — button hover state */
  --color-brand-subtle:   #EBF2FA;   /* Tinted background — selected states, info banners */

  /* ─── Semantic Status Colors ─── */
  --color-success:        #00875A;   /* Green — connected, healthy, positive financial movement */
  --color-success-subtle: #E3FCEF;
  --color-warning:        #FF8B00;   /* Amber — attention needed, approaching deadline */
  --color-warning-subtle: #FFF4E5;
  --color-danger:         #DE350B;   /* Red — action required, error, overdue */
  --color-danger-subtle:  #FFEBE6;

  /* ─── Neutral Scale (Stripe-inspired) ─── */
  --color-bg:             #FFFFFF;
  --color-bg-subtle:      #F6F8FA;   /* Panel background, row hover */
  --color-bg-elevated:    #FFFFFF;   /* Cards, sheets */
  --color-border:         #E3E8EF;   /* 1px borders, dividers */
  --color-border-strong:  #C1C9D2;   /* Emphasized borders, active tab underlines */

  /* ─── Text Scale ─── */
  --color-text-primary:   #0A2540;   /* Stripe navy — headings, primary labels, metric values */
  --color-text-secondary: #425466;   /* Secondary labels, descriptions */
  --color-text-tertiary:  #8792A2;   /* Captions, timestamps, placeholders */
  --color-text-inverse:   #FFFFFF;

  /* ─── Typography ─── */
  --font-family:    'Inter', system-ui, -apple-system, sans-serif;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;

  /* Type scale — Stripe rhythm: 14–16px body, generous line-height */
  --text-xs:    11px;  /* Captions, timestamps — Apple HIG small */
  --text-sm:    13px;  /* Secondary labels — Apple HIG body */
  --text-base:  14px;  /* Primary body — Stripe standard */
  --text-md:    16px;  /* Section headers, card titles */
  --text-lg:    20px;  /* Metric values (supporting) */
  --text-xl:    28px;  /* Hero metric — Robinhood number-as-hero */
  --text-2xl:   36px;  /* Primary KPI when space allows */

  --line-height-tight:  1.2;   /* Headings, metric values */
  --line-height-normal: 1.5;   /* Body text — Stripe default */
  --line-height-loose:  1.75;  /* Helper text, captions */

  /* ─── Spacing (4px base grid — Tailwind scale) ─── */
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;   /* Widget internal padding */
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;

  /* ─── Border Radius ─── */
  --radius-sm:   4px;   /* Tags, badges */
  --radius-md:   6px;   /* Buttons, inputs — Stripe default */
  --radius-lg:   8px;   /* Cards, action item rows */
  --radius-xl:   12px;  /* Widget panel — Apple popover feel */
  --radius-full: 9999px; /* Pills, avatar, status dot */

  /* ─── Elevation / Shadows ─── */
  --shadow-sm:  0 1px 2px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.10);  /* Cards */
  --shadow-md:  0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06);  /* Floating panel */
  --shadow-lg:  0 10px 15px rgba(0,0,0,0.10), 0 4px 6px rgba(0,0,0,0.05); /* Modal sheets */
  --shadow-panel: 0 8px 30px rgba(0,0,0,0.12), 0 2px 8px rgba(0,0,0,0.08); /* Widget panel — macOS popover */

  /* ─── Motion ─── */
  --duration-fast:   100ms;
  --duration-base:   150ms;  /* Panel open/close — Stripe: fast, confident */
  --duration-slow:   200ms;  /* Sheet expand, notification slide */
  --duration-xslow:  300ms;  /* Complex layout transitions */
  --ease-default:    cubic-bezier(0.4, 0, 0.2, 1);   /* Standard — smooth decel */
  --ease-spring:     cubic-bezier(0.34, 1.56, 0.64, 1); /* Badge pop, success states */
  --ease-in-out:     cubic-bezier(0.4, 0, 0.6, 1);
}
```

### Widget Flat Layout Doctrine
**Reference: Robinhood app — single surface, space as structure**

> All components rendered *inside* the widget panel follow flat layout rules. This overrides any component-level shadow or background-elevation defaults when in widget context.

```
Rules:
  1. ONE background color: --color-bg (#FFFFFF) for the entire widget panel interior.
     No --color-bg-subtle, --color-bg-elevated, or --color-bg-card inside the panel.

  2. Sections are separated by dividers only:
     border-bottom: 1px solid var(--color-border)
     Use padding (--space-4 = 16px top/bottom) to breathe — not background changes.

  3. No box-shadow on inner components.
     --shadow-sm, --shadow-md are NOT used inside the widget panel.
     The only shadow is --shadow-panel on the widget panel itself (the outer popover).

  4. Color signals information, not depth.
     --color-success, --color-warning, --color-danger are for status only.
     --color-brand is for primary actions and links only.
     No tinted backgrounds except semantic subtle variants (--color-warning-subtle, etc.)
     used in context-specific banners (NotificationBanner, QuarterlyCountdown when urgent).

  5. Layout hierarchy is established by:
     - Typography weight + size (--text-xl hero → --text-sm label)
     - Whitespace (generous padding between sections)
     - Divider lines between sections
     - NOT by card borders, box shadows, or nested containers

  6. Content order — Year Round state:
     [1] CurrentStatusSection   — 2026 filed return, amounts, doc access
     [2] RecommendedActions     — 2027 strategy: quarterly, tax laws, business changes
     [3] YourExpert             — Susan card, connect options
     [4] BottomBar              — Ask input (always pinned)

  Exception: QuarterlyCountdown MAY use --color-warning-subtle background
  when ≤14 days from deadline (urgency signal, not depth).
```

---

## 2. Foundation Components (shadcn/ui)

Use these as-is. Customize only at the token layer above — do not override component internals.

| Component | Use In Widget | Customization |
|:----------|:--------------|:--------------|
| `Tabs` | Overview / Deductions / Activity tab bar | Underline style (Atlassian), not pill |
| `Badge` | Notification count, status labels, return stage | Color maps to semantic tokens only |
| `Button` | All CTAs — primary, secondary, ghost | Radius: `--radius-md`, min height: 36px |
| `Sheet` | Expert connection panel (expands inline from bottom) | Slide up from bottom, `--duration-slow` |
| `Card` | Action item rows, data viz containers | 1px border + `--shadow-sm`, no heavy shadow |
| `Input` | Ask text field (bottom bar) | Full-width, 40px height, no label (placeholder only) |
| `Separator` | Section dividers within the panel | 1px, `--color-border`, inset 16px (Apple HIG) |
| `Skeleton` | Loading state for all data views | Animated shimmer — never use Spinner for in-place loads |
| `Tooltip` | Icon-only buttons (call, video), deep-link arrows | Max width 180px, 200ms delay (Atlassian) |
| `ScrollArea` | Action items list overflow, activity feed | Auto-hide scrollbar (macOS native feel) |
| `Avatar` | Expert profile in connection sheet | 40px circle, initials fallback |
| `Progress` | Return progress stepper stages | Horizontal bar + stage labels below |

---

## 3. Feature Components

Custom components built on top of the foundation layer. Listed in build priority order.

---

### 3.1 StatusBarTrigger
**Reference: Apple menu bar extras**

The floating button that simulates the macOS status bar icon.

```
Anatomy:
  [icon] [optional badge]

Specs:
  - Position: fixed, bottom-right (16px margin) — simulates menu bar placement
  - Size: 44×44px (Apple minimum touch target)
  - Icon: TurboTax logomark or custom SVG, 20px, --color-brand
  - Background: --color-bg-elevated, --shadow-md, border-radius: --radius-full
  - Badge: 18px circle, --color-danger bg, white text, 10px font, top-right offset (−6px, −6px)
  - Pulsing dot variant: 8px dot, --color-brand bg, keyframe pulse (opacity 1→0.4, scale 1→1.3, 1.5s loop)

States:
  - Default: icon only
  - Has items: numbered red badge (use Atlassian Lozenge logic — cap at 9+)
  - Expert message: pulsing brand-color dot (no number)
  - Panel open: subtle pressed state, --color-bg-subtle bg

Animation:
  - Open: panel scales from 0.95 → 1.0 + fades in, origin bottom-right, --duration-base --ease-default
  - Close: reverse, --duration-fast
```

---

### 3.2 WidgetPanel
**Reference: Apple popover + Stripe card container**

The main floating panel that opens from the trigger.

```
Anatomy:
  [PanelHeader]
  [TabBar — Overview | Deductions | Activity]
  [TabContent — scrollable]
  [BottomBar — Ask input + Connect button]

Specs:
  - Width: 320px (fixed — Apple utility panel convention)
  - Height: min 400px, max 520px (content scrolls within)
  - Position: fixed, anchored above StatusBarTrigger (8px gap)
  - Background: --color-bg (single flat surface — no inner elevation layers)
  - Border: 1px solid --color-border
  - Border-radius: --radius-xl (top corners only if docked to bottom)
  - Internal padding: 0 (sections handle their own padding via border-bottom dividers)
  - Shadow: --shadow-panel on the panel itself ONLY — no shadows on children
  - z-index: 9999

Multi-view navigation:
  - Widget hosts multiple views in a .views-host container (position: relative, overflow: hidden)
  - Active view: translateX(0). Behind (pushed back): translateX(-28%). Forward (pending): translateX(100%)
  - Transition: 260ms cubic-bezier(0.4, 0, 0.2, 1) — no spring here, keeps feel native
  - JS view stack: push on navigate(), pop on goBack()
  - Back button appears in header when stack depth > 1
  - Views: main | expert-detail | action-detail (content injected via data attributes)
  - .views-host is flex: 1. .widget-footer is flex-shrink: 0 — always pinned below views

Responsive behavior:
  - If viewport < 400px wide: full-width, bottom-anchored sheet
```

---

### 3.3 PanelHeader
**Reference: Stripe dashboard header + Apple window chrome**

```
Anatomy:
  [ExpertAvatar + ExpertName + StatusDot] [ReturnStageChip]

Specs:
  - Height: 56px
  - Padding: 0 16px
  - Background: --color-bg (flat — no elevated header bg per Widget Flat Layout Doctrine)
  - Bottom border: 1px solid --color-border
  - ExpertAvatar: 32px, Avatar component, with 8px status dot (green = available, gray = offline)
  - ExpertName: --text-sm, --font-weight-semibold, --color-text-primary
  - "Your Expert" label: --text-xs, --color-text-tertiary, above the name
  - ReturnStageChip: Badge component — "Preparing" / "In Review" / "Ready to File" / "Filed"
    - Colors: Preparing=neutral, In Review=warning, Ready=success, Filed=brand
    - Float right
```

---

### 3.4 ReturnProgressStepper
**Reference: Atlassian progress tracker + Stripe step indicator**

```
Anatomy:
  [Stage 1] ── [Stage 2] ── [Stage 3] ── [Stage 4]
  Preparing   Expert Review  Ready       Filed

Specs:
  - Full width within section padding (16px horizontal)
  - 4 stages, horizontal, equally spaced
  - Connector line: 1px, --color-border (incomplete) / --color-brand (complete)
  - Stage node: 20px circle
    - Completed: --color-brand fill, white checkmark icon (12px)
    - Active: --color-brand border (2px), white fill, --color-brand dot (6px) inside
    - Incomplete: --color-border border, --color-bg fill
  - Stage label: --text-xs, centered below node
    - Active: --color-text-primary, --font-weight-medium
    - Complete: --color-text-tertiary
    - Incomplete: --color-text-tertiary

DO NOT use percentages. Customers understand stages, not percentages (from PRD).
```

---

### 3.5 FinancialSummaryCard
**Reference: Robinhood portfolio view — numbers as hero**

The primary data viz card. Number is the hero; chart is supporting context.

```
Anatomy:
  [Label]
  [HeroValue]  [DeltaBadge]
  [SupportingChart or ProgressBar]
  [SubLabel]

Specs:
  - Padding: 16px
  - Border-bottom: 1px solid --color-border (section divider — no card border, no shadow inside widget)
  - Label: --text-xs, --color-text-tertiary, uppercase, letter-spacing: 0.06em (Stripe label style)
  - HeroValue: --text-xl (28px), --font-weight-bold, --color-text-primary (Robinhood: number front and center)
  - DeltaBadge: inline pill — green/red background, white text, --text-xs — positive = up arrow, negative = down
  - Chart: Recharts ResponsiveContainer, height 48px — NEVER fixed pixel width
    - Bar chart for deductions by category (horizontal, no axes, just bars + labels)
    - No grid lines. No border. Chart tooltip: one value, no border, --color-bg bg, --shadow-sm
  - SubLabel: --text-xs, --color-text-tertiary

Variants:
  - DeductionsSummary: HeroValue = total deductions YTD, chart = category breakdown bars
  - EstimatedLiability: HeroValue = estimated tax owed, DeltaBadge = vs. last year
  - QuarterlyEstimate: HeroValue = Q[n] amount due, SubLabel = due date countdown
```

---

### 3.6 QuarterlyCountdown
**Reference: Atlassian deadline badge + Robinhood time-sensitive indicator**

```
Anatomy:
  [CalendarIcon] [QuarterLabel] [AmountDue] [DueDateLabel] [DaysRemaining]

Specs:
  - Background: --color-warning-subtle if ≤14 days, --color-bg-subtle otherwise
  - Border: 1px solid --color-warning if urgent, --color-border otherwise
  - Border-radius: --radius-lg, padding: 12px 16px
  - QuarterLabel: --text-xs, --color-text-tertiary ("Q2 Estimated Tax")
  - AmountDue: --text-lg, --font-weight-bold, --color-text-primary ("$3,840")
  - DueDateLabel: --text-sm, --color-text-secondary ("Due June 15")
  - DaysRemaining: --text-xs, --color-warning if urgent ("35 days")
  - CalendarIcon: Lucide `Calendar`, 16px, color matches urgency state
```

---

### 3.7 ActionItemRow
**Reference: Atlassian inline task + Apple list row**

The scannable action list. One item, one CTA, maximum clarity.

```
Anatomy:
  [TypeIcon] [Content: Title + SubLabel] [Chevron]

Interaction model:
  - The ENTIRE ROW is the tap target — no inline CTA buttons
  - Row hover: background transitions to #F6F8FA (--duration-fast)
  - Chevron: always visible, --color-text-tertiary, 12px
  - Tap/click navigates to action-detail view (multi-view nav stack)

Specs:
  - Min-height: 52px (Apple standard list row)
  - Padding: 12px 16px
  - Hover: background #F6F8FA, transition --duration-fast
  - Bottom border: 1px --color-border (last row: none)
  - TypeIcon wrap: 28×28px, border-radius: --radius-md
    - Warning type: --color-warning-subtle bg, --color-warning icon
    - Info type: --color-brand-subtle bg, --color-brand icon
    - Neutral type: #F0F2F5 bg, --color-text-secondary icon
    - Icon: 14px SVG, consistent stroke-width 1.3–1.4px
  - Title: --text-sm, --font-weight-medium, --color-text-primary, line-height 1.35
  - SubLabel: --text-xs, --color-text-tertiary
  - Chevron: Lucide `ChevronRight`, 12px, --color-text-tertiary

Max 5 items visible. Remaining accessible via ScrollArea.
```

---

### 3.8 ExpertConnectionSheet
**Reference: Apple bottom sheet + Atlassian inline dialog**

Expands upward from the BottomBar when "Connect with Expert" is tapped. Does NOT navigate away from the widget.

```
Anatomy:
  [SheetHandle]
  [ExpertProfile — Avatar + Name + Specialty]
  [ChannelOptions — Chat | Call | Video]
  [RecentContext snippet — last shared item]
  [StartSession CTA]

Specs:
  - Trigger: Sheet component, side="bottom"
  - Animation: slides up from BottomBar, --duration-slow, --ease-default
  - Background: --color-bg, --shadow-lg, --radius-xl top corners
  - SheetHandle: 32×4px rounded bar, --color-border, centered, 12px from top
  - ExpertProfile:
    - Avatar: 48px, with availability dot (green)
    - Name: --text-md, --font-weight-semibold
    - Specialty: --text-sm, --color-text-tertiary ("Business Tax · S Corp")
  - ChannelOptions: 3-column grid, equal width
    - Each option: icon (24px) + label (--text-xs) + description (--text-xs, --color-text-tertiary)
    - Chat: `MessageSquare` / "Async" / "Responds in ~2 hrs"
    - Call: `Phone` / "Call now" / "Available 9am–6pm PT"
    - Video: `Video` / "Video + Screen" / "Schedule or start now"
    - Selected state: --color-brand-subtle bg, --color-brand border
  - RecentContext: --color-bg-subtle block, --radius-md, --text-xs
    - "Last shared: Q1 books connected · 3 days ago"
    - This communicates the context-travels-automatically principle visually
  - StartSession CTA: Full-width Button, primary, "Start [Chat/Call/Video]"
```

---

### 3.9b ExpertFooterCard *(updated from 3.9a)*
**Reference: TurboTax Live expert card + iOS persistent tab bar**

Rich expert card pinned in the widget footer. Shows enough context about the expert that the user wants to tap in. Always visible regardless of which view is active in the views-host, except when already inside the expert detail or chat views.

```
Anatomy:
  [Avatar 56px] [ExpertName / StatsRow (stars · rating · reviews | years exp) / AvailabilityRow] [Chevron]

Specs:
  - Height: 80px (auto, padding 12px 16px)
  - Background: --color-bg
  - Top border: 1px solid --color-border
  - The ENTIRE row is the tap target — navigates to expert-detail view
  - Hover: background #F6F8FA, transition --duration-fast

  Avatar:
    - 56px circle; layered pattern: gradient bg (#1B4F8A→#2D6BC4) + initials z-index:0, photo z-index:1
    - 11px status dot, border 2px --color-bg, bottom-right of avatar

  ExpertName row:
    - Font: 15px, --font-weight-semibold, --color-text-primary
    - Full name ("Susan Larsen")

  StatsRow:
    - ★ (gold #F59E0B) + rating value + (review count) in --text-xs, --color-text-secondary
    - Separator: | --color-border
    - Years exp: --text-xs, --font-weight-semibold, --color-text-secondary

  AvailabilityRow:
    - 6px dot (--color-success) + "Available now" in --text-xs, --color-success, --font-weight-medium
    - When unavailable: dot in --color-warning, text in --color-text-tertiary

  Chevron: 12px, --color-text-tertiary, right side

Visibility rule:
  - display:none when viewStack includes 'expert' or 'chat'
  - display:flex all other views
```

**Supersedes 3.9a.** The compact 52px strip was insufficient — users couldn't tell at a glance who their expert was or why they should tap in.

---

### 3.9 BottomBar
**Reference: Stripe search bar + Apple toolbar**

Always visible. The widget's permanent action layer.

```
Anatomy:
  [AskInput ─────────────────────] [ConnectButton]

Specs:
  - Height: 56px
  - Padding: 8px 12px
  - Top border: 1px solid --color-border
  - Background: --color-bg (matches panel, not subtle — keeps it grounded)
  - AskInput:
    - Flex-grow: 1
    - Height: 36px, --radius-md
    - Placeholder: "Ask a tax question…"
    - Border: 1px solid --color-border
    - Focus: 2px --color-brand outline offset (Stripe focus ring)
    - On enter/submit: opens inline answer in TabContent, not a new page
  - ConnectButton:
    - Width: auto, min-width: 120px
    - Height: 36px
    - Style: primary filled, --color-brand bg
    - Icon: Lucide `UserRound`, 14px, left of label
    - Label: "Connect"
    - Hover: --color-brand-hover bg, --duration-fast transition

These two CTAs are co-equal — same visual weight, same row. Neither is primary over the other (from PRD design principles).
```

---

### 3.10 NotificationBanner
**Reference: Atlassian Flag component + Stripe inline alert**

Slides in from the top of TabContent. Event-driven only — not on a schedule.

```
Anatomy:
  [TypeIcon] [Title + Body] [DismissButton or ActionCTA]

Specs:
  - Position: top of active tab content, pushes content down (not an overlay)
  - Animation: slides down from 0px, opacity 0→1, --duration-slow, --ease-default
  - Border-left: 3px solid (color matches type)
  - Background: semantic subtle color (success/warning/danger/brand -subtle)
  - Border-radius: --radius-md
  - Margin: 8px 16px 0
  - TypeIcon: 16px Lucide, matches border color
  - Title: --text-sm, --font-weight-semibold
  - Body: --text-sm, --color-text-secondary, max 2 lines
  - DismissButton: `X` icon, 14px, --color-text-tertiary, top-right, 24px touch target
  - ActionCTA: text-only link button (--color-brand, --text-sm) if action is available

Types:
  - Info (brand): new tax law, expert message waiting
  - Warning (amber): quarterly estimate due in ≤14 days, form expected
  - Success (green): account connected, document received, expert reviewed
  - Danger (red): action overdue, connection expired
```

---

### 3.11 DocumentUploadZone
**Reference: Stripe file upload + Apple drag-and-drop**

Used in the Phase 1 (Data In) onboarding flow.

```
Anatomy:
  [UploadIcon] [InstructionText] [BrowseLink]
  ── or ──
  [FileList — uploaded docs with status]

Specs:
  - Default state: dashed 2px border, --color-border, --color-bg-subtle fill, --radius-lg
  - Drag-over: --color-brand-subtle fill, --color-brand border (solid), scale 1.01 transform
  - Height: 100px default, expands to show FileList after upload
  - Icon: Lucide `UploadCloud`, 24px, --color-text-tertiary
  - Instruction: --text-sm, --color-text-secondary / "Drag W-2s, 1099s, K-1s here"
  - BrowseLink: text-only, --color-brand / "or browse"
  - FileList item: 40px row — [FileIcon] [FileName + Type] [StatusBadge]
    - StatusBadge: "Received" (success) / "Processing" (warning) / "Needs Review" (danger)
    - Animate in: slide from top + fade, --duration-slow (Stripe's staggered list entrance)
```

---

### 3.12 AccountConnectionItem
**Reference: Stripe bank connection list + Plaid UI patterns**

Used in Phase 1 account linking flow.

```
Anatomy:
  [InstitutionLogo] [InstitutionName + AccountType] [StatusIndicator + ActionCTA]

Specs:
  - Height: 56px
  - Padding: 0 16px
  - InstitutionLogo: 32px square, --radius-sm, 1px --color-border border
  - InstitutionName: --text-sm, --font-weight-medium
  - AccountType: --text-xs, --color-text-tertiary ("Checking · ····4821")
  - StatusIndicator + ActionCTA:
    - Connected: green dot (8px) + "Connected" --text-xs --color-success
    - Recommended: "Connect" ghost button --text-xs
    - Error: "Reconnect" button --text-xs --color-danger
  - Divider: inset (Apple HIG), 1px --color-border
```

---

---

### 3.13 StatusBarIconSystem
**Reference: Apple macOS menu bar extras + Robinhood notification dot**

The always-present status bar icon is the product's ambient presence. It communicates the full health of the customer's tax situation at a glance — before they even open the widget.

```
Icon States:
  Clean       — icon only, no badge. Everything is current.
  Attention   — red numbered badge (1–9, then "9+"). Items need action.
  Expert      — pulsing brand-blue dot. Expert has sent a message or is waiting.
  Processing  — subtle animated ring (one rotation, then idle). Background sync in progress.
  Filed       — green checkmark overlay. Return filed successfully.

Icon Visual:
  - 20px SVG mark (TurboTax logomark or custom "T" monogram)
  - Color: --color-brand in light mode, white in dark mode
  - Simulated in browser as: 44x44px fixed circle, bottom-right corner (16px margin)

Badge specs (numbered):
  - 18px circle, --color-danger bg, white text, 10px font-weight-700
  - Top-right offset: -6px, -6px from icon edge
  - Border: 2px solid page background (separates from any bg)
  - Cap: display "9+" for counts above 9 (Atlassian convention)
  - Entrance animation: scale from 0.6 → 1.1 → 1.0, --ease-spring, 150ms

Pulsing dot (expert message):
  - 10px circle, --color-brand bg
  - keyframe: opacity 1→0.4, scale 1→1.3, 1.5s ease-in-out infinite
  - Top-right offset: -4px, -4px
  - Does NOT show a number — the dot alone signals "someone is waiting for you"

Processing ring:
  - 18px circle, 2px stroke, --color-brand, conic gradient sweep
  - One full rotation (360°) at 1.2s linear, then pauses idle for 3s, repeats
  - Stops and disappears when sync completes

Hover tooltip (150ms delay):
  - "Tax Assistant" in light mode
  - Show current return stage: "Expert Review — 2 items need attention"
  - Max width: 200px, --text-xs, --color-bg bg, --shadow-sm
```

---

### 3.14 YearRoundCalendarCard
**Reference: Apple Calendar widget + Atlassian timeline + Robinhood event markers**

The year-round presence component. Shows the next 3–4 tax-relevant dates in a compact horizontal timeline. Surfaces both customer obligations (quarterly payments) and product-side events (form expected dates, expert availability windows).

```
Anatomy:
  [SectionLabel — "Coming Up"]
  [TimelineRow]
    [EventDot] [EventLabel + Date] [DaysRemaining]  × n events
  [ViewFullCalendar — text link]

Specs:
  - Container: no border, no background — floats as a section within TabContent
  - SectionLabel: standard section label convention
  - TimelineRow: vertical stack, gap: 2px between events
  - EventItem height: 44px
    - EventDot: 8px circle — color maps to event type (see below)
    - Connector line: 1px, --color-border, between dots (vertical, inset 3.5px)
    - EventLabel: --text-sm, --font-weight-medium, --color-text-primary
    - Date: --text-xs, --color-text-tertiary
    - DaysRemaining: --text-xs, right-aligned — color shifts by urgency:
        > 30 days: --color-text-tertiary
        8–30 days: --color-warning
        ≤ 7 days:  --color-danger, font-weight-500

Event Types (dot color):
  - Quarterly payment:  --color-brand
  - Form expected:      --color-text-tertiary
  - Law change:         --color-warning
  - Expert check-in:    --color-success
  - Filing deadline:    --color-danger

Sample events for mock data:
  - Q2 Estimated Tax · Jun 15 · 35 days
  - K-1 from Vanguard expected · Jun 30 · 50 days
  - S Corp extension deadline · Sep 15 · 127 days
  - Q3 Estimated Tax · Sep 15 · 127 days
```

---

### 3.15 TaxLawUpdateCard
**Reference: Robinhood market event card + Atlassian change log**

Surfaces tax law changes relevant to the customer's specific situation (S Corp, home office, etc.). Always expert-reviewed before appearing — the card communicates that it's been vetted.

```
Anatomy:
  [TypeTag] [Headline] [ExpertReviewedBadge]
  [BodyText — 2 lines max]
  [CTAs: "See What Changed" deep-link + "Ask Expert"]

Specs:
  - Container: --color-bg-subtle bg, no border, --radius-lg, padding: 14px 16px
  - TypeTag: --text-xs, uppercase, letter-spacing — "Tax Law · S Corp" in --color-warning
  - Headline: --text-sm, --font-weight-semibold
  - ExpertReviewedBadge: inline pill — "✓ Expert reviewed" in --color-success-subtle / --color-success
  - BodyText: --text-sm, --color-text-secondary, 2 lines, line-clamp
  - Divider: 1px --color-border, above CTAs
  - CTAs: side-by-side text links, "See What Changed" → deep-link arrow, "Ask Expert" → connects to expert chat
  - If unread: left border-left: 3px solid --color-warning, no border-radius on left side
```

---

### 3.16 OnboardingWizard
**Reference: Stripe onboarding checklist + Linear progress indicator**

The contextual onboarding experience. Dynamic — the wizard knows what the customer has and hasn't done, and shows only the next relevant step. Not a static checklist.

```
Anatomy:
  [ProgressBar — n of 4 steps complete]
  [CurrentStepCard]
    [StepIcon + StepTitle]
    [ContextualBody — what we know so far]
    [PrimaryAction CTA]
  [CompletedSteps — collapsed, tap to expand]

ProgressBar:
  - Full-width, 4px height, --color-bg-subtle track, --color-brand fill
  - Animate fill on step completion: width transition 400ms --ease-default
  - Label below: "Step 2 of 4 · Connect your accounts"

CurrentStepCard:
  - Slightly elevated: 1px --color-border, --shadow-sm
  - StepIcon: 32px circle, --color-brand-subtle bg, 16px Lucide icon in --color-brand
  - StepTitle: --text-md, --font-weight-semibold
  - ContextualBody: dynamic — shows what we know:
      Step 1 (empty):     "Let's start by connecting your business bank account."
      Step 2 (1 account): "Chase Business connected. Add more accounts for a complete picture."
      Step 3 (accounts):  "Great — 3 accounts connected. Now add any documents you've received."
      Step 4 (docs):      "Everything looks good. Let's match you with a business tax expert."
  - PrimaryAction: Full-width primary Button — label changes per step

CompletedSteps:
  - Collapsed by default: "3 steps complete ✓" in --color-text-tertiary
  - Tap to expand: shows each completed step with green checkmark + summary

Dynamic logic (component knows its state):
  - 0 accounts, 0 docs, no expert → show Step 1 (connect bank)
  - 1+ accounts, 0 docs              → show Step 2 (add more accounts or skip to docs)
  - 1+ accounts, 1+ docs             → show Step 3 (upload remaining / add more)
  - accounts + docs complete         → show Step 4 (expert matching)
  - Expert matched                   → wizard disappears, replaced by PanelHeader with expert
```

---

### 3.17 ExpertMatchCard
**Reference: Airbnb host introduction + Stripe Connect onboarding**

The moment the customer meets their expert. Should feel personal and warm — this is the product's key differentiator, surfaced at exactly the right moment.

```
Anatomy:
  [ExpertAvatar — large, 56px] [ExpertName + Specialty + Years]
  [MatchReasoning — why this expert was selected]
  [TrustSignals — "237 clients · S Corp specialist · 4.9★"]
  [CTAs: "Message Kelly" (primary) + "See Full Profile" (ghost)]

Specs:
  - Container: full-width, --radius-lg, 1px --color-border, subtle --shadow-sm
  - Background: subtle blue tint (--color-brand-subtle) — makes the moment feel distinct
  - Transition in: slide from bottom + fade, 250ms (only appears once — it's a milestone)
  - ExpertAvatar: 56px, with online dot (12px, --color-success, border 2px --color-bg)
  - ExpertName: --text-md, --font-weight-semibold
  - Specialty: --text-sm, --color-text-secondary
  - MatchReasoning: --text-xs, italic, --color-text-secondary
      Example: "Matched for S Corp experience in California"
  - TrustSignals: --text-xs, --color-text-tertiary, bullet-separated
  - CTA "Message Kelly": primary button, full-width
  - CTA "See Full Profile": ghost button, below primary
```

---

### 3.18 ExpertWorkingCard
**Reference: Linear issue status + Stripe payment processing**

Shows that the expert is actively working on the return. Replaces the action item list during active preparation phases. Creates the "full service" feeling — customer is not expected to do anything right now.

```
Anatomy:
  [ExpertAvatar — small] [StatusLine] [WorkingOnLabel]
  [LastActivityRow]
  [ContactCTA — "Ask a question"]

Specs:
  - Container: --color-bg-subtle, --radius-lg, padding 14px 16px
  - ExpertAvatar: 28px, with pulsing green dot (expert is active)
  - StatusLine: --text-sm, --font-weight-medium — "Kelly is working on your return"
  - WorkingOnLabel: --text-xs, --color-text-tertiary — "Currently: Schedule C"
  - Pulsing dot on avatar: indicates live/recent activity, 2.5s ease-in-out loop
  - LastActivityRow: "Last update · 2 hours ago" in --text-xs --color-text-tertiary
  - ContactCTA: ghost button, full-width — "Ask Kelly a question"

States:
  - Active (expert online in last 24h): green dot, "Kelly is working on your return"
  - In Progress (return in expert queue): amber dot, "Kelly has your return in queue"
  - Review Ready (expert finished): brand dot → transitions to ReturnReviewApproval
```

---

### 3.19 ReturnReviewApproval
**Reference: DocuSign signing moment + Stripe payment confirm**

The final milestone before filing. Customer needs to review and approve. This is the highest-stakes interaction in the product — design should feel intentional and unhurried.

```
Anatomy:
  [MilestoneIcon — large checkmark or document icon]
  [Headline — "Your return is ready to review"]
  [ReturnSummary — key numbers at a glance]
  [ReviewItems — list of what expert prepared]
  [ApprovalCTAs — "Review Return" (deep-link) + "Ask Kelly First"]

Specs:
  - Container: full-width card, 1px --color-brand border (milestone moment), --radius-lg
  - Background: very subtle --color-brand-subtle tint
  - MilestoneIcon: 40px circle, --color-brand-subtle, checkmark in --color-brand
    - Entrance: scale 0→1 with spring, 300ms (one-time, not repeating)
  - Headline: --text-lg, --font-weight-bold, centered
  - ReturnSummary: 2-column grid — refund/amount owed + effective rate
    - Refund: shown in --color-success if positive
    - Amount Owed: shown in --color-danger if balance due
  - ReviewItems: brief bulleted list — "Schedule C · Schedule E · Form 2553"
  - "Review Return": full-width primary button → deep-links to TurboTax web review flow
  - "Ask Kelly First": ghost, below primary — for questions before approving

This card replaces ActionItems and ExpertWorkingCard when return is ready.
```

---

### 3.20 SettingsPanel
**Reference: macOS System Settings + Stripe account settings**

Accessible via a gear icon in PanelHeader (top-right). Slides in as a Sheet from the right, overlaying the widget panel.

```
Anatomy:
  [SheetHeader — "Settings" + Back chevron]
  [Section: Appearance]
    - Light / Dark / System (segmented control)
  [Section: Notifications]
    - Estimated tax reminders: toggle
    - Expert messages: toggle
    - New tax laws: toggle
    - Document reminders: toggle
  [Section: Connected Accounts]
    - AccountConnectionItem list (links to Phase 1 flow)
  [Section: Expert]
    - Expert name + specialty
    - "Change Expert" text link
    - "Schedule a call" text link
  [Section: App]
    - "Clear all notifications" text link
    - "Disconnect and sign out" danger text link
    - Version string: --text-xs, --color-text-tertiary

Specs:
  - Sheet animation: slides from right, 200ms --ease-default (horizontal vs bottom for expert sheet)
  - Width: 100% of panel (320px)
  - Each section: SectionLabel + content, separated by 8px gap
  - Toggles: system-style toggle (right-aligned), --color-brand when on
  - Segmented control (appearance):
      3 segments: Light | Dark | System
      Active: filled background --color-brand-subtle, --color-brand text
      Height: 32px, full-width of section
  - Gear icon in PanelHeader: 18px, --color-text-tertiary, hover: --color-text-secondary
    Appears only after onboarding is complete
```

---

### 3.21 DragDropZone (Enhanced)
**Reference: Linear attachment upload + Figma import zone**

Replaces the basic upload zone. Handles multi-file drops, Google Drive picker, and provides rich feedback during and after upload.

```
States:

  Idle:
    - Dashed 1px border, --color-border, --color-bg-subtle fill, --radius-lg
    - UploadCloud icon (24px, --color-text-tertiary) centered
    - Primary text: "Drop documents here" (--text-sm, --color-text-secondary)
    - Secondary: "or browse files · or import from Google Drive" (--text-xs, --color-brand links)

  Drag-over (file hovering above zone):
    - Border becomes 2px solid --color-brand
    - Background: --color-brand-subtle
    - Icon and text color shift to --color-brand
    - Subtle scale: 1.01 transform, 100ms
    - Label changes to: "Release to upload"

  Uploading (after drop):
    - Zone collapses to a thin progress bar (4px)
    - Files appear as rows below, each with a progress indicator
    - Progress bar: indeterminate sweep for each file (1.5s)

  Complete:
    - Zone disappears, replaced by FileList below
    - Each file row: [FileTypeIcon] [FileName] [StatusBadge] [RemoveButton]

Multi-file behavior:
  - Accept up to 20 files in one drop
  - Each file gets its own row, uploading in sequence
  - Files that fail: shown with --color-danger StatusBadge + "Retry" link
  - Files that succeed: StatusBadge transitions from "Uploading" → "Received" (200ms)

Google Drive picker:
  - "Import from Google Drive" link opens OAuth sheet (not a redirect — inline)
  - OAuth sheet uses ExpertConnectionSheet pattern (expands from bottom)
  - After auth: shows Drive file picker filtered to PDF/image types
  - Selected files appear directly in FileList without leaving the widget
```

---

### 3.22 LightDarkModeSystem
**Reference: Apple system appearance + Robinhood dark mode**

The widget supports light and dark mode. Mode follows system by default; user can override in Settings. Dark mode is not an afterthought — it uses a distinct, premium palette.

```
Light Mode Palette (default):
  - Panel bg:        #FFFFFF
  - Surface bg:      #F9FAFB
  - Primary text:    #0D1117
  - Secondary text:  #4B5563
  - Tertiary text:   #9CA3AF
  - Border:          rgba(0,0,0,.08)
  - Brand:           #1B4F8A
  - Brand light:     #4B8EE8  (not used in light — reserved for dark)

Dark Mode Palette:
  - Panel bg:        #0D0E11  (near-black with slight blue cast — Robinhood reference)
  - Surface bg:      #141518  (for cards, items, rows within the panel)
  - Primary text:    #F2F3F5
  - Secondary text:  rgba(255,255,255,.55)
  - Tertiary text:   rgba(255,255,255,.3)
  - Border:          rgba(255,255,255,.07)
  - Brand:           #4B8EE8  (lighter for dark bg — meets contrast)
  - Success:         #22C55E  (brighter on dark, same semantic meaning)
  - Warning:         #F59E0B  (warm amber — more visible on dark)
  - Danger:          #F87171  (softer red — less alarming on dark)

CSS implementation:
  - All color values as CSS custom properties on :root
  - Dark mode: [data-theme="dark"] overrides on :root
  - System fallback: @media (prefers-color-scheme: dark) matches [data-theme="system"]
  - Transition: color and background-color, 200ms ease (panel feels like it smoothly switches)

Mode toggle (in Settings):
  - Segmented control: Light | Dark | System
  - On change: sets data-theme attribute on the widget root element
  - Preference persisted to localStorage under "tt-widget-theme"
```

---

### 3.23 ExpertProfileCard
**Reference: LinkedIn credential card · Airbnb host profile · Calendly booking flow**

The full expert view. Shown when the customer taps "See Full Profile" from ExpertMatchCard, or navigates via Settings > Expert. This is the primary trust-building surface — every element answers the customer's implicit question: *Is this person qualified to handle my specific situation?*

```
Anatomy:
  [ProfileHero — large avatar + name + credential badges]
  [StatsRow — years exp. | rating + reviews | returns filed]
  [SpecialtyTags — industry + entity type chips]
  [AvailabilityRow — current status + schedule window]
  [ExpertBio — 2-line summary, expandable]
  [MeetingCTA — "Book a Meeting" → expands MeetingScheduler inline]

ProfileHero:
  - Avatar: 72px circle, --radius-full
    - Online status dot: 12px, --color-success, 2.5px --color-bg border, bottom-right
    - Initials fallback: --text-md, --font-weight-semibold, --color-brand bg
  - Name: --text-lg, --font-weight-bold, --color-text-primary
  - CredentialBadges: inline pill row below name, 5px gap
    - Each badge: height 22px, --radius-full, --color-brand-subtle bg, --color-brand text
    - --text-xs, --font-weight-semibold
    - Examples: "CPA" · "EA" · "CFP" · "JD"
    - Max 3 visible; "+1 more" text link in --color-text-tertiary for overflow

StatsRow:
  - 3-column layout, equal width, separated by 1px --color-border dividers
  - Column 1 — Years Experience:
    - Value: --text-2xl (28px), --font-weight-bold, --color-text-primary
    - Label: --text-xs, --color-text-tertiary / "years exp."
  - Column 2 — Rating:
    - 5 SVG filled stars, --color-warning
    - Rating number: --text-md, --font-weight-bold
    - Review count: --text-xs, --color-text-tertiary / "143 reviews"
  - Column 3 — Returns Filed:
    - Value: --text-2xl, --font-weight-bold
    - Label: --text-xs, --color-text-tertiary / "returns filed"

SpecialtyTags:
  - Horizontal wrapping row, gap: 5px, margin-top: 12px
  - Each tag: --radius-full pill, --color-bg-subtle bg, 0.5px --color-border-strong border
  - Text: --text-xs, --color-text-secondary
  - Examples: "S Corp" · "Sole Proprietor" · "Real Estate" · "California" · "Crypto"
  - Cap at 5 visible; overflow: "+2 more" link in --color-text-tertiary

AvailabilityRow:
  - Height: 36px, flex, align-center, gap: 7px
  - Left: status dot (8px) + status text (--text-sm, --color-text-primary, --font-weight-medium)
    - Available now: --color-success dot + "Available now"
    - Available today: --color-success dot + "Available today · 9am–6pm PT"
    - Busy: --color-warning dot + "Responds within 2 hours"
    - Offline: --color-text-tertiary dot + "Back Monday"
  - Right: schedule text (--text-xs, --color-text-tertiary) e.g. "Mon–Fri · 9am–6pm PT"

ExpertBio:
  - --text-sm, --color-text-secondary, line-height: 1.55
  - 2-line clamp by default
  - "Read more" expand link: --color-brand, --text-xs
  - Example: "S Corp and partnership specialist with 11 years in California business tax.
    Previously at Deloitte. Fluent in Mandarin."

MeetingScheduler (expanded, triggered by "Book a Meeting"):
  - Trigger: ghost button, full-width → expands inline below bio
  - Expansion: height 0 → auto, --duration-slow, --ease-default
  - Border-top: 0.5px solid --color-border

  DateStrip (horizontal scroll):
    - 7 days: today + 6 future
    - Each day tile: 44×52px, --radius-md
      - day-of-week: --text-xs, --color-text-tertiary, uppercase
      - date number: --text-md, --font-weight-medium, --color-text-primary
      - Selected: --color-brand bg, white text
      - Today: 5px dot below date (--color-brand, or white if selected)
      - Unavailable: 35% opacity, pointer-events: none
    - Horizontal scroll with snap, scrollbar hidden

  TimeSlots:
    - 3-column grid, gap: 6px
    - Each slot: height 36px, --radius-md, --color-bg-subtle bg, 0.5px --color-border border
    - --text-xs, --font-weight-medium, centered
    - Hover: --color-brand-subtle bg, --color-brand border + text
    - Selected: --color-brand-subtle bg, --color-brand border + text
    - Booked: line-through, --color-text-tertiary, non-interactive

  ConfirmButton:
    - Full-width primary, disabled until both date + time are selected
    - Label: "Confirm 9:00 AM · Tuesday" — updates dynamically on selection
    - After confirm: button hidden → ScheduledConfirmation appears

States:
  - Default: profile info + "Book a Meeting" ghost button at bottom
  - Scheduler open: MeetingScheduler expanded below bio, button label → "Cancel"
  - Scheduled: "✓ Meeting scheduled" row with date, time, and expert name + "Reschedule" link
```

---

## 4. Layout System

### Panel Section Anatomy
Every section within the widget follows this spacing contract:

```
WidgetPanel (320px wide)
├── PanelHeader (56px, always visible)
├── TabBar (40px, always visible)
├── TabContent (flex-1, scrollable)
│   ├── Section (padding: 16px 16px 0)
│   │   ├── SectionLabel (--text-xs, uppercase, letter-spacing, --color-text-tertiary)
│   │   ├── [Component]
│   │   └── [Component]
│   ├── Separator (1px, inset 16px)
│   ├── Section ...
│   └── ActionItemList (no extra padding — rows handle their own)
└── BottomBar (56px, always visible)
```

### Spacing Contract
- Panel internal padding: `16px` horizontal
- Section-to-section gap: `12px`
- Item-to-item within a section: `8px`
- Between label and first component: `8px`
- Component internal padding: `12px` or `16px` (never less, never more)

### Tab Content: Overview Tab Layout

```
[ReturnProgressStepper]          ← 72px
[Separator]
[FinancialSummaryCard — Deductions]  ← 96px
[FinancialSummaryCard — Quarterly]   ← 80px (or QuarterlyCountdown)
[Separator]
[SectionLabel — "Needs Your Attention"]
[ActionItemRow × n]              ← 52px each, max 5 visible
[Separator if expert message]
[NotificationBanner if event]    ← dismissible
```

---

## 5. State System

Every data view must implement all three states. No exceptions.

| Surface | Loading | Empty | Error |
|:--------|:--------|:------|:------|
| ReturnProgressStepper | Skeleton (3 nodes, animated shimmer) | "No return started yet" + "Get Started" CTA | "Can't load status" + retry link |
| FinancialSummaryCard | Skeleton rect (60px height) | "Connect an account to see [deductions/estimate]" | "Data unavailable" + retry |
| ActionItemList | 3× ActionItemRow skeletons | "You're all caught up." + green checkmark icon | "Couldn't load items" + retry |
| QuarterlyCountdown | Skeleton rect (40px) | "No upcoming estimates" | "Estimate unavailable" |
| ExpertConnectionSheet | Avatar skeleton + 2 text line skeletons | n/a (expert always shown if matched) | "Expert unavailable · Try again" |
| ActivityTab | List skeletons (4 rows) | "No activity yet. Actions you take will appear here." | "Couldn't load activity" |

**Skeleton specs (Stripe):** 
- Background: `--color-bg-subtle` base with `--color-border` shimmer overlay
- Animation: shimmer sweep left→right, 1.5s linear infinite
- Shimmer: `linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.6) 50%, transparent 100%)`
- Never show both a skeleton and real content simultaneously

---

## 6. Motion System

| Interaction | Duration | Easing | Notes |
|:------------|:---------|:-------|:------|
| Panel open | 150ms | `--ease-default` | Scale 0.96→1.0 + opacity 0→1, origin bottom-right |
| Panel close | 100ms | `--ease-in-out` | Faster close = feels snappy (Stripe) |
| Sheet expand | 200ms | `--ease-default` | Slide up from bottom |
| Sheet close | 150ms | `--ease-in-out` | |
| Notification slide in | 200ms | `--ease-default` | Translate Y: -8px → 0, opacity 0→1 |
| Badge pop | 150ms | `--ease-spring` | Scale 0.6 → 1.1 → 1.0 (spring overshoot) |
| Row hover | 100ms | `--ease-default` | Background color only |
| Button press | 80ms | `--ease-default` | Scale 0.98 only on :active |
| Skeleton shimmer | 1500ms | linear | Loop — background-position sweep |
| Success state | 200ms | `--ease-spring` | Icon swap + color change on completion |

**No looping animations except:** skeleton shimmer and the pulsing status dot (both have clear semantic purpose).

---

## 7. Brand Reference Patterns

What to steal — exactly — from each reference.

### Stripe
- **Typography rhythm:** 14px body, 1.5 line-height, two weights only (400 + 600). If it looks corporate, reduce the weight.
- **Color usage:** Color signals state, never decoration. Ask: "Does this color tell the user something?" If no, remove it.
- **Card treatment:** 1px border + `--shadow-sm`. Never aggressive drop shadows. Cards feel like paper, not floating.
- **Skeleton loaders everywhere.** Spinners only for full-page loads. Skeletons for in-place content.
- **Fast, confident transitions.** 150ms. If an animation draws attention to itself, it's too slow or too dramatic.
- **Label convention:** `--text-xs`, uppercase, letter-spacing 0.06em, `--color-text-tertiary`. Use this above every data section.

### Atlassian
- **Lozenge (Badge) for status.** Status is always a pill — never just a colored dot without a label in contexts where the meaning isn't established.
- **Semantic color tokens.** Never use `green` or `red` directly — always `--color-success` / `--color-danger`. Makes dark mode easy later.
- **Inline dialog for expert sheet.** Expands within the widget, doesn't navigate away. Atlassian's inline dialog pattern is exactly this.
- **Flag component for notifications.** Slides in, has a dismiss. Doesn't block the underlying content.
- **Tooltip delay: 200ms.** Appears on hover but not instantly — prevents tooltip flicker during normal navigation.
- **Focus rings:** 2px offset, `--color-brand`. Required on every interactive element. Non-negotiable for accessibility.

### Robinhood
- **Hero number treatment.** Whatever the most important financial figure is — deductions total, estimated tax — give it `--text-xl` or larger, `--font-weight-bold`, `--color-text-primary`. Everything else is subordinate.
- **Chart as context, not content.** The sparkline/bar chart exists to give dimension to the number. If you removed the chart, the user should still have the critical information.
- **Recharts configuration:** No axes, no grid, no labels on the chart. Tooltip only. `ResponsiveContainer` always. Chart height: 48px for summary cards.
- **Delta indicators:** Green/red inline with the hero number — `↑ $1,240 this quarter` — not in a separate row below.
- **List items:** Institution name + masked account number on line 1, balance on line 2. Clean, dense, legible.

### Apple (macOS HIG)
- **Panel dimensions:** 320px wide is the sweet spot for utility panels. Wide enough to be readable, narrow enough to feel like a widget (not an app).
- **Corner radius:** 12px for the panel (macOS popover default). 8px for cards inside the panel.
- **Inset dividers:** Dividers between list rows start 52px from the left edge (after icon + gap), not full-width. This is an Apple detail that makes lists feel native.
- **Compact but breathable.** 52px list rows. 56px headers/footers. 8px between items within a section. 12px between sections.
- **Status indicator:** The small dot next to the expert avatar — 8px, border 2px white, positioned bottom-right of the avatar. Green = available, gray = offline. No label needed.
- **System colors as fallback:** `--color-success: #00875A` is the web equivalent of macOS `systemGreen`. Keep it muted (not neon) — it reads as "all good" not "alarm."

---

## 8. Component Build Order

Build in this sequence. Each phase produces something demoable.

**Phase 0 — Shell (2–3 hrs)**
1. `StatusBarTrigger` — floating button, badge state, open/close toggle
2. `WidgetPanel` — frame, shadow, position, animation
3. `TabBar` — Overview / Deductions / Activity tabs, underline style
4. `BottomBar` — Ask input + Connect button, always visible

**Phase 1 — Overview Tab (3–4 hrs)**
5. `PanelHeader` — expert avatar, name, availability, stage chip
6. `ReturnProgressStepper` — 4 stages, active state
7. `FinancialSummaryCard` — deductions + quarterly estimate
8. `ActionItemRow` — 3–4 sample items with mock data
9. `NotificationBanner` — 1 sample event notification

**Phase 2 — Data In Flow (3–4 hrs)**
10. `AccountConnectionItem` — 3–4 institutions, mix of connected/recommended
11. `DocumentUploadZone` — drag-and-drop, with sample uploaded docs
12. Expert matching intro card (simplified — avatar + name + "Message Now" CTA)

**Phase 3 — Expert Connection (2–3 hrs)**
13. `ExpertConnectionSheet` — Chat/Call/Video options, recent context snippet
14. `ExpertProfileCard` — full profile with credentials, stats, specialty tags, availability, and meeting scheduler
15. Chat simulation — pre-scripted exchange with the expert
16. Deep-link simulation — button opens full-screen "TurboTax web" view overlay

**Phase 4 — Year-Round + Settings (3–4 hrs)**
16. `YearRoundCalendarCard` — 3–4 upcoming events with urgency colors
17. `TaxLawUpdateCard` — 1–2 sample law change cards with expert-reviewed badge
18. `SettingsPanel` — appearance toggle, notification toggles, connected accounts
19. `LightDarkModeSystem` — CSS token switch, data-theme attribute, localStorage persist
20. All skeleton states for every data view

**Phase 5 — Polish (remaining time)**
21. Badge pop animation on StatusBarTrigger
22. Notification slide-in animation
23. Panel open/close spring animation
24. ExpertWorkingCard + ReturnReviewApproval milestone states
25. Deductions tab — bar chart in Recharts

---

## 9. Component × HMW Mapping

Every component should map to at least one HMW. If it doesn't, question whether it belongs.

| Component | HMW |
|:----------|:----|
| StatusBarIconSystem | Presence — expert continuously visible in workspace |
| YearRoundCalendarCard | Proactivity — surface tax-relevant moments as they happen |
| TaxLawUpdateCard | Proactivity + Trust — expert-reviewed changes reach customer fast |
| OnboardingWizard | Frequency — small moments of progress build toward relationship |
| ExpertMatchCard | Trust + Reachability — expert feels available from minute one |
| ExpertProfileCard | Trust — depth of credentials and track record gives customers confidence to hand over their return |
| ExpertWorkingCard | Trust — customer sees expert is working; no need to check in |
| ReturnReviewApproval | Reachability — customer can act from inside their day |
| ActionItemRow | Reachability — every action has one clear path |
| ExpertConnectionSheet | Reachability + Trust — context travels, no briefing needed |
| NotificationBanner | Proactivity + Presence — event-driven, never noise |
| DocumentUploadZone / DragDrop | Frequency — frictionless contribution to the shared context |
| SettingsPanel | Presence — customer in control of ambient presence level |
| FinancialSummaryCard | Trust — customer can see their situation is understood |
| ReturnProgressStepper | Presence — filing stage always visible, no mystery |

---

*Reference this file throughout the build. If a component decision isn't documented here, add it before you build — don't decide in code.*
