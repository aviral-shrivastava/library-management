class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lenddict = {}

    def displayBooks(self): #To dispaly the name of the books
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book): #To garnt a book to the user
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Book has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lenddict[book]}.") #If someone already has the book

    def addBook(self, book):
        self.booksList.append(book) #To add a book in the list of books
        print("Book has been added to the book list.")

    def returnBook(self, book):
        self.lenddict.pop(book) #To remove the book from lent dictionary


if __name__ == '__main__': #To assign the name of the books and name of the org
    mylib = Library(['Macbeth', 'Merchant of venice', 'The tempest', 'Much ado about nothing', 'Romeo and Juliet'], "Shakespearen")


    while(True): #To take the  choice of the user

        print(f"Welcome to the {mylib.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Borrow a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = input()

        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            mylib.displayBooks() #calling the respective function

        elif user_choice == 2:
            book = input("Enter the name of the book you want to borrow: ")
            user = input("Enter your name: ")
            mylib.lendBook(user, book) #calling the respective function


        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            mylib.addBook(book) #calling the respective function


        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            mylib.returnBook(book) #calling the respective function


        else:
            print("Not a valid option.Please  enter a valid option") #If wrong option is entered.
            


        print("Press q to quit and c to continue")
                          
        your_choice=""
        while(your_choice!="c" and your_choice!="q"):
            your_choice = input()
            if your_choice == "q":
                exit() #To exit from the loop

            elif your_choice == "c":
                continue #To continue with the code.

