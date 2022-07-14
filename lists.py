def sum(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum


# Takes in a list of numbers, & returns the biggest number

def biggest(list):
    biggest_so_far = 0
    for num in list:
        if (num > biggest_so_far):
            biggest_so_far = num
    return biggest_so_far

def contains_even(list):
    found = False
    for num in list:
        if (num % 2 == 0):
            found = True
            break
    return found

# Returns if every number is even
def is_all_even(list):
    all_even = True
    for num in list:
        if (num % 2 == 1):
            all_even = False
            break
    return all_even

# Remove Every Odd
def filter_odds(list):
    for num in list:
        if (num % 2 == 1):
            list.remove(num)
    return list

# multiply every number in list by 2
def mult_by_two(list):
    new_list = []
    for num in list:
        new_num = num * 2
        new_list.append(new_num)
    return new_list