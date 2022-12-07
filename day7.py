import re
import copy

day = '7'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

structure = {}

current = '/'

for row in data:
    row = row.split(' ')

    if 'cd' in row:
        dirname = row[-1]
        if dirname == '..':
            current = structure[current][1]
        else:
            structure[dirname] = [[],current,[]]
            current = dirname

    if row[0] == 'dir':
        structure[dirname][2].append(row[1])
    if row[0].isnumeric():
        structure[dirname][0].append(int(row[0]))

print(structure)

totals = []

def sum_files(dirname):
    dirnames = [dirname]
    total = 0

    while dirnames != []:

        current = dirnames.pop(0)
        total += sum(structure[current][0])

        dirnames += structure[current][2]
        print(dirnames)
    return total

sums = []

for key, value in structure.items():
    #print(key)
    sums.append(sum_files(key))

result = sum([x*1 for x in sums if x <= 100000])

result2 = ''
print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)

# modyfikacja nazw w słowniku