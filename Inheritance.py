class Date():
    def get_date(self):
        return "2024-01-25"

class Time(Date):
    def get_time(self):
        return "9:53 AM"

dt = Date()
print("Get The Date From Class Date: ", dt.get_date())
tm = Time()
print("\n Get The Time From Class Time: " , tm.get_time())
print("\n Get The Date From Class Time: " , tm.get_date())

class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self,food):
        print('%s is eating %s. ' % (self.name, food))

class Dog(Animal):

    def fetch(self,thing):
        print(f"{d.name} goes after the {d.name}! ", (self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print(f'{c.name} shreds the string', (self.name))

d = Dog('Ranger')
c = Cat('Meow')

d.fetch('Ball')
c.swatstring()

d.eat("Dog Food")
c.eat("Cat Food")

class Animal1(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print(f"{0} eats {1}".format(self.name,food))
class Dog1(Animal1):
    def fetch(self,thing):
        print(f"{0} goes after the  {1}!".format(self.name,thing))
    def show_affection(self):
        print(f"{0} wags tail".format(self.name))

class Cat1(Animal1):
    def swatstring(self):
        print(f"{0} shreds the string!".format(self.name))
    def show_affection(self):
        print(f"{0} purs".format(self.name))

for i in (Dog1('Rover'), Cat1('Fluffy'),Cat1('Precious'),Dog1('Scout')):i.show_affection()

import random

class Animal(object):

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Doberman', 'German Shepherd', 'Beagle'])

    def fetch(self,thing):
        print(f'%s goes after %s!' %(self.name, thing))

d = Dog('dogname')
print(d.breed)
print(d.name)

# Multiple Inheritance
class A(object):
    def dothis(self):
        print('Doing this in A')

class B(A):
    pass

class C(A):
    def dothis(self):
        print('Doing this in C')
class D(B, C):
    pass

d = D()
d.dothis()
print(D.mro())

