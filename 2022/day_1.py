file = open("2022/input_day_1.txt", "r")

elfs = {}
items = []
elf = 1

while True:
    content = file.readline()
    if not content:
        break
    if content == "\n":
        elfs[elf] = items
        # print(elf,items)
        items = []
        elf += 1
    else:
        items.append(int(content.rstrip()))

file.close()
elfs[elf] = items

elfs_tot = {}
for i in elfs:
    elfs_tot[i] = sum(elfs[i])

max_elf = max(elfs_tot, key=elfs_tot.get)
print("part 1: ", elfs_tot[max_elf])

top_elfs = {}
for i in range(3):
    top_elfs[max_elf] = elfs_tot[max_elf]
    del elfs_tot[max_elf]
    max_elf = max(elfs_tot, key=elfs_tot.get)

print("part 2: ", sum(top_elfs.values()))
