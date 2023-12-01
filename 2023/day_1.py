from aocd import get_data
from aocd import submit
import re

YEAR, DAY = 2023, 1
puzzle = get_data(day=DAY, year=YEAR)

file = open("2023/input_day_1.txt", "r")

tot = 0

while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        line = re.findall(r"\d", content)
        tot += int(line[0] + line[-1])
P1_ANSWER = tot
print("part 1: ", tot)

# submit(P1_ANSWER, part="a", year=YEAR, day=DAY)

key = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

tot = 0
file = open("2023/input_day_1.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        line = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))",
            content,
        )
        trans = []
        for i in line:
            if i in key.keys():
                trans.append(key[i])
            else:
                trans.append(i)
        # print(line)
        # print(trans)
        # print(int(trans[0] + trans[-1]))
        tot += int(trans[0] + trans[-1])
print("part 2: ", tot)
P2_ANSWER = tot

# submit(P2_ANSWER, part="b", year=YEAR, day=DAY)
