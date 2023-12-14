file = open("2022/input_day_2.txt", "r")

guide = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

score = 0

while True:
    content = file.readline()
    if not content:
        file.close()
        break
    else:
        score += guide[content.rstrip()]


print("part 1: ", score)

file = open("2022/input_day_2.txt", "r")

guide = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

score = 0

while True:
    content = file.readline()
    if not content:
        file.close()
        break
    else:
        score += guide[content.rstrip()]

print("part 2: ", score)
