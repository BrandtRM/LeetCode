def getMinimumDays(parcels):
    # Write your code here
    days = 0
    packages = dict()
    for index, value in enumerate(parcels):
        packages[index] = value
    print(packages)

    x = max(packages.values()) 
    # iterate, check for min, reduce all by min, break if all are 0, return days
    while x > 0:
            
        min_days = min(packages.values())
        if min_days == 0:
            min_days += 1

        for i in range(len(packages)):
            if packages[i] <= min_days:
                packages[i] = 0
            else:
                packages[i] -= min_days

        days += 1
        x = max(packages.values())
        
    return days



def getMinDays(parcels):
    # Write your code here
    days = 0
    packages = set()
    for value in parcels:
        packages.add(value)
    print(packages)

    if max(packages) == 0:
        return 0
    # iterate, check for min, reduce all by min, break if all are 0, return days
    while packages:
            
        min_days = min(packages)

        for item in packages:
            if item <= min_days:
                packages.remove(item)
                packages.add(item - min_days)
            else:
                item -= min_days

        packages = {i for i in packages if i != 0}
            
        days += 1
    return days

print(getMinimumDays([4,4,2,3,4]))
print("--------------------------------")
print(getMinimumDays([0,0,0,0]))
print("--------------------------------")
print(getMinimumDays([1,2,3,4,5]))
print("--------------------------------")
print(getMinimumDays([100,25,75,50]))
print("--------------------------------")
print(getMinDays([4,4,2,3,4]))
print("--------------------------------")
print(getMinDays([0,0,0,0]))
print("--------------------------------")
print(getMinDays([1,2,3,4,5]))
print("--------------------------------")
print(getMinDays([100,25,75,50]))
