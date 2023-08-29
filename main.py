#A program to calculate the best move in a game of Yatzy

def is_yatzy(lst):
    for num in lst:
        if num != lst[0]:
            print("No Yatzy")
            return False
    print("Snyggt, Yatzy!")
    print(check_same)

def is_full_house(lst):
    all_same = []
    check_same = []
    i = 0
    while i < len(lst):
        if lst[0] == lst[i]:
            all_same.append(lst[i])
        else:
            check_same.append(lst[i])
        i += 1
    for num in check_same:
        if num != check_same[0]:
            print("No full house!")
            return False
    print("Full house!")
    return True


def is_large_straight(lst):
    sorted_lst = sorted(lst)
    for num in range(len(sorted_lst)-1):
        if sorted_lst[num+1] != sorted_lst[num] + 1:
            print("No large straight!")
            return False
    print("This is a large straight!")
    return True


def is_small_straight(lst):
    sorted_lst = sorted(lst)
    srt1 = sorted_lst[:-1]
    srt2 = sorted_lst[1:]
    if asc(srt1) == True or asc(srt2) == True:
        print("Small Straight!")
        return True
    print("No Small Straight!")
    return False

def asc(srt):
    for i in range(1, len(srt)):
        if srt[i] - srt[i -1] != 1:
            return False
    return True



#Taking in the input and running the evalutation
a = input("Input your numbers: ")

try:
    str_lst = a.split(',')
    lst = list(map(int,str_lst))
    if len(lst) != 5:
        raise ValueError("Did you input too many of too few numbers?")
    else:
        is_yatzy(lst)
        is_large_straight(lst)
        is_full_house(lst)
        is_small_straight(lst)
except:
    raise ValueError("Did you seperate the numbers by a comma?")

