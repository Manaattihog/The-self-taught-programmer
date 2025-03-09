# 1. on tehty.
# 2. ok
# 3. ok

class Square:
    square_list = []

    def __init__(self, s):
        """ width and height in meters """
        self.side = s
        self.square_list.append((self.side, self.side))

    def print_square(self):
        print("{} by {} by {} by {}".format(self.side, self.side,
                                            self.side, self.side))

def is_same(ob1, ob2):
    print(ob1 is ob2)

square1 = Square(int(input("Type side lenght: ")))
square2 = Square(int(input("Type side lenght: ")))
square3 = Square(int(input("Type side lenght: ")))

print(Square.square_list)
square1.print_square()
square2.print_square()
square3.print_square()
is_same(square1, square1)
is_same(square1, square2)
is_same(square1, square3)
