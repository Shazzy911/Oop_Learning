#include <iostream>
using namespace std;

class MyClass
{
private:
    int x;

public:
    MyClass(int x) : x(x) {};

    friend class FriendClass;

    friend void displayInfo(MyClass obj);
};

class FriendClass
{
public:
    void display(MyClass obj)
    {
        cout << "Friend Class accessing value " << obj.x << endl;
    }
};

void displayInfo(MyClass obj)
{
    cout << "Friend Function " << obj.x << endl;
}

int main()
{

    MyClass obj(22);
    FriendClass friendclass;
    friendclass.display(obj);
    displayInfo(obj);

    return 0; // exit program successfully...
}