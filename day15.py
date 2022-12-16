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
print(max_x,min_x)
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




    # diff2 = yd - yg + 1
    #
    # for i in range(diff2):
    #     if i > diff2 / 2:
    #         i = diff2 - i - 1
    #
    #     for k in range(xs - i, xs + i + 1):
    #         if my_map[yg, k+move_x] == '.':
    #             #print(yg+move_y, k+move_x)
    #             my_map[yg, k+move_x] = '#'
    #     yg += 1



# for row in my_map:
#     print(''.join(np.asarray(row[0])[0]))


#print(look)
result = look.tolist().count('#')

if 'B' in look: print('ok')

result2 =''

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)