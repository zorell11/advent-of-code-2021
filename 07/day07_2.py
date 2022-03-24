with open('input', 'r') as f:
    data = f.read()

data = list(map(int, data.split(',')))

ave1 = round(sum(data)/len(data))
ave2 = sum(data)//len(data)

q = lambda x: x * (x+1)//2

sol = float('inf')
for ave in ave1, ave2:
    soll = sum([q(abs(i-ave)) for i in data])
    sol = min(sol, soll)

print(sol)