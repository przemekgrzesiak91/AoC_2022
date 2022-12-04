day = '2'

with open('data/day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

shape_point = {'X':1,'Y':2,'Z':3,}
change_shape = {'X': {'A':'Z', 'B':'X', 'C':'Y'},
                'Y': {'A':'X', 'B':'Y', 'C':'Z'},
                'Z': {'A':'Y', 'B':'Z', 'C':'X'}
                }

def count_point(a,b):
    if a=='A' and b=='X' or a=='B' and b=='Y' or a=='C' and b=='Z':
        return 3
    elif a=='A' and b=='Y' or a=='B' and b=='Z' or a=='C' and b=='X':
        return 6
    else:
        return 0

result = 0
result2 = 0

for row in data:
    a,b = row.split(' ')
    result += shape_point[b] + count_point(a,b)

    new_b = change_shape[b][a]
    result2 += shape_point[new_b] + count_point(a, new_b)


print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)