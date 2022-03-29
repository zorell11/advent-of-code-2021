with open('input', 'r') as f:
    template, rules1 = f.read().split('\n\n')

s= template
rules = {}
for line in rules1.splitlines():
    a, b = line.split(' -> ')
    rules[a] = b

new_template = list(template)

for run in range(10):
    index = 1
    for i in range(0, len(template)-1):
        new_template.insert(index, rules[template[i]+template[i+1]])
        index += 2
    template = new_template[::]

sol = {}
for i in new_template:
    if i in sol:
        sol[i]+=1
    else:
        sol[i]=1 

print(max(sol.values()) - min(sol.values()))