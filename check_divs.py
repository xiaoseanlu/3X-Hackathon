#!/usr/bin/env python3
"""Verify div nesting balance from views-host open to expected close."""

PATH = '/Users/xlu02/Documents/Claude/Claude OS/3X PM-XD Hackathon/prototype/index.html'

with open(PATH, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

print(f"Total lines: {len(lines)}")

# Check where views-host closes
depth = 0
for i in range(1368, 4200):
    o = lines[i].count('<div')
    c = lines[i].count('</div>')
    depth += o - c
    if depth == 0 and i > 1368:
        print(f"views-host first closes at line {i+1} (expected ~4086)")
        print(f"  Line content: {repr(lines[i][:100])}")
        break

# Also check v-main div balance
depth2 = 0
for i in range(2219, 2400):
    o = lines[i].count('<div')
    c = lines[i].count('</div>')
    depth2 += o - c
    if depth2 == 0 and i > 2219:
        print(f"v-main closes at line {i+1}")
        print(f"  Line content: {repr(lines[i][:100])}")
        break

# Verify what's right before and after the v-main close
print("\n=== Lines around v-main close ===")
for i in range(2358, 2382):
    d = sum(lines[j].count('<div') - lines[j].count('</div>') for j in range(2219, i+1))
    print(f"  {i+1} (depth={d}): {lines[i][:100]}")
