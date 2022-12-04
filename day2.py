with open('data/day2.txt', 'r') as f:
    data = f.read().splitlines()

# A X rock
# B Y paper
# C Z scic

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



# day 2.1
sum = 0
sum2 = 0

for row in data:
    a,b = row.split(' ')
    sum += shape_point[b] + count_point(a,b)

    new_b = change_shape[b][a]

    sum2 += shape_point[new_b] + count_point(a, new_b)


print(sum)
print(sum2)