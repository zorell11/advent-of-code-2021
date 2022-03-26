with open('example', 'r') as f:
    data = f.read().splitlines()


edges = {}

for line in data:
    a,b = line.split('-')
    edges[a] = edges.get(a, []) + [b]
    edges[b] = edges.get(b, []) + [a]

print(edges)

def count(node, visited=[]):
    paths = 0
    if node == 'end':
        return 1
    for i in edges[node]:
        if i in visited:
            continue
        if node == node.lower():
            visited.append(node)
        path = count(i, visited)
        paths +=path
        if node == node.lower():
            visited.pop()
    return paths

print(count('start'))