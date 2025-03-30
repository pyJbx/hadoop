#!/usr/bin/env python3
import sys

crime_counts = {}

for line in sys.stdin:
    crime, count = line.strip().split("\t")  # Split (Key, Value)
    count = int(count)

    if crime in crime_counts:
        crime_counts[crime] += count
    else:
        crime_counts[crime] = count

for crime, total in crime_counts.items():
    print(f"{crime}\t{total}")  # Output (Crime Type, Total Count)
