with open('input', 'r') as file:
    data = file.read().splitlines()



data1=data[:]
lenght = len(data[0])
def count_column(data, index):
    z = list(map(list, zip(*data)))
    if z[index].count('1') < z[index].count('0'):
        return '0'
    return '1'

def count_column1(data, index):
    z = list(map(list, zip(*data)))
    if z[index].count('1')>= z[index].count('0'):
        return '0'
    return '1'

def mod_data(data, bit, index):
    new_data = []
    for i in data:
        if i[index]== bit:
            new_data.append(i)
    return new_data


i = 0
condition = True
while condition:
    if len(data)==1 or (len(set(data))==1) or (i>lenght):
        oxygen = int(data[0],2)
        print(oxygen)
        break
    bit = count_column(data,i)
    
    data = mod_data(data, bit, i)

    i += 1

i = 0
while condition:
    if len(data1)==1 or (len(set(data1))==1) or (i>lenght):
        co2 = int(data1[0],2)
        print(co2)
        break
    bit = count_column1(data1,i)    
    data1 = mod_data(data1, bit, i)
    i += 1

print(oxygen * co2)