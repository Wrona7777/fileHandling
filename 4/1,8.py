import os
os.chdir(os.path.dirname(__file__))

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

length = 0

for i in file_lines:
   print(i)
   
   a_list = i.split()
   for j in a_list:
      length += len(j)

print(length)