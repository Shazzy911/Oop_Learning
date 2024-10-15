class Person:
    def __init__(self, name, age, city):
        self.name = name;
        self.age = age;
        self.city = city;
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}"



    def personInfo(self):
        print(f"Person name is {self.name} person age is {self.age} and he lives in {self.city} ");



p1 = Person("Shahzaib", 22, "Multan");

print(p1)

p1.name;
p1.age;
p1.city;

p1.personInfo();

