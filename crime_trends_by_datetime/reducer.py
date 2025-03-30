#!/usr/bin/env python3
import sys

crime_counts = {}

for line in sys.stdin:
    date_occ, count = line.strip().split("\t")  # Read key-value pair
    count = int(count)

    # logic for crime count
    if date_occ in crime_counts:
        crime_counts[date_occ] += count
    else:
        crime_counts[date_occ] = count

# Output final count for each date
for date_occ, total in sorted(crime_counts.items()):
    print(f"{date_occ}\t{total}")
