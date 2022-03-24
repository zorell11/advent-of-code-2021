with open('input', 'r') as f:
    data = f.read().split('\n\n')


nums = list(map(int,data[0].split(',')))

boards = []
for k in data[1:]:
    boards.append([])
    for j in k.splitlines():
        boards[-1].append(list(map(int, j.split())))

boards1 = boards[:]

for num in nums:
    for board in boards:
        for row in board:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = 0
            
        if any(all(x == 0 for x in row) for row in board) or any(all(row[i] == 0 for row in board) for i in range(len(board[0]))):                                                
            if len(boards1) == 1:
                a = sum([i or 0 for row in board for i in row]) * num
                print(a) 
                exit(0)
            for i in range(len(board[0])):
                    for row in board:
                        row[i]=None  
            try:
                boards1.pop(boards1.index(board))
            except ValueError:
                pass


                




            

