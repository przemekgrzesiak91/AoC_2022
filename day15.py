import numpy as np
import re

day = '15'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

pairs = []
x_list = []
y_list = []

for row in data:
    xs,ys,xb,yb = [int(x) for x in re.findall('-?\d+',row)]
    x_list.append(xs)
    x_list.append(xb)
    y_list.append(ys)
    y_list.append(yb)

    pairs.append([(xs,ys),(xb,yb)])

xmin,xmax = min(x_list),max(x_list)
ymin,ymax = min(y_list),max(y_list)
print(ymax,ymin,xmax,xmin)

my_map = np.matrix([['.']*(xmax-xmin+2)]*(ymax-ymin+2))
print(my_map.shape)

for pair in pairs:
    xs,ys,xb,yb = pair[0][0]-xmin,pair[0][1]-ymin,pair[1][0]-xmin,pair[1][1]-ymin
    print(xs,ys,xb,yb)
    my_map[ys,xs] = 'S'
    my_map[yb,xb] = 'B'

for row in my_map:
    print(''.join(np.asarray(row[0])[0]))



result = ''
result2 =''

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)

