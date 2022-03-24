with open('example', 'r') as f:
    data = f.read().splitlines()


M = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

P = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

point = 0

for line in data:
    stack = []
    if line[0] not in M:
        point += P[line[0]]
        continue
    for i in line:
        if i in M:
            stack.append(i)
        elif M[stack[-1]] == i: 
            stack.pop()
        else:
            point += P[i]
            break
print(point)

