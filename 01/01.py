with open('input', 'r') as file:
    depths = file.read().split('\n')
    data  = [int(x) for x in depths]

def task1(data):
    increase = 0
    for i in range(0, len(data)-1):
        if data[i] < data[i+1]:
            increase += 1
    print('task1:', increase)


def task2(data):
    increase = 0
    new_data = []
    for i in range(len(data)-2):
        new_data.append(sum(data[i:i+3]))
        if i>0:
            if new_data[i] > new_data[i-1]:
                increase += 1
    print('task2:', increase)

task1(data)
task2(data)


#q = [*map(int, depths)]
#task1 = sum([ y>x for x,y in zip(q,q[1:])])
#print(task1)
#t2 = [ x+y+z for x,y,z in zip(q,q[1:],q[2:])]
#print(sum([y>x for x,y in zip(t2, t2[1:])]))