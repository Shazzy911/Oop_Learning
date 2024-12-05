# # Problem 5: Inheritance with Method Overriding (Medium)
# # Task:

# # Create a base class Animal with a method make_sound() that prints "Animal makes sound."
# # Create a subclass Dog that overrides the make_sound() method to print "Dog barks."
# # Further create a subclass Cat that overrides the make_sound() method to print "Cat meows."
# # Use a loop to create objects of both Dog and Cat and call their make_sound() methods.
# # Steps:

# # Create the Animal class with the method make_sound().
# # Create subclasses Dog and Cat that override make_sound().
# # Create objects of both Dog and Cat, calling their overridden methods.

# class Animal:
#     def __init__(self):
#         pass
#     def make_sound(self):
#         print(f"Animal make sound")
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#     def make_sound(self):
#         print(f"Dog barks")
# class Cat()        