from string import ascii_lowercase as alc

key = {}

val = 1
for i in alc:
    key[i] = val
    key[i.upper()] = val + 26

    val += 1

tot = 0

file = open("dev/AoC/2022/input_day_3.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        pocket_1 = content[0 : len(content) // 2]
        pocket_2 = content[len(content) // 2 :]
        common = "".join(set(pocket_1).intersection(pocket_2))
        tot += key[common]
print("part 1: ", tot)


from string import ascii_lowercase as alc

key = {}

val = 1
for i in alc:
    key[i] = val
    key[i.upper()] = val + 26

    val += 1

tot = 0
cnt = 1
bags = []

file = open("dev/AoC/2022/input_day_3.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        bags.append(content)
        if cnt % 3 == 0:
            common = "".join(
                set("".join(set(bags[0]).intersection(bags[1]))).intersection(bags[2])
            )
            tot += key[common]
            bags = []
        cnt += 1
print("part 2: ", tot)
