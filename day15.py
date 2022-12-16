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

print(max_x,max_y,min_x,min_y)

#my_map = np.matrix([['.']*(max_x-min_x+1)]*(max_y-min_y+1))
move_y = abs(min_y)
move_x = abs(min_x)

#check = 10 + move_y
check = 2000000 + move_y
look = np.array('.'* abs(max_x-min_x))
print(look)

for pair in pairs:
    ys, xs = pair[0][1],pair[0][0]
    yb, xb = pair[1][1],pair[1][0]

    if yb == 2000000:
        my_map[yb + move_y, xb + move_x] = 'A'
    elif yb == 2000000:
        my_map[yb + move_y, xb + move_x] = 'A'

    # HEHRE
    else:
        my_map[ys+move_y, xs+move_x] = 'S'
        my_map[yb+move_y, xb+move_x] = 'B'

    #print(ys,xs,yb,xb)

    yd = pair[2][2]
    yg = pair[2][3]
    xs = pair[0][0]
    diff = yd - yg + 1


    for i in range(diff):
        if i > diff / 2:
            i = diff - i - 1

        for k in range(xs - i, xs + i + 1):
            if my_map[yg+move_y, k+move_x] == '.':
                #print(yg+move_y, k+move_x)
                my_map[yg+move_y, k+move_x] = '#'
        yg += 1



# for row in my_map:
#     print(''.join(np.asarray(row[0])[0]))

result = 0
for i in my_map[check,:].tolist()[0]:
    if i =='#': result+=1

result2 =''

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)