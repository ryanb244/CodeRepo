def myfunc(string):
    counter = 1
    newstring = ''
    
    for x in string:
        if counter % 2 == 0:
            newstring = newstring + x.upper()
        else:
            newstring = newstring + x.lower()
        counter += 1
    
    return newstring

        


    
        
            




myfunc('aefwd')
    

