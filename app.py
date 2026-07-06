import math

def add(a,b):
    return a + b
def area_ractangle(x, y):
    return x * y

def circle_area(r):
    area = (math.pi * (r ** 2))
    return round(area,3)
#    return area

if __name__ == "__main__":
    print("Hello from jenkins")
    print("Sum is: ", add(4,5))
    print("Area is: ", area_ractangle(4, 5) )
    print("Circle area is: ", circle_area(5.5) )