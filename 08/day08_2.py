with open('input', 'r') as f:
    data = f.read().splitlines()

values = 0
for row in data:
    input, output = row.split(' | ')
    stats = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    sol = {}
    for i in input.split():
        stats[len(i)].append(i)
        if len(i)==2:
            sol[1]=set(i)
        elif len(i) == 3:
            sol[7]=set(i)
        elif len(i) == 4:
            sol[4] = set(i)
        elif len(i) == 7:
            sol[8] = set(i)


    #two, three and five
    for i in stats[5]:
        #three
        if set(i) & sol[1] == sol[1]:
            sol[3] = set(i)
        #five
        elif len(set(i) & sol[4]) == 3:
            sol[5] = set(i)
        #two
        else:
            sol[2] = set(i)

    #zero, six, nine
    for i in stats[6]:
        #six
        if not (set(i) & sol[1] == sol[1]):
            sol[6] = set(i)
        elif set(i) & sol[3] == sol[3]:
            sol[9] = set(i)
        else:
            sol[0] = set(i)

    value = ''
    for i in output.split():
        for j in sol:           
            if set(i) == sol[j]:
                value +=str(j)

    values += int(value)
print(values)