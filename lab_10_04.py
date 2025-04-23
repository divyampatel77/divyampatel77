import os
import shutil

new_dir = './new_subdir'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

shutil.copy('students.csv', new_dir + '/students_copy.csv')
print("File copied to new subdirectory.")