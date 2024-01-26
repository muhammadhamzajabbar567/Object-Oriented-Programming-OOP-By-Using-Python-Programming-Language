# Public Members
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name {self.name} & salary {self.salary}")

emp = Employee('John',125000)
print(f"Employee {emp.name} & Salary {emp.salary}")
emp.show()

# Private Members
class Vehicle:
    def __init__(self,name,salary):
        self.name = name            #Public Data Member
        self.__salary = salary      #Private Data Member

    def show(self):
        print(f"Name {self.name} & Salary {self.__salary}")

v = Vehicle("John",278000)
print(v.show())
# print(f"Name {v.name} & Salary {v.__salary}")  #Unable to access private data member from outside the class
print(f'Name: {v.name}')
print(f"Salary: {v._Vehicle__salary}")

class Company:
    def __init__(self):
        self._project = 'NLP'    #Protected Data Member

class Employee(Company):
    def __init__(self,name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print(f"Name: {self.name}")
        print(f'Working on Project: {self._project}')

c = Employee('jessa')
c.show()
print(f'Project: {c._project}')

class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age

sdt = Student("John",34)
print(f"Student: {sdt.name}, Age: {sdt.get_age()}")
sdt.set_age(36)
print(f"Student: {sdt.name}, Age: {sdt.get_age()}")


class Teacher:
    def __init__(self,name,age,id,course):
        self.name = name        #public data member
        self.__age = age        #private data member
        self.__id = id          #private data member
        self._course = course   #protetced data member

    def show(self):
        print(f"Student: {self.name}, Age: {self.__id}, Course: {self._course}")

    def get_id(self):
        return self.__id

    def set_id(self,number):
        if number > 50:
            print("Invalid Id, Please Set Correct Id")
        else:
            self.__id = number

T = Teacher('John',26,34,'NLP')
T.show()

T.set_id(132)
T.set_id(32)
T.show()


# Single Inheritance
class SingleInheritance_Parent():
    def parent_class(self):
        print("Inside Single Inheritance Parent class")

class SingleInheritance_Child(SingleInheritance_Parent):
    def child_class(self):
        print("Inside Single Inheritance Child class")

child = SingleInheritance_Child()
child.parent_class()
child.child_class()

# Multiple Inheritance
class MultipleInheritance_parent1():
    def person_info(self,name,age):
        print("Inside Multiple Inheritance Parent 1 Class")
        print(f"Name {name}, Age {age}")

class MultipleInheritance_parent2():
    def company_info(self,company_name,location):
        print("Inside Multiple Inheritance Parent 2 Class")
        print(f"Company Name {company_name}, Location {location}")

class MultipleInheritance_Child(MultipleInheritance_parent1, MultipleInheritance_parent2):
    def employee_info(self,salary,skill):
        print("Inside Employee Class")
        print(f"Salary {salary}, Skill {skill}")

child = MultipleInheritance_Child()
child.person_info('jessa',26)
child.employee_info(12000,'Machine Learning')
child.company_info('Google','Atlanta')

# Multi Level Inheritance
class Vehicle:
    def vehicle_info(self):
        print('Inside Vehicle Class')

class Car(Vehicle):
    def Car_info(self):
        print('Inside Car Class')

class SportsCar(Car):
    def sports_info(self):
        print('Inside sports Class')

s_car = SportsCar()
s_car.vehicle_info()
s_car.Car_info()
s_car.sports_info()

# Hierarchical Inheritance
class Vehicle:
    def info(self):
     print('\n Inside Vehicle Class')

class Car(Vehicle):
    def car_info(self,name):
        print(f"Car Name: {name}")

class Truck(Vehicle):
    def truck_info(self,name):
        print(f"Truck Name: {name}")

car = Car()
car.car_info('BMW')
car.info()

truck = Truck()
truck.truck_info('Ford')
truck.info()


# Hybrid Inheritance
class Vehicle:
    def vehicle_info(self):
        print(f"Inside Vehicle Class")

class Car(Vehicle):
    def car_info(self):
        print(f"Inside Car Class")

class Truck(Vehicle):
    def truck_info(self):
        print(f"Inside Truck Class")

class SportsCar(Car, Vehicle):
    def sportscar_info(self):
        print(f"Inside Sports Car Class")

s_car = SportsCar()
s_car.vehicle_info()
s_car.car_info()
s_car.sportscar_info()

# Super Function
class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()

# issubclass function
class Company:
    def fun1(self):
        print("Inside parent class")

class Employee(Company):
    def fun2(self):
        print("Inside child class.")

class Player:
    def fun3(self):
        print("Inside Player class.")

# Result True
print(issubclass(Employee, Company))

# Result False
print(issubclass(Employee, list))

# Result False
print(issubclass(Player, Company))

# Result True
print(issubclass(Employee, (list, Company)))

# Result True
print(issubclass(Company, (list, Company)))

# Method Over_riding
class Vehicle:
    def max_speed(self):
        print("max speed is 100 Km/Hour")

class Car(Vehicle):
    # overridden the implementation of Vehicle class
    def max_speed(self):
        print("max speed is 200 Km/Hour")

# Creating object of Car class
car = Car()
car.max_speed()