// ### Problem 1: **Basic Class Definition** (Easy)

// **Description:**
// Create a `Book` class with attributes `title`, `author`, and `pages`. Write a method `display_info()` that prints the book details in a formatted string.

// **Guidance:**
// This problem focuses on basic class structure and method definition.

// **Goal:**
// ```python
// # Expected Output Example:
// # Title: "The Great Gatsby", Author: F. Scott Fitzgerald, Pages: 180
// ```

// ---

#include <iostream>
using namespace std;

class Book
{

public:
    string author, title;
    int pages;
    Book(string x, string y, int z) : author(x), title(y), pages(z)
    {
    }

    void display_info()
    {
        cout << "Book name is going to be " << title << " written by " << author << "it has " << pages << " as well" << endl;
    };
};

int main()
{
    Book obj("Shahzaib", "Good to know", 888);
    obj.display_info();
    return 0;
}