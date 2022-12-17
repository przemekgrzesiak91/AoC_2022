import re
import copy

day = '7'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()


structure = {'/':0}
path='/'

for cmd in data:
    if '$' in cmd:
        if '/' in cmd:
            path = '/'
        elif 'ls' in cmd:
            pass
        elif '..' in cmd:
            path = path[0:path.rfind('/')]
        else:
            dirname = cmd.split(' ')[2]
            path = path+'/'+dirname
            structure[path] = 0
    elif 'dir' in cmd:
        pass
    else:
        size = int(cmd.split(' ')[0])

        dir = path
        for i in range(dir.count('/')):
            structure[dir] += size
            dir = dir[0:dir.rfind('/')]



result = sum([x for x in structure.values() if x <= 100000])

max_size = structure['/']
to_delete =  30000000-(70000000 - max_size)


result2 = min([x for x in structure.values() if x >= to_delete])

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)

# modyfikacja nazw w słowniku