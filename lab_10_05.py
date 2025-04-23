with open('students.csv', 'r') as src, open('students_upper.csv', 'w') as dest:
    for line in src:
        dest.write(line.upper())

print("Lowercase characters replaced with uppercase in copied file.")