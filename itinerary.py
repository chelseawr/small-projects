#!/bin/python3

'''
    takes 2D array input of an unsorted itinerary (routes)
    returns string of ordered itinerary

        Chelsea May - 2021
'''

# orders routes into complete itinerary
def find_routes(routes):    
    itinerary = find_start(routes)
    
    for i in range(len(routes)):
        itinerary.append(find_next(routes,itinerary[i]))
        
    # convert list to string and output explicit itinerary
    return ', '.join(map(str, itinerary))

# helper function to find destination from given origin
def find_next(routes,stop):
    for r in routes:
        if r[0] == stop:
            return r[1]

# helper function to find the start from a 2d array of itineraties
# finds which origin is not also a destination
def find_start(routes):
    origins = [i[0] for i in routes]
    destinations = [i[1] for i in routes]
    
    # returns list with the first stop as the sole element
    return [item for item in origins if item not in destinations]


   