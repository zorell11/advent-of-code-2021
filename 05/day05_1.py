with open('input', 'r') as f:
    data = f.read().splitlines()

col, row = 1000, 1000
diagram = [[ 0 for i in range(col)] for j in range(row)]

for row in data:
    i,j = row.split(' -> ')
    x1, y1 = map(int, i.split(','))
    x2, y2 = map(int, j.split(','))

    if x1==x2 or y1==y2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            for x in range(min(x1,x2), max(x1,x2)+1):
                diagram[y][x]+=1

sol = 0
for row in diagram:
    for i in row:
        if i>1:
            sol +=1
print(sol)
    



