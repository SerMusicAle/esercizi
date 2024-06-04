"""
Exercise 3: Library Management System 
Create a Book class containing the following attributes: title, author, isbn
The book class must contains the following methods:

__str__ method to return a string representation of the book.

@classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". It means that you must use the class reference cls to create a new object of the Book class using a string.

Example: 
book = “La Divina Commedia, D. Alighieri, 999000666”
divina_commedia: Book = Book.from_string(book)
Here divina_commedia must contain an instance of the class Book with 

title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

Create a Member class with the following attributes: name, member_id, borrowed_books
The member class must contain the following methods:

borrow_book(book) to add a book to the borrowed_books list.

return_book(book) to remove a book from the borrowed_books list.

__str__ method to return a string representation of the member.

@classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
The library class must contain the following methods:

add_book(book) to add a book to the library and increment total_books.

remove_book(book) to remove a book from the library and decrement total_books.

register_member(member) to add a member to the library.

lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

__str__ method to return a string representation of the library with the list of books and members.

@classmethod library_statistics(cls) to print the total number of books.

Create a script and play a bit with the classes:
Create instances of books and members using class methods. Register members and add books to the library. Lend books to members and display the state of the library before and after lending.

"""



"""
id univoci
"""