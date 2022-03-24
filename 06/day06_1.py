with open('example', 'r') as f:
    data = f.read()

data = list(map(int, data.split(',')))


for i in range(80):
    new = 0
    for index,number in enumerate(data):
        if number == 0:
            data[index] = 6
            new +=1
        else:
            data[index]-=1
    data.extend(new*[8])

print(len(data))
