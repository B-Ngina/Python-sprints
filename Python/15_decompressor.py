def decompress(s):
    #We split the sentence into individual words
    words = s.split()
    results = []
    for word in words:
        #check if the words is actually a number 
        if word.isdigit():
            #Turn the text "3" into the number 3
            position = int(word)
            # Go to our results "library" and grab the word at that spot
            #Subtract 1 because Python starts counting at 0
            original_word = results[position - 1]
            results.append(original_word)
        else:
            #If it's a normal word, just add it to the list
            results.append(word)
    return " ".join(results)
