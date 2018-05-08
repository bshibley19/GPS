import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import math

tup1 = (44.963883, -93.351047)
tup2 = (44.956990, -93.345725)

def calculate_initial_compass_bearing(pointA, pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")
    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180 to + 180 which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

def find_distance (pointA, pointB):
    distance = math.sqrt(((pointA[0]-pointB[0])**2)+((pointA[1]-pointB[1])**2))

print calculate_initial_compass_bearing(tup1, tup2)
print find_distance(tup1, tup2)
