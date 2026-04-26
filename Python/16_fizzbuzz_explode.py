def explode_fizzbuzz(target_z_count):
    current_string = "fizzbuzz"
    steps = 0
    
    # We keep going until the count of 'z's reaches our target
    while current_string.count('z') < target_z_count:
        new_string = []
        
        #Look at every single letter in our current string
        #We start counting positions at 1
        for i, char in enumerate(current_string, 1):
            if i % 3 == 0 and i % 5 == 0:
                new_string.append("fizzbuzz")
            elif i % 3 == 0:
                new_string.append("fizz")
            elif i % 5 == 0:
                new_string.append("buzz")
            else:
                #If it's not a special position, keep the letter as it is
                new_string.append(char)
        
        #Join the new pieces to create the string for the next step
        current_string = "".join(new_string)
        
        #Count this as one full step
        steps += 1
        
    return steps
