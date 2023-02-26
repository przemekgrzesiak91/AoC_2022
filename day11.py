import re
from math import lcm, prod

day = '11'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

def create_dic(data):
    monkeys = {}
    for row in data:
        if 'Monkey' in row:
            num = int(re.findall(r'\d',row)[0])
            monkeys[num] = [[],'','',0,0,0]
        elif 'item' in row:
            monkeys[num][0] = [int(x) for x in (re.findall('\d+',row))]
        elif 'Operation' in row:
            monkeys[num][1] = row.split('= ')[1]
        elif 'Test' in row:
            monkeys[num][2] = int(re.findall('\d+',row)[0])
        elif 'true' in row:
            monkeys[num][3] = int(re.findall('\d+',row)[0])
        elif 'false' in row:
            monkeys[num][4] = int(re.findall('\d+',row)[0])
    return monkeys

def play(rounds,part):
    lcm_divs = lcm(*divs)

    for i in range(rounds):
        #print('---------Round ',i+1)
        for key in monkeys.keys():
            while monkeys[key][0]:
                monkeys[key][5] += 1
                old = monkeys[key][0].pop(0)
                new = eval(monkeys[key][1]) % lcm_divs
                if part == 1:
                    new //= 3

                if new % monkeys[key][2] == 0:
                    monkeys[monkeys[key][3]][0].append(new)
                else:
                    monkeys[monkeys[key][4]][0].append(new)

def count(monkeys):
    num_of_inspections = []
    for key in monkeys.keys():
        num_of_inspections.append(monkeys[key][5])

    num_of_inspections = sorted(num_of_inspections, reverse=True)
    #print(num_of_inspections)
    result = num_of_inspections[0] * num_of_inspections[1]
    return result

divs = []
# Part 1
monkeys = create_dic(data)
for key in monkeys.keys():
    divs.append(monkeys[key][2])

play(20,1)
num_of_inspections = []
result = count(monkeys)

# Part 2
monkeys = create_dic(data)
play(10000,2)
num_of_inspections = []
result2 = count(monkeys)

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)

