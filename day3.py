import string

with open('data/day3.txt', 'r') as f:
    data = f.read().splitlines()

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority = list(range(1,53))

dic = {}
for key in alphabet:
    for p in priority:
        dic[key] = p
        priority.remove(p)
        break

result = 0
for row in data:
    n = int(len(row)/2)
    a,b = row[0:n], row[n:]
    letter = (list(set(a).intersection(b)))
    result += dic[letter[0]]

print(result)
result2 = 0
for i in range(0,len(data),3):
    letter = list(set(data[i]).intersection(data[i+1]).intersection(data[i+2]))
    result2 += dic[letter[0]]

print(result2)