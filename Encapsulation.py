class MyClass(object):
 def setAge(self, num):
  self.age = num
 def getAge(self):
  return self.age
zack = MyClass()
zack.setAge(45)
print(zack.getAge())
zack.setAge("Fourty Five")
print(zack.getAge())

class python(object):
 def set_name(self, name):
  self.name = name

 def get_name(self):
  return self.name

py = python()
py.set_name("Programming Language")
print(py.get_name())
py.set_name(123)
print(py.get_name())

class InstanceCounter(object):
 count = 0

 def __init__(self,val):
  self.val = val
  InstanceCounter.count +=1

  def set_val(self,new_val):
   self.val = new_val

   def get_val(self):
    return self.val

   def get_count(self):
    return InstanceCounter

a = InstanceCounter(34)
b = InstanceCounter("Second Object")
c = InstanceCounter(9509)

# for obj in (a,b,c):
#  print(f"Val of obj: %s" +obj.get_val())
#  print("count of obj: %s" +(obj.get_count()))
#
# normal_list = [2,4,5,7,9,10]
#
# class CustomSequence():
#
#   def __len__(self):
#    return 5
#
#   def __getitem__(self, index):
#    return "x{0}".format(index)
#
# class funkyback():
#   def __reversed__(self):
#    return 'backwards!'
#   for seq in normal_list,CustomSequence(),funkyback():
#    print('\n {}: '.format(seq.__class__.__name__), end='')
#    for item in reversed(seq):
#     print(item,end=' , ')
#
# normal_list = [2, 4, 5, 7, 9]
#
# class CustomSequence():
#  def __len__(self):
#   return 5
#  def __getitem__(self,index):
#    return "x{0}".format(index)
# class funkyback():
#   def __reversed__(self):
#      return 'backwards!'
#   for seq in normal_list, CustomSequence(), funkyback():
#    print(item, end=", ")
#    print('\n{}: '.format(seq.__class__.__name__), end="")
#    for item in reversed(seq):
#     pass
names = ["abc", 'def', 'ghi', 'jkl', 'mno']
enumerate(names)
list(enumerate(names))

for i,n in enumerate(names):
 print('Number Names: ', str(i))
 print(n)

