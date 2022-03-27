with open('input', 'r') as f:
    data1, data2 = f.read().split("\n\n")


dotts = set()
for line in data1.splitlines():
    x,y = map(int, line.split(','))
    dotts.add((x,y))

for line in data2.splitlines()[:1]:
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
    
print(len(dotts))