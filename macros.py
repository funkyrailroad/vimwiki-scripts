def determine_fat_intake(pref):
    if pref == "high":
        return 0.45
    elif pref == "mid":
        return 0.35
    elif pref == "low":
        return 0.25
    else:
        exit()

body_fat_fraction = .15
total_weight = 190
caloric_change = 500
fat_intake_preference = determine_fat_intake("high")
fat_intake_preference = 0.9



total_cals = 14 * total_weight
total_cals += caloric_change
fat_weight = total_weight * body_fat_fraction
lean_body_weight = total_weight - fat_weight

protein_mass = 1 * lean_body_weight
protein_cals = 4 * protein_mass

fat_mass = fat_intake_preference * total_weight
fat_cals = 9 * fat_mass

carbs_cals = total_cals - ( fat_cals + protein_cals )
carbs_mass = carbs_cals / 4.


print("total cals", total_cals)
print("total protein mass", protein_mass)
print("total fat mass", fat_mass)
print("total carb mass", carbs_mass)
