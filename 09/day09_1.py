with open('input', 'r') as f:
    data = f.read()

data1 = []
for line in data.splitlines():
    data1.append(list(map(int,line)))
    
sum_low_points = 0
for line in range(len(data1)):
    for column in range(len(data1[0])):
        
        v = []
        for i,j in (line-1, column), (line, column+1), (line+1, column), (line, column-1):
            if 0<=i<len(data1) and 0<=j<len(data1[0]):
                v.append(data1[i][j])
        if data1[line][column] < min(v):
            sum_low_points += data1[line][column] + 1
            
print(sum_low_points)
            