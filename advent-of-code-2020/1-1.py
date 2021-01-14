file = open("1-in.txt", "r")
lines = file.readlines()

for i in range(0, len(lines)-1):
    for j in range(i+1, len(lines)):
        if (int(lines[i]) + int(lines[j]) == 2020):
            print(int(lines[i]) + int(lines[j]), lines[i], lines[j])
            print(int(lines[i]) * int(lines[j]))
