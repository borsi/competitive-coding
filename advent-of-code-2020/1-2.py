file = open("1-in.txt", "r")
lines = file.readlines()

for i in range(0, len(lines)-2):
    for j in range(i+1, len(lines)-1):
        for k in range(j+2, len(lines)):
            if (int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020):
                print(int(lines[i]) + int(lines[j]) +
                      int(lines[k]), lines[i], lines[j])
                print(int(lines[i]) * int(lines[j]) * int(lines[k]))
