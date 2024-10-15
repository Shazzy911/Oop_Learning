# Create a Person class that has attributes name and age, and a method introduce() that prints a message introducing the person.
# Create a subclass Student that inherits from Person. Add an additional attribute student_id and a method study() that prints a message showing the student is studying.





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id  = student_id
    
    def study(self):
        print(f"{self.name} is studying right now... ")






userName = input("Enter your name : ")
userAge = str(input("Enter your age : "))


person1 = Student(userName, userAge, 92659)


person1.study()