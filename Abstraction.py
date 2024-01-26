from abc import ABC,abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("Hey! I'm Triangle & I Have 3 Sides")

class Pentagon(Polygon):
    def noofsides(self):
        print("Hey! I'm Pentagon & I Have 5 Sides")

class Hexagon(Polygon):
    def noofsides(self):
        print("Hey! I'm Hexagon & I Have 6 Sides")

class Quadrilateral(Polygon):
    def noofsides(self):
        print("Hey! I'm Quadrilateral & I Have 4 Sides")

tri = Triangle()
tri.noofsides()

quad = Quadrilateral()
quad.noofsides()

penta = Pentagon()
penta.noofsides()

hexa = Hexagon()
hexa.noofsides()

print('\n')
# Another Example
class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()

#Abstract Properties in Python

# Python program showing
# abstract properties

import abc
from abc import ABC, abstractmethod


class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"


class child(parent):

    @property
    def geeks(self):
        return "child class"


try:
    r = parent()
    print(r.geeks)
except Exception as err:
    print(err)

r = child()
print(r.geeks)
