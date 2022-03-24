with open('example', 'r') as f:
    data = f.read()

data = list(map(int, data.split(',')))


med = sorted(data)[len(data)//2]
sol = 0
for i in data:
    n = abs(i-med)
    sol += (n*(n+1)/2) 

print(sorted(data))
print(sol)