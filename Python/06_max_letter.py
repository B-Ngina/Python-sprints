def get_last_letter(s):
    #returns a list of characters in the string if the char is a letter
    letters = [char for char in s if char.isalpha()]
    #returns an empty string if our character is not a letter
    if not letters:
        return ""
    #the max function tells Python to determine the winner based on alphabetical rank, the .lower function standardizes the case for the comparison while returning the original character e.g., "W" instead of "w"
    return max(letters, key = str.lower)

get_last_letter("world")
