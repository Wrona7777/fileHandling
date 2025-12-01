import os
os.chdir(os.path.dirname(__file__))

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file) as e_file:
   with open(position_file, "w") as p_file:
      for line in e_file:
         if job_title in line:
            p_file.write(line)