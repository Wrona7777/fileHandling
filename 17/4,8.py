import os
import re

os.chdir(os.path.dirname(__file__))

with open("files.txt", "r") as f:
    content = f.read()
    content = content.splitlines()

for i in range(len(content)):
    rozszerzenie = re.search(r'\.([^.]+)$', content[i])

    if len(rozszerzenie.group(1)) > 3:
        print(content[i])