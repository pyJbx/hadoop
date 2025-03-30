#!/usr/bin/env python3
import sys

status_sex_count = {}

for line in sys.stdin:
    try:
        status, vict_sex, count = line.strip().split("\t")
        count = int(count)
        key = (status, vict_sex)

        if key in status_sex_count:
            status_sex_count[key] += count  # Update count
        else:
            status_sex_count[key] = count
    except Exception:
        continue  # Skip malformed lines

# Output aggregated results
for (status, vict_sex), count in status_sex_count.items():
    print(f"{status}\t{vict_sex}\t{count}")
