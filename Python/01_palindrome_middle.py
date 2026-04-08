def get_palindrome_middle(s):
    # Step 1: Check if it's a palindrome
    if s != s[::-1]:
        return "none"
    
    n = len(s)
    mid = n // 2
    
    # Step 2: Extract middle based on parity
    if n % 2 == 1:
        return s[mid]
    else:
        return s[mid-1 : mid+1]

# Examples
print(get_palindrome_middle("racecar"))  # Output: "e"
print(get_palindrome_middle("noon"))     # Output: "oo"
print(get_palindrome_middle("hello"))    # Output: "none"
