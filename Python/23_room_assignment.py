def get_roommates(people):
    #1.We create a dictionary to hold the waiting lines for each group
    group_queues = {}
    
    #2.Sort people into their respective group lines
    for person in people:
        name = person["name"]
        group = person["group"]
        
        if group not in group_queues:
            group_queues[group] = []
        group_queues[group].append(name)
        
    rooms = []
    
    #3.We go through each group line and pair people up
    for group, names in group_queues.items():
        #Step by 2 to grab pairs
        for i in range(0, len(names), 2):
            #If there's a pair available (i + 1 is still within the list)
            if i + 1 < len(names):
                rooms.append(f"{names[i]} and {names[i+1]}")
            #Otherwise, this person is the odd one out (solo room)
            else:
                rooms.append(names[i])
                
    return rooms

#Test with example
test_people = [
    { "name": "Alice", "group": "A" },
    { "name": "Bob", "group": "B" },
    { "name": "Carol", "group": "A" }
]
print(get_roommates(test_people)) #Output: ['Alice and Carol', 'Bob']
