from aocd import get_data
from aocd import submit
import re

YEAR, DAY = 2022, 10
puzzle = get_data(day=DAY, year=YEAR)

small = """
    noop
    addx 3
    addx -5
"""

test = """
    addx 15
    addx -11
    addx 6
    addx -3
    addx 5
    addx -1
    addx -8
    addx 13
    addx 4
    noop
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx 5
    addx -1
    addx -35
    addx 1
    addx 24
    addx -19
    addx 1
    addx 16
    addx -11
    noop
    noop
    addx 21
    addx -15
    noop
    noop
    addx -3
    addx 9
    addx 1
    addx -3
    addx 8
    addx 1
    addx 5
    noop
    noop
    noop
    noop
    noop
    addx -36
    noop
    addx 1
    addx 7
    noop
    noop
    noop
    addx 2
    addx 6
    noop
    noop
    noop
    noop
    noop
    addx 1
    noop
    noop
    addx 7
    addx 1
    noop
    addx -13
    addx 13
    addx 7
    noop
    addx 1
    addx -33
    noop
    noop
    noop
    addx 2
    noop
    noop
    noop
    addx 8
    noop
    addx -1
    addx 2
    addx 1
    noop
    addx 17
    addx -9
    addx 1
    addx 1
    addx -3
    addx 11
    noop
    noop
    addx 1
    noop
    addx 1
    noop
    noop
    addx -13
    addx -19
    addx 1
    addx 3
    addx 26
    addx -30
    addx 12
    addx -1
    addx 3
    addx 1
    noop
    noop
    noop
    addx -9
    addx 18
    addx 1
    addx 2
    noop
    noop
    addx 9
    noop
    noop
    noop
    addx -1
    addx 2
    addx -37
    addx 1
    addx 3
    noop
    addx 15
    addx -21
    addx 22
    addx -6
    addx 1
    noop
    addx 2
    addx 1
    noop
    addx -10
    noop
    noop
    addx 20
    addx 1
    addx 2
    addx 2
    addx -6
    addx -11
    noop
    noop
    noop
"""

# program  = [(dir, int(dist or 0)) for (dir, dist) in re.findall(r'([A-Za-z]{4}) ?(-?\d+)?', small)]
# program  = [(dir, int(dist or 0)) for (dir, dist) in re.findall(r'([A-Za-z]{4}) ?(-?\d+)?', test)]
program  = [(dir, int(dist or 0)) for (dir, dist) in re.findall(r'([A-Za-z]{4}) ?(-?\d+)?', puzzle)]

record = [(0,1)]
cycle = 0
signal = 1

for line in program:
    # print(line)
    if line[0] == 'noop':
        cycle+=1
        record.append((cycle,signal))
    if line[0] == "addx":
        cycle+=1
        record.append((cycle,signal))
        cycle+=1
        record.append((cycle,signal))
        signal+=line[1]
    # print(record)

P1_ANSWER = 0
for i in range(20,221,40):
    P1_ANSWER+=(record[i][0]*record[i][1])
print(P1_ANSWER)

record.pop(0)
crt = ''
mod = 0
for i in record:
    print(i)
    if i[0]%40 == 0:
        mod+=40

    if (i[1]-1) <= (i[0]-1-mod) <= (i[1]+1):
        crt+='#'
        print('#')
    else:
        crt+='.'
        print('.')

    if i[0]%40 == 0:
        crt+='\n'
print(crt)

# submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
# submit(P2_ANSWER, part="b", year=YEAR, day=DAY)