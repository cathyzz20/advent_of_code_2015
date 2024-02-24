#part1
with open('input_text_6.txt', 'r') as file:
    instructions = file.read().split('\n')
    instructions=[i.split(' ') for i in instructions]
file.close()
import numpy as np
grid = np.zeros((1000, 1000), 'int32')
for i in instructions:
    if i[0] == 'turn':
        x1, y1 = i[2].split(',')
        x2, y2 = i[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if i[1] == 'on':
            grid[x1:x2+1, y1:y2+1] = 1
        elif i[1] == 'off':
            grid[x1:x2+1, y1:y2+1] = 0
    elif i[0] == 'toggle':
        x1, y1 = i[1].split(',')
        x2, y2 = i[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] = np.logical_not(grid[x1:x2+1, y1:y2+1])
print(np.sum(grid))
#part2
import numpy as np
data = open('input_text_6.txt.txt').read().splitlines()
data = [i.split(' ') for i in data]
grid = np.zeros((1000, 1000), 'int32')
for i in data:
    if i[0] == 'turn':
        x1, y1 = i[2].split(',')
        x2, y2 = i[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if i[1] == 'on':
            grid[x1:x2+1, y1:y2+1] += 1
        elif i[1] == 'off':
            grid[x1:x2+1, y1:y2+1] -= 1
            grid[grid < 0] = 0
    elif i[0] == 'toggle':
        x1, y1 = i[1].split(',')
        x2, y2 = i[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] += 2
print(np.sum(grid))






