'''Problem statement'''
'''Create a Simple library management system'''

class Library:
    def __init__(self,books):
        self.availableBooks = books 

    def displayAvailableBooks(self):
        print("\nAvailable Books: ")
        [print(i) for i in self.availableBooks]
    def lendBook(self, requestedBook):
        if(requestedBook in self.availableBooks):
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book isn't available in out list.")
    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("You've returned the book. Thank You!")

class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book

library = Library(['Book1','Book2','Book3'])
customer =Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to retuern a book")
    print("Enter 4 to exit")
    choice = int(input())
    if(choice is 1):
        library.displayAvailableBooks()
    elif(choice is 2):
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif(choice is 3):
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif(choice is 4):
        quit()
