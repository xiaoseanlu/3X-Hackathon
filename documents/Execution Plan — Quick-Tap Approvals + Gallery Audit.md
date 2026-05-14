# Execution Plan
**v-main Year-Round Hub Expansion · Component Gallery Audit**
Team Malumin · May 14, 2026 · v3

---

## Part 1 — Year-Round Hub (v-main) Expansion

### Layout order (final)

```
1. Global stepper                — existing, no change
2. 2026 Tax Year card            — existing, no change
3. 2027 Tax Year Strategy        — existing, stays at #3
4. Actions needed                — NEW (Quick-Tap Approvals)
5. Notification banner           — NEW (proactive deduction alert, auto-surfaces)
6. Deductions                    — MOVE IN from tax-review hub
7. Coming Up calendar            — existing
8. Connected Accounts            — NEW, moved to bottom (settings-level)
```

**Rationale for order:** 3–4 are things that need attention now. 5–6 flow together — the banner announces what was found, the section below shows the updated total. 7 is time/calendar context. 8 is utility/settings — the user set it up once and it runs in the background; it doesn't need to be front-and-center every time.

---

### Section 4 — Actions needed (Quick-Tap Approvals)

`w-sec` with section header + count badge. Two `hub-approval-card` items. All classes exist today.

**Item 1 — Q2 Tax Payment**
```
Name:        Q2 Estimated Tax · June 15, 2026
Amount:      $3,840
Description: Susan reviewed your Q1 income and calculated your Q2 estimated
             payment. Confirm so she can set up the reminder and keep your
             books current before the deadline.
Flag:        📅 Susan calculated · Q2 2027 estimate
Buttons:     [Approve]   [Change amount]
```

**Item 2 — Flagged Expense**
```
Name:        Malucchi's Ranch · $500.00 · March 14, 2026
Description: No prior history at this merchant. Susan needs you to confirm
             whether this was a business meal before she categorizes it as
             a deductible expense.
Flag:        🔍 Susan flagged · Uncategorized expense
Buttons:     [Business expense]   [Personal — skip]
```

**Behavior:** `approveItem()` handles both approve buttons (turns green ✓, decrements badge). When both cards resolve, section collapses — ~5-line JS addition. "Change amount" and "Personal — skip" resolve inline with alternate `.done` labels ("Changed" / "Skipped").

---

### Section 5 — Notification banner (proactive deduction alert)

**Component:** Existing `.notif-banner.success` — green left-border, `#E3FCEF` background, 200ms slide-in animation. Already fully built, zero new CSS.

**Content:**
```
Title:  New deduction found
Body:   $450 · WeWork coworking · added to Software & Subscriptions
```

**Trigger:** Auto-surfaces ~800ms after the user enters the year-round hub (simulates a live sync event from the connected QuickBooks account). Implemented with `setTimeout` inside `demoGoto('yearround')` — same pattern as the Q2 payment confirmation banner.

**Placement:** Between Actions needed and Deductions. Reads as: "Here's what just came in from your connected accounts" — then the Deductions section below shows the updated running total that includes it.

**Dismiss:** Existing ✕ button, same as notifBanner. Banner stays until dismissed (no auto-hide).

**Implementation:** Second banner div `id="notifBannerDeduction"` — doesn't conflict with the existing `notifBanner` (which is for the Q2 confirmation). Each banner has its own ID and independent show/hide.

---

### Section 6 — Deductions

Already fully built in the tax-review hub. Move in, update content to reflect year-round accumulation in progress.

| Field | Tax-review value | Year-round value |
|:------|:----------------|:----------------|
| Hero | $4,593 | $6,120 |
| Delta | ↑ $1,200 vs last year | Tracked so far · 2027 |
| WeWork bar row | — | Add new row (the one the banner just announced) |

Click behavior unchanged: → `navigate('deductions')`.

---

### Section 7 — Coming Up calendar

Existing, no change. Just moves to position 7 (was position 5 in old layout).

---

### Section 8 — Connected Accounts

Settings-level section at the bottom. **One clickable summary card — not individual ic-card rows.** The hub is an overview page of sections you can drill into; this section is just a glance at account health. Tap the whole thing → `navigate('data-in')` for the full management layer (same as the prep stage connect-accounts view).

**Component:** `w-sec.clickable` — the same pattern as the 2026 Tax Year card. One tap target, full section is the hit area.

**Content (summary stats):**
```
Connected accounts                              [chevron]
────────────────────────────────────────────────────────
3 financial institutions    3 apps connected
Last synced: 2h ago · All accounts active
```

Two stat cells side by side using existing `status-line` / `sl-lbl` / `sl-val` atoms (or a simple two-column flex — no new CSS). A green dot + "All accounts active" subline signals health at a glance.

**What it's NOT:** No individual ic-cards. No Manage link. No ic-add card. Those all live in v-data-in (the next layer). The hub entry is read-only and glanceable — click to manage.

---

### What we are NOT building

- No new CSS classes, no new views, no new interaction patterns.
- "Change amount" resolves inline (no navigation). If you want it to open `action-q2`, tell me — easy change.
- No mobile layout, no real-time data, no new animations.

---

## Part 2 — Component Gallery Audit

### New sections to add (after Part 1 is built)

1. **Quick-Tap Approvals (hub-approval-*)** — default state, resolved state, collapse behavior, reuse rule
2. **Notification banner — year-round variant** — success (green) proactive deduction alert, vs the existing warning (amber) Q2 confirmation
3. **Connected Accounts — year-round variant** — all-connected ic-* cards, clickable (no `.connected` on wrapper), condensed preview format

### Stale sections — update these

| Section | Fix |
|:--------|:----|
| Filing stages stepper | Update to 5-stage: Prep → Review → Ready to File → Filed → Year Round |
| Expert profile view | Add availability row ("Available now · Mon–Fri · 9am–6pm PT") replacing credential badges |
| Expert footer card 3.9b | Diff and align to current v-expert design |
| Year-round calendar | Verify 4-item strip, dot/connector/days columns, color coding (warning/tertiary/brand/danger) |
| Layout system | Document flat doctrine: gray scroll bg, white w-sec bars, no shadow, section-8 connected accounts at bottom as utility |
| Action rows v2.3 | Verify full-row hover + icon color system |

### Spot-check sections — probably fine

Status bar icon · Icon system · Color tokens · Typography · Financial summary · Tax law detail cards · Business context card · Expert match item · Upload screen · QB Detail view · Skeleton loader · Institution cards · Institution search · Drag and drop · Notification banners · Expert booking · Chat view · Multi-view navigation · Settings view

### Execution order

1. Build v-main (Part 1) — ~60 min
2. Add new Gallery sections — ~20 min
3. Fix stale Gallery sections — ~45 min
4. Spot-check Gallery sections — ~30 min
5. Final top-to-bottom read of Gallery

Estimated total: ~2.5 hours.

---

## One remaining question

**"Change amount" on the Q2 card:** Resolve inline (simpler, tighter demo flow) or navigate to the existing `action-q2` detail view? My lean is inline — but if you want that view to be part of the recorded demo run, linking there makes it demonstrably deeper.

Everything else is unblocked. Say go.
