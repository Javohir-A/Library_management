import random

class Book:
    def __init__(self, title: str, author: str, publication_year: int, available_quantitiy: int) -> None:
        self.author = author
        self.publication_year = publication_year
        self.title = title
        self.available_quantitiy = available_quantitiy
    def check_out(self):
        if self.available_quantitiy > 0:
            self.available_quantitiy -= 1
            print(f"Checked out: {self.title}")
        else:
            print(f"Sorry, {self.title} is not available for checkout.")

    def return_book(self):
        self.available_quantitiy += 1
        print(f"Returned: {self.title}")
    
    def set_quantitiy(self, new_quantitiy: int):
        self.available_quantitiy = new_quantitiy

    def info_book(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nPuplication year: {self.publication_year}\nAvailabe: {self.available_quantitiy}\n'

class User:
    check_out_list = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.ID = random.randint(10000000,99999999)
        
    def check_out(self, library: "Library"):
        self.library = library
        
        if self.ID in [x.ID for x in library.return_user_info()]:
            print(library.display_available_books())
            index_book = int(input("Choose the index of a book you want borrow\n"))
            try:
                check_out_book = library.available_books[index_book-1]
                check_out_book.check_out()
                self.check_out_list.append(check_out_book)
                print(f"{check_out_book.title} is added to your list successfully!")

            except IndexError as indxerr:
                print('Invalid index you entered!\nPlease try again!')
        else:
            print(f"You are not joined to {library.name} library\nPlease, join and try again!")
    
    def display_check_out_list(self):
        for i, book in enumerate(self.check_out_list):
            print(i+1,book.title)

    def return_book(self, library: "Library"):
        self.display_check_out_list()
        index_book = int(input("Choose the index of a book you want to return\n"))
        try:
            Returned_book = self.check_out_list[index_book-1]
            library.user_list.remove(self)
            Returned_book.return_book()
        except IndexError:
            print('Invalid index you entered!\nPlease try again!')

class Library:
    available_books = []
    user_list = [] 

    def __init__(self, name: str) -> None:
        self.name = name
    
    def add_user(self, user: User):
        self.user_list.append(user)

    def add_book(self, book: Book):
        self.available_books.append(book)
    
    def display_available_books(self):
        for index, book in enumerate(self.available_books):
            print(f"{index+1}")
            print(book.info_book())
        # print(self.user_list[0].ID)

    def remove_book(self):
        self.display_available_books()
        index_book = int(input("Choose the index of a book you wnat to remove"))
        try:
            removal_book = self.available_books[index_book-1]
            self.available_books.remove(removal_book)
        except IndexError as indxerr:
            print('Invalid index you entered!\nPlease try again!')
    def return_user_info(self):
        return self.user_list
        




book1 = Book('The 48 Laws Of Power', "Robert Greene", 2012, 3)
book2 = Book('Atomic Habits', 'James Clear', 2018, 26)
book3 = Book('1984', 'George Orwell', 2004, 5)

library = Library('Tashkent')
User1 = User('javohir')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_available_books()

library.add_user(User1)

User1.check_out(library)
User1.check_out(library)
User1.display_check_out_list()
for x in library.return_user_info():
    print(x.name)

User1.return_book(library)
User1.display_check_out_list()

for x in library.return_user_info():
    print(x.name)
# library.display_available_books()

# library.remove_book()
# library.display_available_books()