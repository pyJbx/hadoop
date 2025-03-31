#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Assuming tab-separated values

    vict_sex = fields[12]  # Victim Sex
    status = fields[18]  # Status Desc (Crime Status)

    # Validate data (ignore missing or incorrect values)
    if vict_sex and status and vict_sex in {"M", "F", "X"}:
        print(f"{status}\t{vict_sex}\t1")  # Emit key-value pair with count
