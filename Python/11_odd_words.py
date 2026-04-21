def get_odd_words(s):
    words = s.split()
    odd_words = [] #an empty list to hold our results
    
    for word in words:
        #we check if the length of the word is odd
        if len(word) % 2 != 0: 
            odd_words.append(word)
            
    #join the list back together with spaces
    return " ".join(odd_words)
