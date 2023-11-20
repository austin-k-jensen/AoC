from aocd import get_data
from aocd import submit
import re

YEAR, DAY = 2022, 9
puzzle = get_data(day=DAY, year=YEAR)

test = """
    R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2
"""

moves = [(dir, int(dist)) for (dir, dist) in re.findall(r'([UDRL]) (\d+)', puzzle)]

head = [0,0]
tail = [0,0]
visted = []
for m in moves:
    # print(m)
    for i in range(m[1]):
        if m[0] =='U':
            head[1]+=1
            if abs(head[1]-tail[1]) > 1:
                tail[1]+=1
                if abs(head[0]-tail[0]) > 0:
                    tail[0]+=head[0]-tail[0]
        elif m[0] =='D':
            head[1]+=-1
            if abs(head[1]-tail[1]) > 1:
                tail[1]+=-1
                if abs(head[0]-tail[0]) > 0:
                    tail[0]+=head[0]-tail[0]
        elif m[0] =='R':
            head[0]+=1
            if abs(head[0]-tail[0]) > 1:
                tail[0]+=1
                if abs(head[1]-tail[1]) > 0:
                    tail[1]+=head[1]-tail[1]
        elif m[0] =='L':
            head[0]+=-1
            if abs(head[0]-tail[0]) > 1:
                tail[0]+=-1
                if abs(head[1]-tail[1]) > 0:
                    tail[1]+=head[1]-tail[1]
        # print(head,tail)
        visted.append((tail[0],tail[1]))

P1_ANSWER = len(set(visted))
print(P1_ANSWER)
        

        


submit(P1_ANSWER, part="a", year=YEAR, day=DAY)
# submit(P2_ANSWER, part="b", year=YEAR, day=DAY)