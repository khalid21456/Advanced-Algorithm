import myModule as md

def myFunction(*args):
    print(args[1]+" Edaoudi")

def multiArgs(lang1, lang2, lang3):
    print("My favorite language is : "+lang3)

def kwargs(**boys):
    print(boys["num2"])

#default parameter
def visiting(country="Morocco"):
    print("I visited "+country)


#the pass statement

def func():
    pass

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result


#Lambda function

x = lambda a,b:print("hello "+a+" "+b)

#Arrays
cars = ["Ford", "Volvo", "BMW"]


#OOP

class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.graud = 2019
  def __str__(self):
     return self.name
  def printing(sd):
     print("My name is "+sd.name+", and I have "+str(sd.age)+" years old.")

p1 = Person("John", 36)


class Student(Person):
   def __init__(self, name, age):
      super().__init__(name, age)
   def printing(sd):
      print("Hi")
obj = Student("Khalid",18)


# python iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

x = [15,12,20,1,14,48]


def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0] 
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot] 
    return quicksort(less) + [pivot] + quicksort(greater)

book = dict()

book["apple"] = 10
book["banana"] = 8.5
book["avocado"] = 15

print(book)