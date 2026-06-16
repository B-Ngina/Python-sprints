def sort_numbers(s):
    numbers = sorted([int(num) for num in s.split(',')])
    return numbers
#Test case check
sort_numbers("3,1,2")
