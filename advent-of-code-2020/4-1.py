import re

file = open("4-in.txt", "r")
lines = file.read().replace('\n\n', '  ').replace('\n', ' ').split('  ')
# print(lines[0])

# a = 'hcl:5d90f0 cid:270 ecl:#66dc9c hgt:62cm byr:1945 pid:63201172 eyr:2026'

valid_tags = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # , 'cid'}


def extract_patterns(passport):
    data = passport.split(' ')
    # print(data)
    passport_tags = set()
    for d in data:
        passport_tags.add(d.split(':')[0])
    return passport_tags


def val_yr(t, arg):
    if (t == 'byr'):
        a = 1920
        b = 2002
    elif(t == 'iyr'):
        a = 2010
        b = 2020
    elif(t == 'eyr'):
        a = 2020
        b = 2030
    else:
        return 'error'

    return (bool(int(arg) >= a and int(arg) <= b))


def val_height(t, arg):
    parts = re.split('(\d+)', arg)
    if (len(parts) == 3):
        height = int(parts[1])
        unit = parts[2]
        if (unit == 'cm'):
            if(height >= 150 and height <= 193):
                return True
            else:
                return False
        elif (unit == 'in'):
            if(height >= 59 and height <= 76):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def val_hair(t, arg):
    regex = re.compile('^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')
    match = regex.match(str(arg))
    return bool(match)


def val_eye(t, arg):
    colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    return (bool(arg in colors))


def val_pid(t, arg):
    regex = re.compile('^[0-9]{9}$')
    match = regex.match(str(arg))
    return (bool(match))


def val_cid(t, arg):
    return True


validation = {
    'byr': val_yr,
    'iyr': val_yr,
    'eyr': val_yr,
    'hcl': val_hair,
    'hgt': val_height,
    'ecl': val_eye,
    'pid': val_pid,
    'cid': val_cid
}


def validate_values(passport):
    data = passport.split(' ')
    for d in data:
        key = d.split(':')[0]
        value = d.split(':')[1]
        if (not validation[key](key, value)):
            # print(key, value)
            return False
    return True
# print(validation['byr']('byr', 'dasd'))
# print(validation['hgt']('77in'))
# print(validation['hcl']('#ab12dg'))
# print(validation['ecl']('amb'))
# print(validation['pid']('0123456789'))


def valid_passport(valid_tags, in_tags):
    diff = valid_tags.difference(in_tags)
    return not bool(diff)


def batch_validate(passports):
    count = 0
    for passport in passports:
        extracted_tags = extract_patterns(passport)
        if (valid_passport(valid_tags, extracted_tags)):
            if(validate_values(passport)):
                print(re.findall('pid:[0-9]{9}', str(passport))[0])
                count += 1

    return count
    # print(valid_tags)
    # print(valid_tags.difference(extracted_tags))


print(batch_validate(lines))
