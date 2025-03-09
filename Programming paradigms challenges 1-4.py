#1. Make class named Apple with 4 instance variables that describes apple
class Apple:
    def __init__(self, c, w, h, f):
        """Weight --> kg, height --> cm, freshness --> 0...10"""
        self.colour = c
        self.weight = w
        self.height = h
        self.freshness = f

apple1 = Apple("Red", 0.1, 10, 8)
print(apple1.colour)
apple1.colour = "Yellow"
print(apple1.colour)

#Create a circle class with method called area that calculates and returns
#its area. Then create circle object, call area on it and print the result
#Use pi() in math
import math

class Circle:
    def __init__(self, d):
        """diameter and area in meters(m)"""
        self.diameter = d
    def area(self):
        return (int(self.diameter)/2)**2 * math.pi

circle1 = Circle(input("type circles diameter:"))
print("Area: ", circle1.area())

#3. Create a triangle class with a method called area that calculates and
# returns its area. Then create triangle object, call area on it, and
# print the result.

class Triangle:
    def __init__(self, b, h):
        """Base and height in meters(m)"""
        self.base = b
        self.height = h
    def area(self):
        return self.base*self.height/2

triangle2 = Triangle(int(input("Triangles base: ")),
                     int(input("Triangles height: ")))
print(triangle2.area())

# 4. Make a Hexagon class with a method called calculate_perimeter that
# calculates and returns its perimeter. then create a Hexagon object,
# call calculate_perimeter on it, and print the result.

class Hexagon:
    def __init__(self, s):
        """side lenght in meters(m)"""
        self.sidelen = s

    def calculate_perimeter(self):
        return self.sidelen * 6

hexagon1 = Hexagon(int(input("Type hexagons side lenght: ")))
print(hexagon1.calculate_perimeter())
