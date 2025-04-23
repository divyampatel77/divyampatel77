import csv

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    students = []
    for row in reader:
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        row['Total'] = total
        students.append(row)

print("Student Data with Total:")
for student in students:
    print(student)