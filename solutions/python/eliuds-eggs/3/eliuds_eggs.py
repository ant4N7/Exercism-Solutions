def egg_count(display_value):
    counter = 0
    
    #loop through each bit in the display value
    while display_value:
    
        #if the right most bit is 1, add it to the counter
        counter += display_value & 1
        
        #drop the right most bit and repeat
        display_value >>= 1
    
    return counter
    