# Program 3: Department-wise min and max salary
employees = [
    {"dept": "HR", "roll_no": 1, "salary": 50000},
    {"dept": "HR", "roll_no": 2, "salary": 60000},
    {"dept": "IT", "roll_no": 3, "salary": 80000},
    {"dept": "IT", "roll_no": 4, "salary": 75000}
]

dept_salaries = {}
for emp in employees:
    dept = emp["dept"]
    salary = emp["salary"]
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)

for dept, salaries in dept_salaries.items():
    print(f"{dept} Department -> Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")
