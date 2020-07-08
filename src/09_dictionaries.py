"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({"lat": 56, "lon": -244, "name": "way out there!"})
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# d = next(item for item in l if item['user'] == 'user7')
# d['match_sum'] += 3
# print(l)

# YOUR CODE HERE
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! first attempt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# x = next(value for value in waypoints if value['name'] == 'a place')
# x['name'] = 'not a real place'
# # print(waypoints)
# y = next(value for value in waypoints if value['lon'] == -121)
# y['lon'] = -130
# print(waypoints)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! first attempt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
waypoints[0]["name"] = 'not a real place'
waypoints[0]['lon'] = -130
print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for values in waypoints:
    for value in values.values():
        print(value)