def find_org(acronym):
    full_names = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]
    
    for name in full_names:
        #We create the acronym for the current name
        #We split "Wild Honey Organization" into ["Wild", "Honey", "Organization"]
        words = name.split()
        
        #Get the first letter of each word and join them
        #Result for WHO: "WHO"
        generated_acronym = "".join(word[0].upper() for word in words)
        
        #We Compare it to the input
        if generated_acronym == acronym.upper():
            return name
            
    return None
