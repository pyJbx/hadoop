#!/usr/bin/env python3
import sys

# Dictionary to store counts
demographics_count = {}

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    try:
        demographic, count = line.split("\t")
        count = int(count)

        # Manually check and update count
        if demographic in demographics_count:
            demographics_count[demographic] += count
        else:
            demographics_count[demographic] = count

    except ValueError:
        continue  # Skip malformed lines

# Output aggregated results
for demographic in sorted(demographics_count, key=lambda x: demographics_count[x], reverse=True):
    print(f"{demographic}\t{demographics_count[demographic]}")
