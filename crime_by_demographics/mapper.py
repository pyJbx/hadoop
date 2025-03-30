#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Assuming tab-separated values

    vict_age = fields[11]  # Vict Age
    vict_sex = fields[12]  # Vict Sex

    # Categorize victim age into age groups
    age = int(vict_age)
    if age < 18:
        age_group = "Under_18"
    elif age < 35:
        age_group = "18_34"
    elif age < 60:
        age_group = "35_59"
    else:
        age_group = "60_plus"

    print(f"{vict_sex}_{age_group}\t1")
