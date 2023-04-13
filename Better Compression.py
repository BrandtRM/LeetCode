def betterCompression(s):
    # Write your code here
    ## split string into alpha and numeric parts(assumption that alpha always comes before a numeric i.e. valid string for this example)
    split = re.split('(\d+)', s.strip())
    
    ## dict to store value pairs
    comp = dict()
    i = 0
    ## removes end element
    while i < len(split) - 1:
        ## key already in dict
        if comp.get(split[i]):
            comp[split[i]] += int(split[i + 1])
            i += 2
        ## key not in dict
        else:
            comp[split[i]] = int(split[i + 1])
            i += 2     
              
    sol = ''
    ## builds outputted string in alphabetic ordering
    for key in sorted(comp):
        sol += key + str(comp[key])
        
    return sol
