import re

day = '21'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()


#Part1

monkeys = {}


while data:
    for monkey in data:
        #print(data)
        name, value = monkey.split(': ')
        if value.isdigit():
            monkeys[name] = value
            data.remove(monkey)
        else:
            name1,symbol,name2 = value.split(' ')
            if name1 in monkeys.keys() and name2 in monkeys.keys():
                #print(name, str(eval(monkeys[name1]+symbol+monkeys[name2])))
                monkeys[name] = str(eval(monkeys[name1]+symbol+monkeys[name2]))
                data.remove(monkey)

result = monkeys['root']

#Part 2
with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()
monkeys = {}

while data:
    for monkey in data:
        #print(data)
        name, value = monkey.split(': ')
        if value.isdigit():
            if name != 'humn':
                monkeys[name] = '('+value+')'
            else:
                monkeys[name] = 'X'
            data.remove(monkey)
        else:
            name1,symbol,name2 = value.split(' ')
            if name1 in monkeys.keys() and name2 in monkeys.keys():
                if name == 'root':
                    symbol = '='
                    #print(monkeys[name1], monkeys[name2])
                #print(name, str(eval(monkeys[name1]+symbol+monkeys[name2])))
                try:
                    print(str(eval(monkeys[name1]+symbol+monkeys[name2])))
                    print((monkeys[name1]+symbol+monkeys[name2]))
                    monkeys[name] = str('('+str(eval(monkeys[name1]+symbol+monkeys[name2]))+ ')')

                except:
                    monkeys[name] = str('('+monkeys[name1]+symbol+monkeys[name2]+')')
                data.remove(monkey)


symbols_convert = {'+': '-',
                   '*': '/',
                   '-': '+',
                   '/': '*'}

L, R = monkeys['root'].split('=')
R = R[:-1]
L = L[1:]
n = L.count('(')
print(L)

while L:
    L = L[1:-1]
    #print(L)
    nl = 0
    nr = 0
    for i in range(len(L)):
        if L[i] == '(': nl += 1
        elif L[i] == ')': nr += 1

        if nl == nr:
            if 'X' in L[:i + 1]:
                new = L[i+1:]
                L = L[:i + 1]
            else:
                new = L[:i + 2]
                L = L[i+2:]
            value = (re.findall(r'\d+',new)[0])
            symbol = (re.findall(r'[\+\-\*\/]',new)[0])
            symbol = symbols_convert[symbol]
            print(value,symbol)
            R = '('+R+symbol+value+')'


            print(L,'<><>', new)
            break
print(eval(R))

result2= eval(R)

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', int(result2))

# modyfikacja nazw w słowniku