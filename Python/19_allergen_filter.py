def get_allergen_friendly_meals(meals, allergens):
    safe_meals = []
    
    #We Convert the avoid list to a 'set' for much faster searching
    avoid_set = set(allergens)
    
    for meal_name, meal_allergens in meals:
        #Check if there is any overlap between meal_allergens and avoid_set
        is_safe = True
        for allergen in meal_allergens:
            if allergen in avoid_set:
                is_safe = False
                break #We found one! No need to keep checking this meal.
        
        if is_safe:
            safe_meals.append(meal_name)
            
    return safe_meals
