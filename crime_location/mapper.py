#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Assuming tab-separated values
    lat = fields[26]
    lon = fields[27]  # Extract latitude and longitude
    if lat and lon:  # Ignore header and missing values
        print(f"{lat},{lon}\t1")  # Emit (LAT, LON, 1)
