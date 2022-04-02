import heapq

with open('input', 'r') as f:
    data = f.read().splitlines()

board = [ list(map(int,i)) for i in data]

new_board = []
for line in board:
    new_line = []
    for j in range(5):
        a = list(map(lambda x: (x+j if x+j<10 else (x+j)%9), line))
        new_line += a
    new_board.append(new_line)

board = new_board[:]
for i in range(1,5):
    for line in board:
        new_board.append([ j+i if j+i<10 else (j+i)%9 for j in line])

checked = [[0]*len(i)  for i in new_board]

queue = [(0, 0, 0, checked)]
while True:
    #queue.sort(key=lambda x:x[0])
    #value, x, y, checked = queue.pop(0)
    value, x, y, checked = heapq.heappop(queue)
    if checked[x][y]:
        continue
    if (x,y) == (len(new_board)-1, len(new_board[x])-1):
        print(value)
        break

    checked[x][y] = 1
    for x1,y1 in (x-1, y), (x, y+1), (x+1, y), (x, y-1):
        if not (0<=x1<len(new_board) and 0<=y1<len(new_board[0])):
            continue
        
        if checked[x1][y1]:
            continue
        
        #queue.append((value+new_board[x1][y1], x1, y1, checked))
        heapq.heappush(queue, (value+new_board[x1][y1], x1, y1, checked))