# Inheritence

class Mammal:
  def walk(self):
    print("walk")

class Dog(Mammal): # Inheriting the methods in the mammal class
  pass

class Cat(Mammal):
  def scratch(self):
    print("scratch")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()
cat1.scratch()