file1_lines = open('file1.txt').readlines()
file2_lines = open('file2.txt').readlines()

max_len = max(len(file1_lines), len(file2_lines))
merged_lines = []

for i in range(max_len):
    if i < len(file1_lines):
        merged_lines.append(file1_lines[i])
    if i < len(file2_lines):
        merged_lines.append(file2_lines[i])

with open('merged_file.txt', 'w') as f:
    f.writelines(merged_lines)

print("Files merged alternately.")