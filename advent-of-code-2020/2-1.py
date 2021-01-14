file = open("2-in.txt", "r")
lines = file.readlines()


def number_of_occurences(character, word):
    count = 0
    for c in word:
        if (character == c):
            count += 1
    return count


def extract_interval(input):
    f = int(input.split(' ')[0].split('-')[0])
    t = int(input.split(' ')[0].split('-')[1])
    return (f, t)


def extract_character(input):
    c = input.split(' ')[1].split(':')[0]
    return c


def extract_word(input):
    w = input.split(' ')[2]
    return w


def between(a, b, c):
    if (c >= a and c <= b):
        return True
    else:
        return False


def count_good_passwords(lines):
    count = 0
    for line in lines:
        interval = extract_interval(line)
        character = extract_character(line)
        word = extract_word(line)
        n = number_of_occurences(character, word)
        if (between(interval[0], interval[1], n)):
            count += 1
    return count


print(count_good_passwords(lines))
