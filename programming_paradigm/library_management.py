class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out__ = False

    def check_out_book(self):
        if self.__is_checked_out__ == False:
            self.__is_checked_out__ = True
            return True
        else: return False

    def return_book(self):
        if self.__is_checked_out__ == True:
            self.__is_checked_out__ = False
            return True
        else: return False

class Library:
    
    def __init__(self):
        self.__books__ = []

    def add_book(self, book):
        if (type(book)= Book):
            self.__books__.append(book)
    
    def check_out_book(self,title):
        done = False
        for i in self.__books__:
            if i.title == title and i.check_out_book():
                i.check_out_book()
                done = True
                break
        return done    
    
    def return_book(self,title):
        done = False
        for i in self.__books__:
            if i.title == title and i.return_book():
                i.return_book()
                done = True
                break
        return done 

    def list_available_books(self):
        available = []
        for i in self.__books__:
            if i.__is_checked_out__ == False:
                available.append(i.title)
        return available
