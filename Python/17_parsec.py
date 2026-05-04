def convert_parsecs(parsecs):
    #We check if the number is odd (Time)
    if parsecs % 2 != 0:
        #Time conversion: 1 parsec = 2 hours
        time = parsecs * 2
        return time
    
    #Otherwise, it is even (Distance)
    else:
        #Distance conversion: 2 parsecs = 6 light years
        distance = (parsecs // 2) * 6
        return distance
