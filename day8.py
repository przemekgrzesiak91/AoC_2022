import re
import copy

day = '8'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = [int(x) for x in list(data[i])]

visible = 0

n = len(data)
m = len(data[0])

for i in range(n):
    for j in range(m):
        height = data[i][j]
        if i == 0 or j == 0 or i == n-1 or j == m-1 :
           visible += 1

        elif data[i-1][j] < height or data[i+1][j] < height or data[i][j-1] < height or data[i][j+1] <= height:
            for ix in range(n):
                if ix == i:continue
                if data[i][ix] >= height: break
            for jx in range(m):
                if jx == j:continue
                if data[jx][j] >= height: break
            print(i,j,'dd',height)
            visible += 1

print(visible)

result = ''

result2 = ''
print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)

# modyfikacja nazw w słowniku