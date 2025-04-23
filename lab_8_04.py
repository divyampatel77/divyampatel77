# lab_8_04.py
# Separate names in a set into two sets based on first letter (A or B)

names = {"Anil", "Asha", "Bhavik", "Bina", "Amit", "Bobby"}
a_names = {name for name in names if name.startswith('A')}
b_names = {name for name in names if name.startswith('B')}

print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
