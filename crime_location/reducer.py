#!/usr/bin/env python3
import sys

crime_counts = {}

for line in sys.stdin:
    location, count = line.strip().split("\t")  # Read key-value pair
    count = int(count)

    if location in crime_counts:
        crime_counts[location] += count  # Update count
    else:
        crime_counts[location] = count  # Initialize count

# Output sorted crime hotspots
for location, total in sorted(crime_counts.items(), key=lambda x: x[1], reverse=True):  # Sort by highest crime count
    print(f"{location}\t{total}")
