with open('input', 'r') as f:
    data = f.read().splitlines()

sol = 0
for row in data:
    i,j = row.split(' | ')
    #output = j.split()
    #for digit in output:
    #    if str(len(digit)) in '2437':
    #        sol += 1
    for digit in j.split():
        if len(digit) in [2, 4, 3, 7]:
            sol += 1
    

print(sol)