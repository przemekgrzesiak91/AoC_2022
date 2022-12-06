day = '6'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

print(data)

for c in range(len(data[0])-3):
    if len(set(data[0][c:c+4])) == 4:
        result = c+4
        break


for c in range(len(data[0])-13):
    if len(set(data[0][c:c+14])) == 14:
        result2 = c+14
        break


print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)