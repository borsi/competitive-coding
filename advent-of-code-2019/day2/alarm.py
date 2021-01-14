def readData(datafile):
    with open(datafile) as f:
        return f.read().split(',')


def iterator(input):
    i = 0
    data = input.copy()
    while int(data[i]) < 99:
        if int(data[i]) == 1:
            data[int(data[i+3])] = str(int(data[int(data[i+1])]) +
                                       int(data[int(data[i+2])]))
        elif int(data[i]) == 2:
            data[int(data[i+3])] = str(int(data[int(data[i+1])])
                                       * int(data[int(data[i+2])]))
        i += 4
    return data


def searchSolution(data, solution):
    for noun in range(0, 99):
        for verb in range(0, 99):
            data[1] = noun
            data[2] = verb
            solved = iterator(data)
            if int(solved[0]) == solution:
                return noun, verb


def main():
    memory = readData('input.txt')
    a, b = searchSolution(memory, 19690720)
    print('What is 100 * ' + str(a) + ' + ' + str(b)+'?\n')
    print(100*a+b)


main()
