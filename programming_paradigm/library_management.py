class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out__ = False

    

class Library:
    
    def __init__(self):
        self.__books__ = []

    def add_book(self, book):
        if (type(book)= Book):
            self.__books__.append(book)
    
    def check_out_book(self, title):
        for i in self.__books__:
            if title == i.title and i.__is_checked_out__ == False:
                i.__is_checked_out__ = True

    def return_book(self, title):
        for i in self.__books__:
            if title == i.title and i.__is_checked_out__ == True:
                i.__is_checked_out__ = False

    def list_available_books(self):
        available = []
        for i in self.__books__:
            if i.__is_checked_out__ == False:
                available.append(i.title)
        return available
