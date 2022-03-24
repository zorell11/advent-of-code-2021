with open('input', 'r') as file:
    data = file.read().split('\n')

horizontal, depth = 0, 0
for i in data:
    move, value = i.split(' ')
    if move == 'forward':
        horizontal += int(value)
    elif move == 'up':
        depth -=int(value)
    else:
        depth += int(value)

print("Horizontal:", horizontal)
print("Depth: ", depth)
print("Puzzle answer:", horizontal*depth)