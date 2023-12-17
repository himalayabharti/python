import math

class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        dx = self.x1 - self.x2
        dy = self.y1 - self.y2
        dist=dx**2 + dy**2
        return math.sqrt(dist)

    
x1=2
y1=3
x2=4
y2=6
# creating two point objects
Point=point(x1,y1,x2,y2)


# printing the distance between the two points
print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {Point.distance()}")
