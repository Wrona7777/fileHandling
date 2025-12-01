import os
os.chdir(os.path.dirname(__file__))

def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('countries.txt')

file_lines = file_content.splitlines()

file_lines.sort()

for nr, line in enumerate(file_lines, start=1):
    kraj = line.split()[0]
    stolice = line.split()[1]
    populacja = line.split()[2]
    print(f"{nr}. {kraj}, {stolice}, {populacja}")