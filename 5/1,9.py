import os
os.chdir(os.path.dirname(__file__))

file_name = 'it_company.csv'
job_title = 'Software Engineer'

with open(file_name) as plik:
    nr = 1
    for line in plik:
        if job_title in line:
            print(f"{nr}. {line}")
            nr += 1