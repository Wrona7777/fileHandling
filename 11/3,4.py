import re # module for regular expressions
import os
os.chdir(os.path.dirname(__file__))
# file name with shopping report
email_file = 'email.txt'

# read the content of email
with open(email_file, "r", encoding="utf-8") as mail:
   content = mail.read()

pattern = r'€\s*(\d{1,3})'

amounts = re.findall(pattern, content)

total = 0
for amount in amounts:
    total += int(amount)
print(total)