#A program to calculate the best move in a game of Yatzy

def is_yatzy(lst):
    for num in lst:
        if num != lst[0]:
            print("No Yatzy")
            return False
    print("Snyggt, Yatzy!")
    return True
#Aaaaah what did i do here  
def is_full_house(lst):
    all_same = []
    check_same = []
    i = 0
    while i < len(lst):
        if lst[0] == lst[i]:
            all_same.append(lst[i])
            print(lst[i])
        else:
            check_same.append(lst[i])
            print(lst[i])
        i += 1
    for num in check_same:
        if num != check_same[0] or len(check_same) < 2:
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
    for key, value in nums.items():
        print(f"Number: {key}, Times appeared: {value}")
    num = 1
    while num <= len(nums):
        if nums[num] == 4:
            print("4K")
            return "4K"
        elif nums[num] == 3:
            print("3K")
            return "3K"
        num += 1

combinations_appeared = {"Ones": False, "Twos": False, "Threes": False, "Fours":False, "Fives": False, "Sixes":False, "3K":False,
                         "4K": False, "SS":False, "LS": False, "CH":False, "FH":False, "YA":False}

def eval_func(lst, combinations_appeared):
    if combinations_appeared["YA"] == False and is_yatzy(lst) == True:
        print('\033[92m' + 'Keep your throw! Note down Yatzy.' + '\033[0m')
        combinations_appeared["YA"] = True 
    elif combinations_appeared["LS"] == False and is_large_straight(lst) == True:
        print('\033[92m' + 'Keep your throw! Note down large straight.' + '\033[0m')
        combinations_appeared["LS"] = True
    elif combinations_appeared["FH"] == False and is_full_house(lst) == True:
        print('\033[92m' + 'Keep your throw! Note down full house.' + '\033[0m')
        combinations_appeared["FH"] = True
    elif combinations_appeared["SS"] == False and combinations_appeared["LS"] == False and is_small_straight(lst) == True:
        print("Almost large straight: Try rerolling the remaining die.")
    elif combinations_appeared["SS"] == False and is_small_straight(lst) == True:
        print('\033[92m' + 'Keep your throw! Note down a small straight!' + '\033[0m')
        combinations_appeared["SS"] = True
    elif more_of_a_kind(lst) == "4K":
        print("It's four of a kind.")
#Taking in the input and running the evalutation
a = input("Input your numbers: ")

try:
    str_lst = a.split(',')
    lst = list(map(int,str_lst))
    if len(lst) != 5:
        raise ValueError("Did you input too many of too few numbers?")
    else:
        #eval_func(lst, combinations_appeared)
        is_full_house(lst)
except:
    raise ValueError("Did you seperate the numbers by a comma?")

