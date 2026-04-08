def is_fizz_buzz(arr):
    #we find the first actual integer to determine our starting number
    start_val = None
    for idx, val in enumerate(arr):
        if isinstance(val, int):
            #If we find 16 at index 1, the number at index 0 must be 15
            start_val = val - idx
            break
    
    # If the array is all strings (like ["Fizz", "Buzz"]), 
    # we can't be 100% sure where it starts, so we default to 1.
    if start_val is None:
        start_val = 1
        
    #We then run the loop using our calculated starting point
    for idx, val in enumerate(arr):
        current_num = start_val + idx
        
        if current_num % 15 == 0:
            expected = "FizzBuzz"
        elif current_num % 3 == 0:
            expected = "Fizz"
        elif current_num % 5 == 0:
            expected = "Buzz"
        else:
            expected = current_num

        if val != expected:
            return False
            
    return True
