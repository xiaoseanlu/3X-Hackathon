#!/usr/bin/env python3
PATH = '/Users/xlu02/Documents/Claude/Claude OS/3X PM-XD Hackathon/prototype/index.html'
lines = open(PATH).read().splitlines()

# Check all major views close properly
views = ['v-welcome','v-data-in','v-stage1','v-main','v-expert','v-tax-review','v-settings','v-demo-controls']
starts = {v: next(i for i,l in enumerate(lines) if f'id="{v}"' in l) for v in views}

for v, start in sorted(starts.items(), key=lambda x: x[1]):
    depth = 0
    close = None
    for i in range(start, min(start+300, len(lines))):
        depth += lines[i].count('<div') - lines[i].count('</div>')
        if depth == 0 and i > start:
            close = i + 1
            break
    status = "✓" if close else "UNCLOSED"
    print(f"{status} {v}: opens line {start+1}, closes line {close}")
