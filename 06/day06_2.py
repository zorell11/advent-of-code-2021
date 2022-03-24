with open('input', 'r') as f:
    data = f.read()

data = list(map(int, data.split(',')))


data1 = [0]*9
for i in data:
    data1[i]+=1


for day in range(256):
    data2 = [0]*9
    for i,j in enumerate(data1):
        if i==0:
            data2[6]+=j
            data2[8]+=j
        else:
            data2[i-1]+=j

    data1=data2
print(data1)
print(sum(data1))