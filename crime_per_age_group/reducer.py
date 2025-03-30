#!/usr/bin/env python3
import sys

for line in sys.stdin:
    crime_type, age_group = line.strip().split("\t")  # Read key-value pair
    print(f"{crime_type}\t{age_group}")  # Output without counting
