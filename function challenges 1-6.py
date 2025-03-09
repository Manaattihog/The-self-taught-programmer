import math

def funktio(x):
    """
    returns x squared
    :param x: int
    :return: int x xquared
    """
    return math.sqrt(x)
x = input("type number: ")
x = int(x)
print(funktio(x))

def tekstifunktio(teksti):
    """
    prints string teksti
    :param teksti: string
    :return: NULL
    """
    print(teksti)
    return
teksti = input("write text: ")
tekstifunktio(teksti)

def lotsofvariables(a, y, z, i = 2, j = 3):
    """
    returns sum of all variables
    :param a: int.
    :param y: int.
    :param z: int.
    :param i: int.
    :param j: int.
    """
    return a + y + z + i + j
a = 2
y = 3
z = 5
print(lotsofvariables(a, y, z))

def jakokahdella(b):
    """
    returns b divided by 2
    :param b: int.
    :return: int b/2
    """
    return int(b/2)
def mulby4(c):
    """
    multiplies c by 4
    :param c: int.
    :return: int c*4
    """
    return int(c*4)
b = input("type number: ")
b = int(b)
c = jakokahdella(b)
print(mulby4(c))


def stofloat(g):
    return float(g)

try:
    g = input("Type numbers: ")
    g = int(g)
    print(stofloat(g))
except(ValueError):
    print("Invalid input")
    
    
