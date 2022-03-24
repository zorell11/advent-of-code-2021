with open('input', 'r') as f:
    data1 =  f.read().split()

data = []
for i in data1:
    data.append(list(map(int, i)))


light = 0
stack = []

def index(x, y, light):
    if (x,y) not in checked:
        data[x][y] += 1
    if data[x][y] == 10:
        light += 1
        data[x][y] = 0
        stack.append((x,y))
        checked.append((x,y))
    return light


for run in range(1,1000):
    checked = []
    for l in range(len(data)):
        for c in range(len(data[l])):
            light = index(l, c, light)
            while stack:
                x,y = stack.pop()
                for i,j in (x-1, y-1), (x-1,y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1):
                    if 0<=i<len(data) and 0<=j<len(data[l]):
                        light = index(i, j, light)

    for i in data:
        if set(i) != {0}:
            break
    else:
        print(run)
        break