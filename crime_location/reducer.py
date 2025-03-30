#!/usr/bin/env python3
import sys
from collections import defaultdict

crime_counts = defaultdict(int)

for line in sys.stdin:
    location, count = line.strip().split("\t")  # Read key-value pair
    crime_counts[location] += int(count)  # Sum up crime occurrences

# Output sorted crime hotspots
for location, total in sorted(crime_counts.items(), key=lambda x: x[1], reverse=True):  # Sort by highest crime count
    print(f"{location}\t{total}")
