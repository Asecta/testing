import os

with open("document1") as f:
    data = f.read()

stream = os.popen("git tag")
while True:
    line = stream.readline()
    if not line: break
    print(line)

print(data)
