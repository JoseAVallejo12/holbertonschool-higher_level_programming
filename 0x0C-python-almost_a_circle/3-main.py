#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r3 = Rectangle(8, 7, 0, 0, 2)
    print(r3.area())

    r2 = Rectangle(2, 10)
    print(r2.area())


    

    print(r1.id, r3.id, r2.id)