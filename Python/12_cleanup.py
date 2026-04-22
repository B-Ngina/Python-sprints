def get_cleanup_score(items):
    base_values = {
        "bottle": 10, "can": 6, "bag": 8, "tire": 35, "straw": 4,
        "cardboard": 3, "newspaper": 3, "shoe": 12, "electronics": 25,
        "battery": 18, "mattress": 38
    }
    
    total_score = 0
    streak_item = None
    streak_bonus = 0
    
    for i, item in enumerate(items, 1): #We start counting from 1 for the multiplier
        current_value = 0
        
        #Handling Rare Items (List)
        if isinstance(item, list):
            current_value = item[1]
            streak_item = None 
            #Rare items break the streak
            streak_bonus = 0
            
        #Handling Normal Items (String)
        else:
            val = base_values[item]
            if item == streak_item:
                streak_bonus += 1
            else:
                streak_item = item
                streak_bonus = 0
            current_value = val + streak_bonus
            
        #We apply the Multiplier (Every 5th item)
        if i % 5 == 0:
            multiplier = (i // 5) + 1
            current_value *= multiplier
            
        total_score += current_value
        
    return total_score
