with open('input', 'r') as f:
    data = f.read().splitlines()


diagram = {}


for row in data:
    i,j = row.split(' -> ')
    x1,y1 = map(int, i.split(','))
    x2,y2 = map(int, j.split(','))

    dx = x2-x1
    dy = y2-y1

    if dx:
        dx = dx //abs(dx)
    if dy:
        dy = dy // abs(dy)
    x,y = x1,y1
    while True:
        diagram[(x,y)] = diagram.get((x,y),0) +1
        if x==x2 and y==y2:
            break
        x+=dx   
        y+=dy

sol = 0
for i in diagram.values():
    if i>1:
        sol+=1

print(sol)
    