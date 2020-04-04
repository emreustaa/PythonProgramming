import math


class Point:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def returnPoints(self):
        return self.x1, self.y1, self.x2, self.y2


class Euclidean:
    def __init__(self, points):
        self.points = points

    def calculateDistance(self):
        return math.sqrt(math.pow(point.x1 - point.x2, 2) + math.pow(point.y1 - point.y2, 2))


class Manhattan:

    def __init__(self, points):
        self.points = points

    def calculateDistance(self):
        return abs((point.x1 - point.x2) + (point.y1 - point.y2))


point = Point(1, 2, 3, 5)

euclidean = Euclidean(point)
print(euclidean.calculateDistance())

manhattan = Manhattan(point)
print(manhattan.calculateDistance())
