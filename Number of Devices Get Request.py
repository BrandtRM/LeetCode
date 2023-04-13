import requests
import datetime
def numDevices(statusQuery, threshold, dateStr):
    # Write your code here
    ## Get total number of pages
    pages = requests.get("https://jsonmock.hackerrank.com/api/iot_devices/").json()['total_pages']
    
    data = []
    ## Query each page and add to list as a 3 tuple
    for i in range(1, pages + 1):
        get = requests.get("https://jsonmock.hackerrank.com/api/iot_devices/search?page=<pageNumber>".replace('<pageNumber>', str(i))).json()
        
        ## Add each 3 tuple
        for item in get['data']:
            data.append((item['status'], datetime.datetime.fromtimestamp(item['timestamp'] / 1000.0).strftime("%m-%Y"), item['operatingParams']['rootThreshold']))

    sol = 0
    ## Check for matching date, status query and a threshold less than the root
    for item in data:
        if item[0] == statusQuery  and item[1] == dateStr and item[2] > threshold:
            sol += 1
            
    return sol
