import re

stacks = {
    1: ["V", "C", "D", "R", "Z", "G", "B", "W"],
    2: ["G", "W", "F", "C", "B", "S", "T", "V"],
    3: ["C", "B", "S", "N", "W"],
    4: ["Q", "G", "M", "N", "J", "V", "C", "P"],
    5: ["T", "S", "L", "F", "D", "H", "B"],
    6: ["J", "V", "T", "W", "M", "N"],
    7: ["P", "F", "L", "C", "S", "T", "G"],
    8: ["B", "D", "Z"],
    9: ["M", "N", "Z", "W"],
}

file = open("2022/input_day_5.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        move = [int(s) for s in re.findall(r"\d+", content)]
        for i in range(move[0]):
            crate = stacks[move[1]].pop(len(stacks[move[1]]) - 1)
            stacks[move[2]].append(crate)

top = ""
for i in range(1, 10):
    crate = stacks[i].pop(len(stacks[i]) - 1)
    top += crate
print("part 1: ", top)

stacks = {
    1: ["V", "C", "D", "R", "Z", "G", "B", "W"],
    2: ["G", "W", "F", "C", "B", "S", "T", "V"],
    3: ["C", "B", "S", "N", "W"],
    4: ["Q", "G", "M", "N", "J", "V", "C", "P"],
    5: ["T", "S", "L", "F", "D", "H", "B"],
    6: ["J", "V", "T", "W", "M", "N"],
    7: ["P", "F", "L", "C", "S", "T", "G"],
    8: ["B", "D", "Z"],
    9: ["M", "N", "Z", "W"],
}

file = open("2022/input_day_5.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        move = [int(s) for s in re.findall(r"\d+", content)]
        # print(move)
        # print(stacks[move[1]])
        # print(stacks[move[2]])
        crates = stacks[move[1]][len(stacks[move[1]]) - move[0] :]
        stacks[move[1]] = stacks[move[1]][: len(stacks[move[1]]) - move[0]]
        stacks[move[2]] = stacks[move[2]] + crates
        # print(crates)
        # print(stacks[move[1]])
        # print(stacks[move[2]])

top = ""
for i in range(1, 10):
    crate = stacks[i].pop(len(stacks[i]) - 1)
    top += crate
print("part 2: ", top)
