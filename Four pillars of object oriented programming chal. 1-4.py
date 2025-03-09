# 1. Create rectangle and square classes with method called calculate_perimeter
# that calculates the perimeter of the shapes they represent. Create rectangle and square
# objects and call the method on both of them

# Laiskotti sen verran, etten jaksanu kirjottaa loppuja tehtäviä

class Shape:
    def what_am_i(self):
        print("I am a Shape")
        
class Rectangle(Shape):
    def __init__(self, w, h):
        """widht and height in meters"""
        self.width = w
        self.height = h
    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square(Rectangle, Shape):
    def change_size(self):
        new_size = int(input("Squares new side lenght: "))
        self.width = new_size
        self.height = new_size

class Horse:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

class Rider:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
rectangle1 = Rectangle(int(input("Type rectangles width: ")),
                       int(input("Type rectangles height: ")))
square1 = Square(int(input("Type squares width: ")),
                 int(input("Type squares height: ")))

print("Rectangles perimeter is: ", rectangle1.calculate_perimeter())
print("Squares perimeter is: ", square1.calculate_perimeter())
square1.change_size()
print("Squares new perimeter is: ", square1.calculate_perimeter())
square1.what_am_i()
rectangle1.what_am_i()

kuski = Rider("Anton", 0)
polle = Horse("Polle", 18, kuski)
print(polle.owner.name)

















