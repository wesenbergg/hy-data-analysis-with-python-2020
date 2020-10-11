#!/usr/bin/env python3

import math

def triangle():
    base=float(input("Give base of the triangle: "))
    height=float(input("Give height of the triangle: "))
    print("The area is "+str(height*base/2))

def rectangle():
    width=float(input("Give width of the rectangle: "))
    height=float(input("Give height of the rectangle: "))
    print("The area is "+str(height*width))
    
def circle():
    radius=float(input("Give radius of the circle: "))
    print("The area is "+str(math.pi*radius**2))


def main():
    while True:
        userInp=input("Choose a shape (triangle, rectangle, circle): ")
        if userInp == "triangle":
            triangle()
        elif userInp == "rectangle":
            rectangle()
        elif userInp == "circle":
            circle()
        elif userInp == "":
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
