import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# creating two point objects
point1 = Point(2, 3)
point2 = Point(4, 6)

# printing the distance between the two points
print(f"The distance between {point1} and {point2} is {point1.distance(point2)}")
