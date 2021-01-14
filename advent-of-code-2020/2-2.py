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


def good_password(interval, character, password):
    n = number_of_occurences(character, password)
    if (between(interval[0], interval[1], n)):
        return True
    else:
        return False


def compare_letter(letter, index, line):
    if (line[index-1] == letter):
        return True
    else:
        return False


def new_good_password(interval, character, password):
    first = compare_letter(character, interval[0], password)
    second = compare_letter(character, interval[1], password)
    return bool(first) ^ bool(second)


def count_good_passwords(lines):
    count = 0
    for line in lines:
        interval = extract_interval(line)
        character = extract_character(line)
        word = extract_word(line)
        if (good_password(interval, character, word)):
            count += 1
    return count


def new_count_good_passwords(lines):
    count = 0
    for line in lines:
        interval = extract_interval(line)
        character = extract_character(line)
        word = extract_word(line)
        if (new_good_password(interval, character, word)):
            count += 1
    return count


print(new_count_good_passwords(lines))
# print(new_good_password((1, 3), 'a', 'abcde'))  # true
# print(new_good_password((1, 3), 'b', 'cdefg'))  # false
# print(new_good_password((2, 9), 'c', 'ccccccccccc'))  # false
