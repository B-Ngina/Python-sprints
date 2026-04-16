import re

def math_on_string(s):
    #we Use 're' to find all numbers and the gaps between them
    #numbers: ['3', '10', '8']
    #gaps: ['ab', 'c']
    numbers = re.findall(r'\d+', s)
    gaps = re.findall(r'\D+', s)

    #If we have leading/trailing non-digits, findall captures them.
    #We need to make sure the first gap we look at is between number 1 and 2.
    if s and not s[0].isdigit():
        gaps.pop(0)

    if not numbers:
        return 0

    #Start our math with the first number
    result = int(numbers[0])

    #Loop through the rest of the numbers and look at the gaps in between
    for i in range(1, len(numbers)):
        gap_length = len(gaps[i-1])
        current_num = int(numbers[i])

        #Even gap = Addition, Odd gap = Subtraction
        if gap_length % 2 == 0:
            result += current_num
        else:
            result -= current_num

    return result
