def is_narcissistic(n):
    #We convert to string to count digits and iterate
    n_str = str(n)
    total_digits = len(n_str)
    
    #Using the list comprehension we raise each digit to the power of the total number of digits
    results = sum(int(digit) ** total_digits for digit in n_str)
    
    #Return the result of the comparison (this will be True or False)
    return results == n

print(is_narcissistic(153)) # Should be True
print(is_narcissistic(154)) # Should be False
