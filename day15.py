import numpy as np
import re

day = '15'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

pairs = []

for row in data:
    xs,ys,xb,yb = [int(x) for x in re.findall('-?\d+',row)]
    diff = abs(ys - yb) + abs(xs - xb)
    #diffy,diffx = abs(ys - yb), abs(xs - xb)

    pairs.append([(xs,ys),(xb,yb),(xs-diff, xs+diff, ys+diff, ys-diff)])


max_x = max([max(z[2][:2]) for z in pairs])
max_y = max([max(z[2][2:]) for z in pairs])
min_x = min([min(z[2][:2]) for z in pairs])
min_y = min([min(z[2][2:]) for z in pairs])

#print(max_x,max_y,min_x,min_y)

# my_map = np.matrix([['.']*(max_x-min_x+1)]*(max_y-min_y+1))
move_y = abs(min_y)
move_x = abs(min_x)

#check = 10 + move_y
check = 2000000 + move_y
look = np.array(['.']* abs(max_x+10-min_x))


for pair in pairs:

    ys, xs = pair[0][1],pair[0][0]
    yb, xb = pair[1][1],pair[1][0]

    if yb+move_y == check:
        look[xb + move_x] = 'B'
    elif ys+move_y == check:
        look[xs + move_x] = 'S'

    # my_map[ys+move_y, xs+move_x] = 'S'
    # my_map[yb+move_y, xb+move_x] = 'B'

    yd = pair[2][2] + move_y
    yg = pair[2][3] + move_y

    if True: #check in range(yg,yd):
        #print(ys, xs, yb, xb)
        diff = min(yd - check, check - yg)
        #print(diff)

        for k in range(xs+move_x-diff, xs+move_x+diff+1):
            #print(k)
            if look[k] == '.':
                look[k] = '#'

result = look.tolist().count('#')

# PART 2
import re

day = '15'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

pairs = []
for row in data:
    xs,ys,xb,yb = [int(x) for x in re.findall('-?\d+',row)]
    diff = abs(ys - yb) + abs(xs - xb)

    pairs.append([(xs,ys),(xb,yb)])


points = set()
lines = dict()

def distance(A,B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def is_free(point: tuple[int, int], pairs) -> bool:
    """Returns True if point is outside the exclusion range of every sensor in sensors"""
    for pair in pairs:
        if distance(pair[0],pair[1]) >= distance(pair[0],point):
            return False
    return True

def find_lines(pairs):
    for pair in pairs:
        range = distance(pair[0],pair[1])

        lineA = (True,  pair[0][1] - range - 1 - pair[0][0])
        lineB = (False, pair[0][1] - range - 1 + pair[0][0])
        lineC = (True,  pair[0][1] + range + 1 - pair[0][0])
        lineD = (False, pair[0][1] + range + 1 + pair[0][0])

        for line in [lineA,lineB,lineC,lineD]:
            if line in lines:
                lines[line] += 1
            else:
                lines[line] = 1
    return lines

def find_point(lines):

    rising= []
    descending= []

    for line, n in lines.items():
        if n > 1:
            if line[0]:
                descending.append(line[1])
            else:
                rising.append(line[1])

    points = []

    for rising_q in rising:
        for descending_q in descending:

            x = (rising_q - descending_q) // 2
            y = x + descending_q
            point = (x, y)
            points.append(point)

    for point in points:
        if (
            (0 <= point[1] <= search_area)
            and (0 <= point[0] <= search_area)
            and is_free(point, pairs)
        ):
            return point[0] * 4000000 + point[1]


search_area = 4000000
lines = find_lines(pairs)

result2 = find_point(lines)


print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)