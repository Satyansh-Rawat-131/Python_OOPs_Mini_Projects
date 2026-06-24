class Book:

    def __init__(self , title , author , isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"title : {self.title} \nauthor : {self.author} \nisbn : {self.isbn} \nborrowed : {"yes" if self.is_borrowed else "no"}"

# class Lib:

#     def __dict__(Self):
#         pass

#     def __init__(self):
#         self.books = []

#     def add_book(self , book):
#         self.books.append(book)
#         print(f"book title : {book.title} added to the lib")

#     def display(self):
#         if not self.books:
#             print("no such book in library")
#         for i in self.books:
#             print("\n",i)

#     def borrow_books(self , isbn):
#         for i in self.books:
#             if i.isbn == isbn and not i.is_borrowed:
#                 i.is_borrowed = True
#                 print(f"yoy have borrowed {i.title}")
#                 return
#         print("book is not available or has been borrowed")

#     def return_book(self , isbn):
#         for i in self.books:
#             if i.isbn == isbn and i.is_borrowed:
#                 i.is_borrowed = False
#                 print(f"you have returned the book = {i.title} ")

# class User:
#     def __init__(self , userId , name , email):
#         self.userId = userId
#         self.name = name
#         self.email = email

#     def add_user(self):
#         pass

#     def list_user(self):
#         pass

#     def __str__(self):
#         pass

#     def update_user(self , userId):
#         self.userId = userId
#         pass

#     def delete_user(self):
#         pass

# book1 = Book("Game Of Thrones" , "George R.R. Martin" , "123456789" )
# book2 = Book("Deep Learning" , "Ian Goodfellow, Yoshua Bengio, and Aaron Courville" , "987654321" )
# book3 = Book("Designing Machine Learning Systems" , "Chip Huyen" , "135792468" )
# book4 = Book("Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" , "Aurélien Géron." , "246813579" )

# print(book1)

# lib = Lib()
# lib.add_book((book1))
# lib.add_book((book2))
# lib.add_book((book3))
# lib.add_book((book4))

# lib.add_book(Book("Atomic Habit" , "James Clear" , "123498765" ))

# print()

# print(lib.display())
