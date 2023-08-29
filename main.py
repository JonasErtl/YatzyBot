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
def more_of_a_kind(lst):
    nums = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for num in lst:
        if num == 1:
            nums[1] = nums[1] + 1
        elif num == 2:
            nums[2] = nums[2] + 1
        elif num == 3:
            nums[3] = nums[3] + 1
        elif num == 4:
            nums[4] = nums[4] + 1
        elif num == 5:
            nums[5] = nums[5] + 1
        else:
            nums[6] = nums[6] + 1
    largest_value = None
    for value in nums.values():
        if largest_value is None or value > largest_value:
            largest_value = value
    print(largest_value)
    

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
        more_of_a_kind(lst)
except:
    raise ValueError("Did you seperate the numbers by a comma?")

