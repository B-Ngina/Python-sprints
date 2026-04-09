def get_next_bingo_number(n):
    letter = n[0]
    num = int(n[1:])
    letters = "BINGO"
    
    # Find the boundaries
    limits = {"B": 15, "I": 30, "N": 45, "G": 60, "O": 75}
    
    # If it's the absolute last one,we reset to start
    if n == "O75":
        return "B1"
    
    # If we are at the end of a letter's range, we move to the next letter
    if num == limits[letter]:
        current_idx = letters.find(letter)
        next_letter = letters[current_idx + 1]
        return f"{next_letter}{num + 1}"
    
    # Otherwise,we just increment the number
    return f"{letter}{num + 1}"
