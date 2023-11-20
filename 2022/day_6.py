file = open("dev/AoC/2022/input_day_6.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        for i in range(len(content) - 3):
            if len(set(content[i : i + 4])) == 4:
                print("part 1: ", i + 4)
                break
        for i in range(len(content) - 13):
            if len(set(content[i : i + 14])) == 14:
                print("part 2: ", i + 14)
                break
