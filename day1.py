with open('data\day1.txt','r') as f:
    data = f.readlines()
i = 0
result = [0]

for line in data:
    if line == '\n':
        i += 1
        result.append(0)

    else:
        result[i] += int(line.strip())

print(max(result))
result = sorted(result)[::-1]
final = sum(result[0:3])
print (final)