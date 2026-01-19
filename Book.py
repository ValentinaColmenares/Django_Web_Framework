# A simple Python class representing a "Book" with attributes like title, author, and price, and methods to display
# information and calculate discounts

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        """Prints the book's information."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percentage):
        """
        Calculates and returns the price after discount.
        discount_percentage should be a value between 0 and 100.
        """
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        discount_amount = self.price * (discount_percentage / 100)
        return self.price - discount_amount

# Example usage:
book = Book("Clean Code", "Robert C. Martin", 45.00)

book.display_info()

discounted_price = book.apply_discount(20)
print(f"Price after discount: ${discounted_price:.2f}")


# filter the books to find all books by a specific author, sort them by price, and then create a new list of dictionaries 
# that includes a calculated discounted_price for each book
from pprint import pprint

books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "price": 45.00},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "price": 50.00},
    {"title": "Clean Architecture", "author": "Robert C. Martin", "price": 40.00},
    {"title": "Refactoring", "author": "Martin Fowler", "price": 55.00},
]

author_name = "Robert C. Martin"
discount = 0.10  # 10%

filtered_sorted_books = [
    {
        **book,
        "discounted_price": round(book["price"] * (1 - discount), 2)
    }
    for book in sorted(
        filter(lambda b: b["author"] == author_name, books),
        key=lambda b: b["price"]
    )
]

pprint(filtered_sorted_books)