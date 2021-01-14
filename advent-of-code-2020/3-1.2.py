file = open("3-in.txt", "r")
#file = open("3-intest.txt", "r")
# lines = file.readlines()
lines = file.read().splitlines()


def is_tree(char):
    if (char == '#'):
        return True
    else:
        False


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def sloper(slope):
    right = slope[0]
    step = slope[1]
    count = 0
    j = 0
    for i in range(0, len(lines), step):
        l = len(lines[i])
        #print(j, j % l)
        if(is_tree(lines[i][j % l])):
            count += 1
        j += right
    return(count)


mul = 1
for s in slopes:
    route = sloper(s)
    mul *= route
    print(route, mul)
