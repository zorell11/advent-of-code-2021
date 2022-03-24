with open('input', 'r') as f:
    data = f.read().splitlines()

data = [[ int(i) for i in line ] for line in data ]

checked = set()
q = set() #queue
basin = []
for l in range(len(data)):
    for c in range(len(data[l])):
        if data[l][c] == 9 or (l,c) in checked:
            checked.add((l,c))
            continue
        q.add((l,c))
        counter = 0
        while q:
            l,c = q.pop()
            checked.add((l,c))
            counter += 1
            for i,j in (l-1,c), (l, c-1), (l+1, c), (l, c+1):
                if (i,j) in checked:
                    continue
                if 0<=i<len(data) and 0<=j<len(data[l]):
                    if data[i][j]!=9:
                        q.add((i,j))
        basin.append(counter)

basin.sort()
print('{}'.format(basin[-1] * basin[-2] * basin[-3]))