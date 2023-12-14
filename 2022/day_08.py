grid = []

file = open("2022/input_day_8.txt", "r")
while True:
    content = file.readline().rstrip()
    if not content:
        file.close()
        break
    else:
        grid.append([int(d) for d in str(content)])

center = [[0 for col in range(len(grid) - 2)] for row in range(len(grid[0]) - 2)]

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        tree = grid[i][j]
        vis = 0

        comps = []
        for x in range(i):
            comps.append(grid[x][j])
        if tree > max(comps):
            vis += 1

        comps = []
        for x in range(i + 1, len(grid)):
            comps.append(grid[x][j])
        if tree > max(comps):
            vis += 1

        comps = []
        for y in range(j):
            comps.append(grid[i][y])
        if tree > max(comps):
            vis += 1

        comps = []
        for y in range(j + 1, len(grid)):
            comps.append(grid[i][y])
        if tree > max(comps):
            vis += 1

        if vis == 0:
            center[i - 1][j - 1] = 1

trees = len(grid) * len(grid[0])
hid = sum(sum(center, []))
vis = trees - hid
print("part 1: ", vis)

################ Part 2 ################

views = []
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        tree = grid[i][j]
        view = 1

        vis = 0
        comps = []
        for x in range(i):
            comps.append(grid[x][j])
        for comp in comps[::-1]:
            # print(comp)
            if tree > comp:
                vis += 1
            else:
                vis += 1
                break
        view *= vis

        vis = 0
        comps = []
        for x in range(i + 1, len(grid)):
            comps.append(grid[x][j])
        for comp in comps:
            # print(comp)
            if tree > comp:
                vis += 1
            else:
                vis += 1
                break
        view *= vis

        vis = 0
        comps = []
        for y in range(j):
            comps.append(grid[i][y])
        for comp in comps[::-1]:
            # print(comp)
            if tree > comp:
                vis += 1
            else:
                vis += 1
                break
        view *= vis

        vis = 0
        comps = []
        for y in range(j + 1, len(grid)):
            comps.append(grid[i][y])
        for comp in comps:
            # print(comp)
            if tree > comp:
                vis += 1
            else:
                vis += 1
                break
        view *= vis
        views.append(view)
print("part 2: ", max(views))
