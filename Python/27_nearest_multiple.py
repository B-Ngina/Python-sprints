def round_to_nearest_multiple(num, multiple):
    #Finds the factor fraction, round it to the nearest whole integer, 
    #and scales it back up by multiplying it by the target factor.
    return round(num / multiple) * multiple

#Test cases checks
print(round_to_nearest_multiple(5, 3))   #Output: 6
print(round_to_nearest_multiple(17, 4))  #Output: 16
