def parse_frontmatter(s):
    #Initializes an empty dictionary to hold our final key-value pairs
    result = {}
    
    # Splits the giant raw text block into individual lines using the newline character
    lines = s.split('\n')
    
    for line in lines:
        # Skips the structural '---' boundaries and skips any blank or whitespace-only lines
        if line == '---' or not line.strip():
            continue
            
        # Ensures the line contains a colon before trying to parse it
        if ':' in line:
            # Splits the line at the FIRST colon only. 
            # This protects values that might contain colons themselves (like times or sub-titles).
            key, value = line.split(':', 1)
            
            # Removes any accidental leading or trailing spaces around the key and value
            key = key.strip()
            value = value.strip()
            
            #TYPE CONVERSION LAYER
            
            # Step 1: Checks if the value represents a Boolean
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            else:
                # Step 2: Attempts numerical conversion using a try/except safety net.
                # This handles negative numbers ('-100') and decimals ('4.5') gracefully.
                try:
                    if '.' in value:
                        value = float(value) # Converts to a decimal number if a dot is present
                    else:
                        value = int(value)   # Converts to a whole integer
                except ValueError:
                    # Step 3: Fallback to a String if it cannot be converted to a number.
                    # If the string is wrapped in literal quotes ("text" or 'text'), strips them off.
                    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1] # Slices off the first and last character (the quotes)
            
            # Assigns the cleanly processed value to its corresponding key in the dictionary
            result[key] = value
            
    # Return the completed, strongly-typed dictionary object
    return result

# Test case check
print(parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"))
# Output: {'title': 'My Post', 'draft': False, 'views': 100}
