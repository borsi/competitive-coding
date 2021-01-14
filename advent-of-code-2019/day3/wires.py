def readData(datafile):
    with open(datafile) as f:
        lines = f.read().splitlines()
        return lines[0].split(','), lines[1].split(',')


a, b = readData('input.txt')
print(a[0], b[0])
