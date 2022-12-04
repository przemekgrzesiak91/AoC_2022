import string
day = '3'

with open('data/day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority = list(range(1,53))

def check(a,b,c=''):
    if c != '':
        letter = (list(set(a).intersection(b,c)))
    else:
        letter = (list(set(a).intersection(b)))

    return dic[letter[0]]

dic = {}
for key in alphabet:
    for p in priority:
        dic[key] = p
        priority.remove(p)
        break

result = 0
for row in data:
    n = int(len(row)/2)
    result += check(row[0:n],row[n:])

result2 = 0
for i in range(0,len(data),3):
    result2 += check(data[i], data[i+1], data[i+2])

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)
