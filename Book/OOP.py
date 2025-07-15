class Book():
    def __init__(self, title, author, pages, current_page, is_Open):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_Open = False


    def __str__(self):
        return f"The book '{self.title}' is written by {self.author} and has {self.pages} pages."
    

    def open_book(self):
        self.is_Open = True
        print(f"Book is now open")

    def close_book(self):
        self.is_Open = False
        print(f"Book is now closed")

    def turn_page(self):
        if (self.is_Open == True and self.current_page < self.pages):
            self.current_page = self.current_page + 1
            print(f"Turned Page To: {self.current_page}")
        else:
            print(ValueError("Error lil bro"))
    
    def is_long_book(self):
        if (self.pages > 300):
            return True
        else:
            return False

    def go_to_page(self, num):
        if (num < self.pages and self.is_Open == True ):
            self.current_page = num
            print(f"Current page is now: {self.current_page}")
        else:
            print(f"ERROR going to page")
    
    def go_to_pagev2(self):
         if (self.is_Open == True):
            num = int(input("What page number would you like to go to? "))
         if (num < self.pages):
            self.current_page = num
            print(f"Current page is now: {self.current_page}")



TheBook = Book("The Book", "Jay P", 55, 1, False)

TheBook.open_book()
TheBook.turn_page()
TheBook.go_to_page(43)
TheBook.go_to_page(78)
TheBook.go_to_pagev2()
TheBook.close_book()

