with open('input', 'r') as f:
    data = f.read().splitlines()


M = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

P = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []

for line in data:
    stack = []
    for i in line:        
        if i in M:
            stack.append(i)
        elif M[stack[-1]] == i: 
            stack.pop()
        else:
            break
    else:
        score = 0
        for i in stack[::-1]:
            score *= 5
            score += P[M[i]]
        scores.append(score)

mid = len(scores)//2
print(sorted(scores)[mid])