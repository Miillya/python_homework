import sys
_, work_hours, hour_cost, bonus = sys.argv
salary = (float(hour_cost) *  float(work_hours)) + float(bonus)
print(f"Заработная плата = {salary}")