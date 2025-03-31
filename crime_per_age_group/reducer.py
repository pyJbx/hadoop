#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    fields = line.split("\t")  
    if len(fields) != 2:
        continue  # Skip malformed lines

    crime_type, age_group = fields
    print(f"{crime_type}\t{age_group}")  
