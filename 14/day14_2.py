with open('input', 'r') as f:
    data1, data2 = f.read().split('\n\n')

last = data1[-1]
rules = {}
for line in data2.splitlines():
    a, b = line.split(' -> ')
    rules[a] = b

template = {}
for x,y in zip(data1, data1[1:]):
    if str(x+y) not in template:
        template[str(x+y)] = 0
    template[str(x+y)] += 1

for _ in range(40):
    new_template = {}
    for i in template:
        if i[0]+rules[i] not in new_template:
            new_template[i[0]+rules[i]] = 0
        if rules[i]+i[1] not in new_template:
            new_template[rules[i]+i[1]] = 0
        new_template[i[0]+rules[i]] += template[i]
        new_template[rules[i]+i[1]] += template[i]
        
    template = new_template

stats = {}
stats[last] = 1
for i in new_template:
    if i[0] not in stats:
        stats[i[0]] = 0
    stats[i[0]] += new_template[i]

print(max(stats.values()) - min(stats.values()))