import subprocess
import re

with open("document1-1") as f:
    data = f.read()

proc = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE)
proc_out = proc.stdout.decode('utf-8')
tag = re.sub('[\\r\\n]', '', proc_out)

print(f"Tag: '{tag}'")
print(f"Data: '{data}'")