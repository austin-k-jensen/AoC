from collections import defaultdict

dirs = defaultdict(int)
path = []

file = open("dev/AoC/2022/input_day_7.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        content = content.split()
        if content[1] == "cd" and content[2] != "..":
            path.append(content[2])
        if content[1] == "cd" and content[2] == "..":
            path.pop()
        if content[0] != "$" and content[0] != "dir":
            for i in range(len(path)):
                dirs[tuple(path[: i + 1])] += int(content[0])

tot_1 = 0
for dir in dirs:
    if dirs[dir] <= 100000:
        tot_1 += dirs[dir]
print("part 1: ", tot_1)

used = dirs[("/",)]
req = 30000000 - (70000000 - used)
canidates = []
for dir in dirs:
    if dirs[dir] >= req:
        canidates.append(dirs[dir])
print("part 2: ", min(canidates))
