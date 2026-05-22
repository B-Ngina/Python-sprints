def get_meeting_time(availability):
    total_people = len(availability)
    #We create our 'time_seen' counter for all 24 hours, starting at 0
    #Index 0 represents 0:00-1:00, Index 11 represents 11:00-12:00, etc.
    time_seen = [0] * 24

    #Loop through each person
    for person_windows in availability:
        #Use a set to track unique hours for this person only
        person_hours = set()
        
        #Loop through each window for that person
        for start, end in person_windows:
            #Loop through each window for that person
            for hour in range(start, end):
                person_hours.add(hour) 
                #Sets automatically ignore duplicates!
                
        #Mark every individual hour inside this window as 'seen'
        for hour in person_hours:
            time_seen[hour] += 1
                
    #Now we find the earliest hour where the count matches the number of people
    for hour in range(24):
        if time_seen[hour] == total_people:
            return hour
            
    return "None"

#Test case check
print(get_meeting_time([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]])) #Should return 13
