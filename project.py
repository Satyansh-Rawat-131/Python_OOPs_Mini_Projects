class Book:

    def __init__(self , title , author , isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"title : {self.title} \nauthor : {self.author} \nisbn : {self.isbn} \nborrowed : {"yes" if self.is_borrowed else "no"}"
