with open('input', 'r') as file:
    data = file.read().split('\n')

horizontal, depth, aim = 0, 0, 0 
for i in data:
    move, value = i.split(' ')
    value = int(value)
    if move == 'forward':
        horizontal += value
        depth += aim*value
    elif move == 'up':
        aim -= value
    elif move == "down":
        aim += value


print("Horizontal:", horizontal)
print("Depth: ", depth)
print("Aim:", aim)
print("Puzzle answer:", horizontal*depth)