with open('input', 'r') as f:
    data = f.read().splitlines()

board = [ list(map(int,i)) for i in data]

checked = [[0]*len(i)  for i in data]

queue = [(0, 0, 0, checked)]
run = 0
while True:
    queue.sort(key=lambda x:x[0])
    value, x, y, checked = queue.pop(0)
    if checked[x][y]:
        continue
    if (x,y) == (len(board)-1, len(board[x])-1):
        print(value)
        break

    checked[x][y] = 1
    for x1,y1 in (x-1, y), (x, y+1), (x+1, y), (x, y-1):
        if not (0<=x1<len(board) and 0<=y1<len(board[0])):
            continue
        
        if checked[x1][y1]:
            continue
        
        queue.append((value+board[x1][y1], x1, y1, checked))