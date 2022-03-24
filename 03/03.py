with open('input', 'r') as file:
    data = file.read().splitlines()

a = zip(*data)

gamma_rate = ''
epsilon_rate = ''
for i in a:
    if i.count('0') > (len(i)//2):
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'


print(int(gamma_rate,2))
print(int(epsilon_rate,2))
print(int(gamma_rate,2) * int(epsilon_rate,2))



z = list(map(list, zip(*data)))
i = ("".join(max(k, key = k.count) for k in z))
j = ("".join(min(k, key = k.count) for k in z))
print(int(i, 2) * int(j, 2))

def count_column(data, bit):
    z = zip(*data)
    if i.count('1')>= i.count('0'):
        oxygen.append('1')
        co2.append('0')
    else:
        oxygen.append('0')
        co2.append('1')

i = 0
while len(data)!= 1 or (set(data)==1):
    bit = count_column(data,i)

