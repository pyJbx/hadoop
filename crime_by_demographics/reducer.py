#!/usr/bin/env python3
import sys

# Dictionary to store counts
demographics_count = {}

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    
    if not line:
        continue  # Skip empty lines

    parts = line.split("\t")
    
    if len(parts) != 2:
        continue  # Skip malformed lines

    demographic, count = parts  # Unpack values

    try:
        count = int(count)  # Ensure count is an integer
    except ValueError:
        continue  # Skip invalid counts

    # Manually check and update count
    if demographic in demographics_count:
        demographics_count[demographic] += count
    else:
        demographics_count[demographic] = count

# Output aggregated results
for demographic in sorted(demographics_count, key=lambda x: demographics_count[x], reverse=True):
    print(f"{demographic}\t{demographics_count[demographic]}")
