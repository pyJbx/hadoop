#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Split on tab
    crime_type = fields[9]  # Extract 'Crm Cd Desc'
    print(f"{crime_type}\t1")  # Emit (Crime Type, 1)
