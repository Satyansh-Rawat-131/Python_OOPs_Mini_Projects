class Book:

    def __init__(self , title , author , isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"title : {self.title} \nauthor : {self.author} \nisbn : {self.isbn} \nborrowed : {"yes" if self.is_borrowed else "no"}"


book1 = Book("Game Of Thrones" , "George R.R. Martin" , "123456789" )
book2 = Book("Deep Learning" , "Ian Goodfellow, Yoshua Bengio, and Aaron Courville" , "987654321" )
book3 = Book("Designing Machine Learning Systems" , "Chip Huyen" , "135792468" )
book4 = Book("Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" , "Aurélien Géron." , "246813579" )

print(book1)