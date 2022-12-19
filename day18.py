day = '18'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

data = [tuple(map(int, cube.split(','))) for cube in data]

total = len(data) * 6
print(total)

for cube in data:
    if (cube[0] + 1, cube[1], cube[2]) in data: total -= 1
    if (cube[0] - 1, cube[1], cube[2]) in data: total -= 1
    if (cube[0], cube[1] + 1, cube[2]) in data: total -= 1
    if (cube[0], cube[1] - 1, cube[2]) in data: total -= 1
    if (cube[0], cube[1], cube[2] + 1) in data: total -= 1
    if (cube[0], cube[1], cube[2] - 1) in data: total -= 1


result = total
result2 = ''

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)