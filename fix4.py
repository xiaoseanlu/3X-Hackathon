#!/usr/bin/env python3
"""
fix4.py — Move Connected Accounts card back inside v-main.
Root cause: fix2.py inserted the card AFTER v-main's closing </div>,
making it a loose child of .views-host in normal flow → two-panel layout blowout.
"""

PATH = '/Users/xlu02/Documents/Claude/Claude OS/3X PM-XD Hackathon/prototype/index.html'

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

# The bad pattern: v-main closes, THEN Connected Accounts div appears outside it
OLD = """        </div>

      </div>

        <!-- Connected Accounts summary -->
        <div class="w-sec clickable" onclick="navigate('data-in')" style="border-bottom:none">
          <div class="hub-section-header" style="margin-bottom:var(--s2)">
            <div class="hub-section-title">Connected Accounts</div>
            <svg viewBox="0 0 12 12" fill="none" style="width:12px;height:12px;color:var(--color-text-tertiary)"><path d="M4.5 2.5L8 6l-3.5 3.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
            <div style="width:7px;height:7px;border-radius:50%;background:var(--color-success);flex-shrink:0"></div>
            <span style="font-size:var(--text-xs);color:var(--color-text-secondary)">All accounts active · Last synced 2h ago</span>
          </div>
          <div style="font-size:var(--text-xs);color:var(--color-text-tertiary)">3 financial institutions · 3 apps connected</div>
        </div>

      </div>

      <!-- View: Expert — uses ExpertProfileCard (ep-*) from Component Gallery -->"""

# The fix: put Connected Accounts INSIDE v-main, then close v-main after it
NEW = """        </div>

        <!-- Connected Accounts summary -->
        <div class="w-sec clickable" onclick="navigate('data-in')" style="border-bottom:none">
          <div class="hub-section-header" style="margin-bottom:var(--s2)">
            <div class="hub-section-title">Connected Accounts</div>
            <svg viewBox="0 0 12 12" fill="none" style="width:12px;height:12px;color:var(--color-text-tertiary)"><path d="M4.5 2.5L8 6l-3.5 3.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
            <div style="width:7px;height:7px;border-radius:50%;background:var(--color-success);flex-shrink:0"></div>
            <span style="font-size:var(--text-xs);color:var(--color-text-secondary)">All accounts active · Last synced 2h ago</span>
          </div>
          <div style="font-size:var(--text-xs);color:var(--color-text-tertiary)">3 financial institutions · 3 apps connected</div>
        </div>

      </div>

      <!-- View: Expert — uses ExpertProfileCard (ep-*) from Component Gallery -->"""

if OLD in src:
    out = src.replace(OLD, NEW, 1)
    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(out)
    lines_after = len(out.splitlines())
    print(f'SUCCESS — Connected Accounts moved inside v-main. Lines: {lines_after}')
else:
    print('ERROR — OLD pattern not found. Dumping nearby lines for debug...')
    idx = src.find('<!-- Connected Accounts summary -->')
    if idx >= 0:
        print('Found Connected Accounts at char', idx)
        print(repr(src[idx-300:idx+200]))
    else:
        print('Connected Accounts comment not found at all!')
