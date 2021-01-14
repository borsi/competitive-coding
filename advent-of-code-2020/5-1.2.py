file = open("5-in.txt", "r")
lines = file.read().splitlines()


def find_seat(start, end, partitioning):
    if(bool(partitioning)):
        p = partitioning[0]
        remainder = partitioning[1:]
        mid = (end + start) // 2

        if (p == 'L'):
            return find_seat(start, mid - 1, remainder)
        elif (p == 'R'):
            return find_seat(mid + 1, end, remainder)
    else:
        return start


def find_row(start, end, partitioning):
    if((bool(partitioning)) and (partitioning[0] == 'F' or partitioning[0] == 'B')):
        p = partitioning[0]
        remainder = partitioning[1:]
        mid = (end + start) // 2
        if (p == 'F'):
            return find_row(start, mid - 1, remainder)
        elif (p == 'B'):
            return find_row(mid + 1, end, remainder)
    else:
        return (start, find_seat(0, 7, partitioning))


def seat_id_calculator(partitioning):
    rc = find_row(0, 127, partitioning)
    return rc[0] * 8 + rc[1]


def find_highest_seat_id(input):
    high = 0
    for row in input:
        seatID = seat_id_calculator(row)
        if (seatID > high):
            high = seatID
    return high


def find_occupied_seats(input):
    seats = []
    for row in input:
        seatID = seat_id_calculator(row)
        seats.append(int(seatID))
        # print(seatID)
    return seats


def find_missing_seat(input):
    seats = find_occupied_seats(input)
    seats.sort()
    for index, obj in enumerate(seats):
        if(index < len(seats)-1):
            if (seats[index + 1] != seats[index] + 1):
                print(seats[index - 1], seats[index], seats[index+1])
                print(index, obj)


find_missing_seat(lines)
