def get_direction(time1, time2):
    #We start by converting "HH:MM" to total minutes
    h1, m1 = map(int, time1.split(":"))
    h2, m2 = map(int, time2.split(":"))
    
    t1_minutes = h1 * 60 + m1
    t2_minutes = h2 * 60 + m2
    
    #Total minutes in a day
    TOTAL_MIN = 1440 
    
    #We calculate distances using modulo to handle the mid-night wrap-around
    #Forward is (Target - Start), Backward is (Start - Target)
    forward = (t2_minutes - t1_minutes) % TOTAL_MIN
    backward = (t1_minutes - t2_minutes) % TOTAL_MIN
    
    #Compare
    if forward < backward:
        return "forward"
    elif backward < forward:
        return "backward"
    else:
        return "equal"
