import re

tot_1 = 0
tot_2 = 0

file = open("dev/AoC/2022/input_day_4.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        asgn = [int(s) for s in re.findall(r"\d+", content)]
        if (asgn[0] >= asgn[2] and asgn[1] <= asgn[3]) or (
            asgn[0] <= asgn[2] and asgn[1] >= asgn[3]
        ):
            tot_1 += 1
        if (asgn[1] >= asgn[2] and asgn[0] <= asgn[3]) or (
            asgn[3] >= asgn[0] and asgn[2] <= asgn[1]
        ):
            tot_2 += 1

print("part 1: ", tot_1)
print("part 2: ", tot_2)
