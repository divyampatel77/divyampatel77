import csv

data = [['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'],
        ['101', 'John', '80', '85', '90'],
        ['102', 'Jane', '75', '88', '92']]

with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("CSV file created successfully.")