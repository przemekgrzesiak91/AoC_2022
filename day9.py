import numpy as np
import pandas as pd

day = '9'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()



print(data)
h = [0,0]
t = [0,0]
t_history = set()

for command in data:
    dir, value = command.split(' ')

    for i in range(1,int(value)+1):
        #Head moves
        if dir == 'R': h[0] += 1
        elif dir == 'L': h[0] -= 1
        elif dir == 'U': h[1] += 1
        elif dir == 'D': h[1] -= 1

        #Tail
        if abs(h[0]-t[0]) == 2:
            t[0]= t[0] + 1 if dir == 'R' else t[0] - 1

            if abs(t[1]-h[1]) == 1:
                t[1] = h[1]

        elif abs(h[1]-t[1]) == 2:
            t[1]= t[1] + 1 if dir == 'U' else t[1] - 1

            if abs(t[0] - h[0]) == 1: t[0] = h[0]

        #print(h,'---',t, dir)
        t_history.add(tuple(t))

all = {0: [0,0], 1: [0,0], 2: [0,0], 3: [0,0], 4: [0,0], 5: [0,0],
       6: [0,0], 7: [0,0], 8: [0,0], 9: [0,0]}
t_history2 = set()

for command in data:
    dir, value = command.split(' ')
    visual = np.chararray([35, 35])
    visual[:] = ''

    for j in range(1,int(value)+1):
        print('>>>>>>>>>>>>>>>>>',command)
        for i in range(0,9):
            #Head moves
            if i==0:
                if dir == 'R': all[i][0] += 1
                elif dir == 'L': all[i][0] -= 1
                elif dir == 'U': all[i][1] += 1
                elif dir == 'D': all[i][1] -= 1
            print(i, all[i], i + 1, all[i + 1])

            #Tail
            x = all[i][0]-all[i+1][0]
            y = all[i][1]-all[i+1][1]
            if abs(x) >= 2:
                all[i+1][0]= all[i+1][0] + x - 1

                y = all[i+1][1]-all[i][1]
                if abs(y) == 1:
                    all[i+1][1] = all[i][1]
                elif abs(y) > 1:
                    all[i + 1][1] = all[i][1] + y

            elif abs(y) >= 2:
                all[i+1][1] = all[i+1][1] + y - 1

                x = all[i+1][0] - all[i][0]
                if abs(x) == 1:
                    all[i+1][0] = all[i][0]
                elif abs(x) > 1:
                    all[i + 1][0] = all[i][0] + x

            #print(h,'---',t, dir)
            if i==8:
                # if tuple(all[i+1]) not in t_history2:
                #     pass
                #     print(all[i],all[i+1])
                t_history2.add(tuple(all[i+1]))



result = (len(t_history))

result2 = (len(t_history2))
print(sorted(t_history2))
print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)

#funkcja jak  H - T tylko dla H -1, 1-2 loop !
