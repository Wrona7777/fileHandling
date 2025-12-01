import os
os.chdir(os.path.dirname(__file__))

original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file) as original:
   content = original.read()

# write the content to the target file (copy)
with open(target_file,"w",encoding="utf-8") as copy:
    copy.write(content)