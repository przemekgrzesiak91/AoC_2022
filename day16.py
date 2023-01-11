from collections import deque
import re

day = '16'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

pipes = dict()
TIME_LIMIT = 30

for row in data:
    value = re.findall(r'\d+',row)
    valves = re.findall(r'[A-Z]{2}',row)
    pipes[valves[0]] = [int(value[0]), list(valves[1:])]
print(pipes,'\n')

queue=deque([(0,(),"AA",0)])
visited=set()
result = 0

while queue:
    min,opened,current,pressure=queue.popleft()

    if min==TIME_LIMIT:
        result=max(result,pressure)
        continue
    if (opened,current) in visited:
        continue
    visited.add((opened,current))

    pressure_add = pressure
    for valve in opened:
        pressure_add += pipes[valve][0]
    if pipes[current][0]!=0:
        if current not in opened:
            queue.append((min+1,tuple(list(opened)+[current]),current,pressure_add))

    for valve in pipes[current][1]:
        queue.append((min+1,opened,valve,pressure_add))
#PART2
TIME_LIMIT = 26
result2 = ''

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)
