def compress(s):
    words = s.split()
    seen_words = {} #Our "Memory Map" to remember first occurrences
    result = []
    
    #enumerate(words, 1) gives us the word and its position (1, 2, 3...)
    for i, word in enumerate(words, 1):
        if word in seen_words:
            #If we've seen it, we add the position of the first time it appeared
            result.append(str(seen_words[word]))
        else:
            #If it's new, we save the word and its current position in our map
            seen_words[word] = i
            result.append(word)
            
    #Finally, we glue everything back together with a single space
    return " ".join(result)
    
