def mergeArrays(a, b):
    # Write your code here
    i = 0
    j = 0
    c = []
    
    ## Iterate until every element is added
    while len(c) < len(a) + len(b):
        ## indexes in check and a <= b
        if i < len(a) and j < len(b) and a[i] <= b[j]:
            c.append(a[i])
            i += 1
        ## indexes in check and a > b
        elif i < len(a) and j < len(b) and b[j] <  a[i]:
            c.append(b[j])
            j += 1
        ## a is the last left
        elif i < len(a):
            c.append(a[i])
            i += 1
        ## b is the last left
        elif j < len(b):
            c.append(b[j])
            j += 1
    return c
