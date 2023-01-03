from collections import deque

#TO DO
#check 0 and 27 for S i E
#change grid to numpy array/matrix

day = '12'

with open('data\day'+day+'.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

max_x = len(grid)
max_y = len(grid[0])

letters = {chr(x): x - 96 for x in range(97,97+26)}
letters["S"] = 1
letters["E"] = 26 # dlaczego nie 0 i 27

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
starts = []
for i,row in enumerate(grid):
    for j,value in enumerate(row):
        if value == 'S':
            start = (i,j)

        if value == 'E':
            end = (i,j)

        if value == 'a':
           starts.append((i,j))

def bfs(start,end):
    queue = deque()
    queue.append([start])
    seen = set()

    while queue:
        path = queue.popleft()
        last = path[-1]

        if last not in seen:
            seen.add(last)

            if last == end:
                return (len(path) - 1)

            for dir in dirs:
                new_pos = tuple(sum(x) for x in zip(last, dir))

                if 0<=new_pos[0]<max_x and 0<=new_pos[1]<max_y:
                    h1 = letters[grid[last[0]][last[1]]]
                    h2 = letters[grid[new_pos[0]][new_pos[1]]]

                    if h2 <= h1 +1:
                        path_copy = path[:]
                        path_copy.append((new_pos))
                        queue.append(path_copy)

result = bfs(start,end)

#Part 2
result2 = []

for start in starts:
    value = bfs(start,end)
    if value is not None:
        result2.append(value)
print(result2)
result2 = min(result2)

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)