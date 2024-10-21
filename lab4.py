import data
from data import Point
import math

# Write your functions for each part in the space below.

# Part 1
#function first_element takes a list with nested lists and return the 1st elements of those lists
def first_element(x:list[list[int]])->list:
    new_list = []
    final_list = []
    for i in x:
        if len(i) != 0:
            new_list.append(i)
    for n in new_list:
        final_list.append(n[0])
    return final_list

# Part 2

#function x_coordinates takes argument list[Point] and returns a list with the x-coordinate of
# each point from the input list.
def x_coordinates(point_list:list[Point])->list:
    x_coord_list = []
    for i in point_list:
        x_coord_list.append(i.x)
    return x_coord_list

# Part 3

#function are_in_positive_quadrant takes parameter type list[Point(x,y)] and returns a list of only points that are in
# the first quadrant of the x,y plane.

def are_in_positive_quadrant(point_list:list[Point])->list[Point]:
    positive_list = []
    for i in point_list:
        if i.x > 0 and i.y > 0:
            positive_list.append(i)
    return positive_list

# Part 4

#function distance takes two parameters of type Point(x:int, y:int) and returns a float of the Euclidean distance
# between the two points.
#Euclidean distance definition: square root((x2-x1)**2 + (y2-y1)**2)

def distance(point_1:Point, point_2:Point)->float:
    return math.sqrt((point_2.x - point_1.x)**2 + (point_2.y - point_1.y)**2)

# Part 5
#function manhattan_distance takes two parameters of type Point(x:int, y:int) and returns a float of the Manhattan distance
# between the two points.
#Manhattan distance definition: The distance between two points measured along axes at right angles.
# In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.

def manhattan_distance(point_1:Point, point_2:Point)->float:
    return abs(point_1.x - point_2.x) + abs(point_1.y - point_2.y)

# Part 6
#function distance_all takes parameter of type list[Point(x:int,y:int)] and returns a new list with the distance
# (either euclidian or manhattan) from the origin to the corresponding point

def distance_all(point_list:list[Point])->list:
    distance_list = []
    origin = Point(0,0)
    for i in point_list:
        dist = distance(origin, i)
        dist = round(dist)
        distance_list.append(dist)
    return distance_list


