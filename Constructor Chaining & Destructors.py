class Vehicle:
    def __init__(self,engine):
        self.engine = engine
        print("Inside Vehicle Constructor")

class Car(Vehicle):
    def __init__(self,engine, max_speed):
        super().__init__(engine)
        print("Inside Car Constructor")
        self.max_speed = max_speed

class Electric_Car(Car):
    def __init__(self,engine, max_speed,km_range):
        super().__init__(engine,max_speed)
        print("Inside Electric Car Constructor")
        self.km_range = km_range

ec = Electric_Car('1800 cc',240,1000)
print(f"Engine={ec.engine}, Max Speed={ec.max_speed}, KM Range={ec.km_range}")

# Destructors
import time
class Student:
    def __init__(self,name):
        print("Inside Student Constructor")
        self.name = name
        print("Object Initialized")

    def show(self):
        print(f"Hello, My Name is {self.name}")

    def __del__(self):
        print("Inside Student Destructor")
        print("Object Destroy")

s1 = Student('Emma')
s1.show()
s2 =s1
del s1

time.sleep(5)
print('After 5 seconds Sleep')
s2.show()


