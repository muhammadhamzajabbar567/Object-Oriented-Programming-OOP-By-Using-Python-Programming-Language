# Inheritance

class Parent:
    def d1(self):
        print("Parent Class Method Called....")

class Child(Parent):

    def __init__(self):
        print("Child Class Object Created....")

    def d2(self):
        print("Child Class Method Called....")

obj = Child()
obj.d1()
obj.d2()

#Composition

class Component:

    def __init__(self):
        print("Component Class Object Created....")

    def m1(self):
        print("Component Class Method m1() executed....")

class Composite:
    def __init__(self):

        self.comp = Component()
        print("Composite Class Object also Created....")

    def m2(self):
        print("Composite Class m2 Method executed....")

        self.comp.m1()

compos = Composite()
compos.m2()

#Aggregation
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay *12) + self.bonus
class Employee:
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.agg_salary = sal

    def total_salary(self):
        return self.agg_salary.annual_salary()

sal = Salary(95000,25000)
emp =   Employee('John',34,sal)
print(emp.total_salary())


