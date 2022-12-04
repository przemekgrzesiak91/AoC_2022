day = '4'

with open('data/day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

overlaps = 0
overlaps2 = 0
for row in data:
    x1,y1,x2,y2 = [int(x) for x in row.replace('-',',').split(',')]

    a = set(range(x1, y1+1))
    b = set(range(x2, y2+1))

    if a.issubset(b) or a.issuperset(b):
        overlaps += 1
    if a.intersection(b):
        overlaps2 += 1

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', overlaps)
print('Part 2:', overlaps2)