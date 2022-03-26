with open('input', 'r') as f:
    data = f.read().splitlines()


edges = {}

for line in data:
    a,b = line.split('-')
    edges[a] = edges.get(a, []) + [b]
    edges[b] = edges.get(b, []) + [a]

print(edges)

def count(node, visited=[], double=False):
    paths = 0
    if node == 'end':
        return 1
    for i in edges[node]:
        if i == 'start':
            continue
        if i in visited and double:
            continue
        if i in visited:    
            if node == node.lower():
                visited.append(node)
            path = count(i, visited, True)
            paths +=path
            if node == node.lower():
                visited.pop()
        else:
            if node == node.lower():
                visited.append(node)
            path = count(i, visited, double)
            paths +=path
            if node == node.lower():
                visited.pop()

    return paths

print(count('start'))