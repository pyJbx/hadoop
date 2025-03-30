#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Data is tab-separated
    date_occ = fields[2]  # 'DATE OCC' column (Index 2 based on sample data)
    if date_occ:  # Ignore empty values
        print(f"{date_occ}\t1")