from itertools import zip_longest
day = '13'

data = []
with open('data\day'+day+'.txt', 'r') as f:
    for line in f.readlines():
        if len(line)>1:
            data.append(eval(line.strip()))

def compare(L,R):
    z = zip_longest(L, R, fillvalue=None)

    for p in z:
        l, r = p
        res = None

        if isinstance(l, int) and isinstance(r, int):
            if l < r: return True
            elif l > r: return False

        elif type(l)==list and type(r)==list:
            res = compare(l, r)

        elif type(l)==int and type(r)==list:
            res = compare([l], r)
        elif type(l)==list and type(r)==int:
            res = compare(l, [r])

        elif l == None: return True
        elif r == None: return False

        if res != None: return res

result = 0
for id,i in enumerate(range(0,len(data),2),start=1):
    L = data[i]
    R = data[i+1]

    result += id if compare(L,R) > 0 else 0

#Part2
'''Compare [[2]] and  [[6]] with all pairs to get thiers index'''
result2 = 0
pos_two = 1
pos_six = 2

for id,i in enumerate(range(0,len(data))):
    L = data[i]
    pos_two += 1 if compare(L,[[2]]) > 0 else 0
    pos_six += 1 if compare(L,[[6]]) > 0 else 0

result2 = pos_two*pos_six


print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)