import math


def fuelReqs(mass):
    return (math.floor(mass / 3) - 2)


def readData(datafile):
    with open(datafile) as f:
        return f.read().splitlines()


def sumReqs(masses):
    sum = 0
    for m in masses:
        sum += fuelReqs(int(m))
    return sum


def main():
    masses = readData('input.txt')
    print(sumReqs(masses))


main()
