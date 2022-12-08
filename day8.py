import numpy as np

day = '8'

with open('data\day'+day+'.txt', 'r') as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = [int(x) for x in list(data[i])]

ndata = np.asarray(data)

visible = 0

n = len(data)
m = len(data[0])

scores =[]

result2 = 0

for i in range(n):
    for j in range(m):
        height = ndata[i,j]
        if i == 0 or j == 0 or i == n-1 or j == m-1 :
            visible += 1
        else:
            # print('>',height)
            # print('1:', ndata[i,j+1:] )
            # print('2:', ndata[i,0:j])
            # print('3:', ndata[0:i,j])
            # print('4:', ndata[i+1:,j])

            lines = [ndata[i,j+1:].tolist(), np.flip(ndata[i,0:j]).tolist(), np.flip(ndata[0:i,j]).tolist(), ndata[i+1:,j].tolist() ]

            if (lines[0] >= height).any() and (lines[1] >= height).any() and (lines[2] >= height).any() and (lines[3] >= height).any():pass
            else: visible += 1

            #print(lines)
            score = 1
            for line in lines:
                n_trees = 1
                for k in range(len(line)):
                    #print(height, line, k)
                    if line[k] < height and k != len(line)-1: n_trees += 1
                    else:
                        score *= n_trees
                        break
                #print('>>>', n_trees)

            scores.append(score)
            if score > result2: result2 = score
            #print('-----')

#print(scores)
result =  visible

print('˜”°•Day '+ day+'•°”˜')
print('Part 1:', result)
print('Part 2:', result2)