with open('input', 'r') as f:
    data1, data2 = f.read().split("\n\n")


dotts = set()
for line in data1.splitlines():
    x,y = map(int, line.split(','))
    dotts.add((x,y))

for line in data2.splitlines():
    direction, num = line.strip('fold along ').split('=')
    num = int(num)
    dott = set()
    if direction == 'y':
        for x,y in dotts:
            if y>num:
                y = num*2-y 
            dott.add((x,y))

    else:
        for x,y in dotts:
            if x>num:
                x = num*2-x
            dott.add((x,y))
    dotts = dott     
    

xm = max( i[0] for i in dotts)
ym = max( i[1] for i in dotts)

board = []
for i in range(ym+1):
    board.append( [' ']* (xm+1))

for x,y in dotts:
    board[y][x] = 'X'

for i in board:
    print("".join(i))
