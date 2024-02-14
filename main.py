# coordinate distance finder
import math


class Coordinate:
    # coordinate class with properties X, Y, and Z representing cartesian coordinate positions
    # fancy speak for a point in 3D space
    # contains properties get() which returns a 
    def __init__(self, x,y,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    # when the coordinate object is called (idk) it returns a string of the coordinate
    # in the form of (x,y,z)
    def __call__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    # get coords in dictionary with "X", "Y", "Z" keys
    def get(self):
        return {"X" : self.x, "Y" : self.y, "Z" : self.z}
    
    # returns spatial distance from one point to another
    def distance(self, other):
        return math.sqrt(
            (self.x - other.x)**2
            + (self.y - other.y)**2
            + (self.z - other.z)**2)
    

# example coordinate list
coordinateList = [
    Coordinate(0,0),
    Coordinate(0,1,2),
    Coordinate(2,2),
    Coordinate(3,3),
    Coordinate(0,3),
    Coordinate(3,0),
]

# coordIn 
def coordIn(object, list):
    return any(list[i]() == object() for i in range(len(list)))
#print(coordIn(Coordinate(0,0), coordinateList))
# find index of coordinate in list
def findCordPos(object:Coordinate, list):
    for i in range(len(list)):
        if list[i].get() == object.get():
            return i
    return -1
    
def find_closest(origin:Coordinate, coordinates, display = False):
    # finds closet coordinate to coordinate
    
    # check if origin coordinate is in list
    originIndex = findCordPos(origin, coordinates)
    # if so, remove it
    if originIndex != -1:
        coordinates.pop(originIndex)
    closest = coordinates[0]
    for coordinate in coordinates: # loop through coordinates
        # if current one is closer than the closest one
        if origin.distance(closest) > origin.distance(coordinate):
            # set the closest to the current coordinate
            closest = coordinate
    # display bool says whether or not to print out data 
    if display:
        print("Found closest coordinate to", origin(), "at", closest(),
              "with distance", origin.distance(closest))
    # returns dictionary with distance of origin coordinate to closest coordinate, 
    # and with XYZ coordinates
    return {
        "Distance": closest.distance(origin), 
        "X" : closest.x,
        "Y" : closest.y,
        "Z" : closest.z,
        "XYZ" : closest.get()
           }
#print(find_closest(Coordinate(0,0), coordinateList).distance(Coordinate(0,0)))
print(find_closest(Coordinate(0,0), coordinateList, True))
#print(Coordinate(0,0).distance(Coordinate(2,2)))
