# ### Problem 1: **Basic Class Definition** (Easy)

# **Description:**  
# Create a `Book` class with attributes `title`, `author`, and `pages`. Write a method `display_info()` that prints the book details in a formatted string.

# **Guidance:**  
# This problem focuses on basic class structure and method definition.

# **Goal:**  
# ```python
# # Expected Output Example:
# # Title: "The Great Gatsby", Author: F. Scott Fitzgerald, Pages: 180
# ```

# ---





class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title of the New book is gonna be {self.title} it has {self.pages} pages with the self-motivation chapters as well. The author of the book is one of the best noble award winner {self.author}")
    



book1 = Book("Good to know", "Shahzaib Saleem", 387)

book1.display_info()
