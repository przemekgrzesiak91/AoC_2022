import numpy as np

day = '14'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

print(data)

min_X, min_Y, max_X, max_Y = 500,500,0,0

for row in data:
    row = row.split(' -> ')
    for corr in row:
        x,y = [int(value) for value in corr.split(',')]
        if x> max_X: max_X = x
        elif x< min_X: min_X = x

        if y > max_Y: max_Y = y
        elif y < min_Y: min_Y = y

print(min_X, min_Y, max_X, max_Y)

rocks = np.array([[('.')]*(max_X-min_X+1)]*(max_Y+2))

for row in data:
     row = row.split(' -> ')
     x,y = 0,0
     for corr in row:
         if x==0 and y==0:
             x, y = [int(value) for value in corr.split(',')]
             x -= min_X

         else:
             new_x,new_y =  [int(value) for value in corr.split(',')]
             new_x -= min_X

             if x == new_x:
                 if y<new_y:
                     rocks[y:new_y+1,x] = '#'
                 else:
                     rocks[new_y:y+1,x] = '#'
             if y == new_y:
                 if x < new_x:
                     rocks[y,x:new_x+1] = '#'
                 else:
                     rocks[y,new_x:x+1] = '#'
             x, y = new_x, new_y
start = 500-min_X
rocks[0,start] = '+'

def sand(rocks,i,j=0):
    for j in range(j,max_Y):
        if rocks[j+1,i] in ("o", "#"):
            if rocks[j+1, i-1] == ".":
                if i-1>=0:
                    return sand(rocks,i-1,j)
                else:
                    return False

            elif rocks[j+1,i+1] == ".":
                if i<=min_X:
                    return sand(rocks, i+1,j)
                else:
                    return False

            else:
                if j==0 and i==start: return False
                rocks[j,i] = "o"
                return True
            break

n = 0
a = True
while a:
    n+=1
    a = sand(rocks,start)
result = n-1

for row in rocks:
    print(''.join(row))

#Part 2

lcol = max_Y+4 - start
rcol = max_Y+4 - ((max_X-min_X+1) - start)

rocks2 = np.pad(rocks,((0,2),(lcol,rcol)), mode='constant', constant_values= '.')
rocks2[max_Y + 2, 0:] = '#'

a = True
start = max_Y+4
max_Y = rocks2.shape[1]
while a:
    n+=1
    a = sand(rocks2, start)
result2 = n - 1

# for row in rocks2:
#     print(''.join(row))

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)