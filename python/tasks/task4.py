# Problem 4: Multiple Inheritance with Method Resolution Order (Medium)
# Task:

# Create classes A and B. Both classes have a method greet() that prints different messages.
# Create a class C that inherits from both A and B.
# Inside C, call the greet() method and observe which one is called based on the method resolution order (MRO).
# Steps:

# Create class A with a method greet() that prints "Hello from A".
# Create class B with a method greet() that prints "Hello from B".
# Inherit both classes into class C.
# Inside class C, call the greet() method and understand MRO.


class A:
    def __init__(self,greet,name):
        self.greet = greet
        self.name = name
    def greeting(self):  
        print(f"Hello Sir ${self.name} good ${self.greet} and have a nice day") 

class B:
    def __init__(self,greet,name):
        self.greet = greet
        self.name = name
    def greeting(self):  
        print(f"Hello Sir ${self.name} good ${self.greet} and have a nice day") 
class C(A,B):
    def __init__(self,greet,name):
        A.__init__(self,greet,name)
        B.__init__(self,greet,name)
        self.greet = greet
        self.name = name
    def greeting(self):  
        print(f"Hello Sir {self.name} good {self.greet} and have a nice day") 

value =  C("Good Morning", "Shahzaib Saleem")
value.greeting()