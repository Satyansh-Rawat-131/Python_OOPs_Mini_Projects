class Book:

    def __init__(self , title , author , isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"title : {self.title} \nauthor : {self.author} \nisbn : {self.isbn} \nborrowed : {"yes" if self.is_borrowed else "no" "\n"}"
    

class Lib:

    def __dict__(Self):
        pass

    def __init__(self):
        self.books = []

    def add_book(self , book):
        self.books.append(book)
        print(f"book title : {book.title} added to the lib")

    def list_books(self):
        print("\nList of books present in the library :")
        if not self.books:
            print("no books in the library \n")
        for book in self.books:
            print(book)

lib1 = Lib()

lib1.list_books()

book1 = Book("Game Of Thrones" , "George R.R. Martin" , "123456789" )
# book2 = Book("Deep Learning" , "Ian Goodfellow, Yoshua Bengio, and Aaron Courville" , "987654321" )
# book3 = Book("Designing Machine Learning Systems" , "Chip Huyen" , "135792468" )
# book4 = Book("Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" , "Aurélien Géron." , "246813579" )

print(book1)
print("\n")

lib1.add_book(book1)
lib1.add_book(Book("One Piece" , "Eiichiro Oda" , "000000001"))


lib1.list_books()