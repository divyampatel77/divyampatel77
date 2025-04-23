import pickle

employee = {
    'EmpCode': 'E001',
    'EmpName': 'Alice',
    'DateOfJoining': '2020-05-15',
    'Salary': 50000
}

with open('employee.dat', 'wb') as f:
    pickle.dump(employee, f)

with open('employee.dat', 'rb') as f:
    loaded_employee = pickle.load(f)

print("Deserialized Employee Data:")
print(loaded_employee)