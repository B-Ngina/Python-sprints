def get_longest_substring(s):
    n = len(s)
    
    #We try lengths starting from the longest possible (n-1) down to 1
    for length in range(n - 1, 0, -1):
        seen_substrings = set()
        
        #We slide the window of 'length' across the string
        for i in range(n - length + 1):
            substring = s[i : i + length]
            
            #If we've seen this specific chunk before, it's a repeat!
            if substring in seen_substrings:
                return substring
            
            seen_substrings.add(substring)
            
    return "" # Return empty if no repeats are found
  
get_longest_substring("mississippi") #returns "issi"
