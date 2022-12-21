day = '18'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

data = [tuple(map(int, cube.split(','))) for cube in data]

total = len(data) * 6

empty = []
visited = []
max_x, max_y, max_z = [max(data, key=lambda x: x[i])[i] + 1 for i in range(3)]

result = 0
result2 = 0

neighbours = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

def check(pos):
    for new_pos in neighbours:
        neighbour = tuple(sum(x) for x in zip(pos,new_pos))
        if neighbour not in data:
            return 0
    empty.append(pos)

for cube in data:
    for new_pos  in neighbours:
        neighbour = tuple(sum(x) for x in zip(cube, new_pos))
        if neighbour in data: total -= 1
        else:
            if neighbour not in visited:
                check(neighbour)
        visited.append(neighbour)

visited = []
print((max_x, max_y, max_z))
queue = {(max_x, max_y, max_z)}
total2 = 0

while queue:
    pos = queue.pop()
    #print(pos)
    visited.append(pos)

    for new_pos in neighbours:
        neighbour = (tuple(sum(x) for x in zip(pos, new_pos)))
        if neighbour in data:
            #print(pos, neighbour)
            total2 += 1
        elif neighbour not in visited:
            if -2 in neighbour or max_z+2 in neighbour:
                continue
            queue.add(neighbour)



result = total
result2 = total2

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)
