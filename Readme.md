#Multiple Inheritance.


// In multiple inheritance, when two parent classes have the same function name and properties, the derived class will face an ambiguity issue.
// In your given code, when you call obj.myFunction();, the compiler will throw an error because it doesn't know whether to call myFunction() from MyClass or MyOtherClass.
// To resolve this ambiguity, you can use the scope resolution operator (::) to specify which parent class's function you want to call. Here's how you can do it:

// int main(){
//     MyChildClass obj;
//     obj.MyClass::myFunction();  // This will print "Some content in parent class."
    obj.MyOtherClass::myFunction();  // This will print "Some content in another class."
//     return 0;
// }