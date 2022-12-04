day = '1'

with open('data/day'+day+'.txt', 'r') as f:
    data = f.readlines()
i = 0
result = [0]

for line in data:
    if line == '\n':
        i += 1
        result.append(0)

    else:
        result[i] += int(line.strip())

result = sorted(result)[::-1]
final = sum(result[0:3])

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', max(result))
print('Part 2:', final)