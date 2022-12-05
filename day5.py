import re
import copy

day = '5'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

id_break = data.index('')
stacks_dic = {}
stacks,instructions = data[0:id_break],data[id_break+1:]

for num in stacks[-1].replace(' ',''):
    stacks_dic[int(num)] = []

for row in stacks[-2::-1]:
    i = 1
    for num in range(1,len(row),4):
        if row[num] != ' ':
            stacks_dic[i].append(row[num])
        i+=1

def move_crates(instructions, stacks_func, part):
    stacks_func = copy.deepcopy(stacks_func)

    for instruction in instructions:

        taken = []
        n,x,y = [int(x) for x in re.findall(r'\d+', instruction)]

        for n0 in range(n):
            taken.append(stacks_func[x].pop(-1))

        if part == 1:
            stacks_func[y] += taken
        elif part == 2:
            stacks_func[y] += taken[::-1]


    return stacks_func

stacks_dic1 = move_crates(instructions,stacks_dic,1)
result = ''
for key,value in stacks_dic1.items():
    result += value[-1]


stacks_dic2 = move_crates(instructions,stacks_dic,2)
result2 = ''
for key,value in stacks_dic2.items():
    result2 += value[-1]



print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)