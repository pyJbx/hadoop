#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\t")  # Assuming tab-separated values

    if len(fields) > 12:  # Ensure correct indexing
        vict_age = fields[11]  # Vict Age
        vict_sex = fields[12]  # Vict Sex

        # Categorize victim age into age groups
        try:
            age = int(vict_age)
            if age < 18:
                age_group = "Under_18"
            elif age < 35:
                age_group = "18_34"
            elif age < 60:
                age_group = "35_59"
            else:
                age_group = "60_plus"
        except ValueError:
            age_group = "Unknown"

        # Emit key-value pair (Victim Sex + Age Group, 1)
        if vict_sex and vict_sex != "Vict Sex":
            print(f"{vict_sex}_{age_group}\t1")
