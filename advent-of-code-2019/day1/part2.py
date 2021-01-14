import math


def fuelReqs(mass):
    return (math.floor(mass / 3) - 2)


def fuelForFuel(fuelmass):
    if fuelmass > 0:
        return fuelmass + fuelForFuel(fuelReqs(fuelmass))
    else:
        return 0


def readData(datafile):
    with open(datafile) as f:
        return f.read().splitlines()


def sumReqs(masses):
    sum = 0
    for m in masses:
        sum += (fuelForFuel(int(m)) - int(m))
    return sum


def main():
    masses = readData('input.txt')
    print(sumReqs(masses))
    #test = 100756
    # print(fuelForFuel(test)-test)


main()
