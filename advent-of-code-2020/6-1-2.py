file = open("6-in.txt", "r")
lines = file.read().replace('\r\n', ' ').split('  ')


def reduce_groups(group):
    votes = set()
    for i in range(0, len(group)):
        if (group[i] != ' '):
            votes.add(group[i])
    return len(votes)


def reduce_groups_set(group):
    votes = set()
    for i in range(0, len(group)):
        if (group[i] != ' '):
            votes.add(group[i])
    return votes


def sum_yes(input):
    sum = 0
    for i in input:
        sum += reduce_groups(i)
    return sum


def sum_yes_per_group(groups):
    answers = groups.split(' ')
    sums = reduce_groups_set(answers[0])
    if (len(answers) == 1):
        return len(answers[0])
    else:
        for g in range(1, len(answers)):
            tocompare = reduce_groups_set(answers[g])
            sums = sums.intersection(tocompare)
        return len(sums)


def sumall(lines):
    sumofsums = 0
    for l in lines:
        sumofsums += (sum_yes_per_group(l))
    return sumofsums


print(sumall(lines))
