import numpy as np

day = '10'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

x_value = 1
cycle = 0
cycles = [20,60,100,140,180,220]
signal_strength = []

sprite_position = list('###.....................................')
current_CRT = ''
CRT = []

def check_cycle(cycle, x_value):
    if cycle in cycles:
        signal_strength.append(x_value*cycle)

def check_sprite(cycle, x_value, sprite_position, current_CRT):
    if cycle % 40 == 1:
        print('>>',len(current_CRT))
        CRT.append(current_CRT)
        current_CRT = ''
        sprite_position = list('###.....................................')

    pos = 39 if cycle == 40 else cycle%40-1
    if sprite_position[pos] == '#':
        current_CRT += '#'
    else: current_CRT += '.'
    #print(cycle, ''.join(sprite_position)   ,'\n>', current_CRT)


    return current_CRT



for row in data:
    if 'noop' in row:
        cycle += 1
        check_cycle(cycle,x_value)
        current_CRT = check_sprite(cycle,x_value,sprite_position,current_CRT)

    else:
        for i in range(2):
            cycle += 1
            check_cycle(cycle,x_value)
            current_CRT = check_sprite(cycle,x_value, sprite_position, current_CRT)

        x_value += int(row.split(' ')[1])
        sprite_position = []
        for i in range(40):
            if i in (x_value-1,x_value,x_value+1): sprite_position.append('#')
            else: sprite_position.append('.')

CRT.append(current_CRT)

print(signal_strength)
result = sum(signal_strength)

def result2():
    for i in CRT:
        if i=='': continue
        print(i.replace('.',' '))


print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:')
result2()
