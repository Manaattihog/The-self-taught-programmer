def adder(x, y = 4):
    return x + y
x = input("type number: ")
x = int(x)
y = input("type another number: ")
y = int(y)
print(adder(x))
print(adder(x, y))
