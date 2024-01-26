# class Student:
#     school_name = 'My School'  #class variable
#
#     def __init__(self,name,age): #constructor
#         self.name = name
#         self.age = age
#
#
#     def show(self):            #instance method
#         print(f'Name: {self.name},Age: {self.age}')
#
#     @classmethod                 #class method
#     def change_school(cls,name):
#         cls.name = name
#
#     @staticmethod
#     def find_notes(subject_name):
#         return ['chapter 1', 'chapter 2', 'chapter 3']
class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)

    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']

# std = Student('John',34)
# std.show()
#
# Student.change_school('XYZ School')
# std.change_school('The Educator')
#
# Student.find_notes('Math')
# std.find_notes('Mathematics')
# create object
jessa = Student('Jessa', 12)
# call instance method
jessa.show()

# call class method using the class
Student.change_School('XYZ School')
# call class method using the object
jessa.change_School('PQR School')

# call static method using the class
Student.find_notes('Math')
# call class method using the object
jessa.find_notes('Math')