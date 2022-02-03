# '''Create a library class
# display book
# lend book
# add book
# return book
# AkashLibrary=Library(listofBooks,library_name)
# dict(books=name_person)
# create a main function and run an infinite while loop asking users for their input'''
class Library():
    name=""
    def __init__(self,LibraryName="userLib",listOfBooks=[]) -> None:
        self.availableBooks=dict() #all available books in library and value as their count.Add new books in it 
        self.lendedBooks=dict()#books which are lended to user(book-nooflended)
        self.name=LibraryName
        for book in listOfBooks:
            self.addBooks(book)
    def addBooks(self,book):
        if book not in self.availableBooks:
            self.availableBooks[book]=0
        self.availableBooks[book]+=1
        print(f"{book} book is added")
    def displayBook(self):
        print("Displaying Books:")
        print(f"Books       NoOfBooks")
        for book,count in self.availableBooks.items():
            print(f"{book:>8}  {count:^10}\n")
    def displayLendedBook(self):
        print(f"Books       NoOfBooks")
        for book,count in self.lendedBooks.items():
            print(f"{book:>8}  {count:^10}\n")
    def lendBooks(self,book):
        NoOfBookPresent=self.availableBooks.get(book,0)
        NoOfBookLended=self.lendedBooks.get(book,0)
        NoOfBookAvail=NoOfBookPresent-NoOfBookLended
        if NoOfBookAvail>0:
            if book not in self.lendedBooks:
                self.lendedBooks[book]=0
            self.lendedBooks[book]+=1
            print(f"{book} book is handed to you")
        else:
            print(f"Sorry! {book} Book is not Available")
    def returnBooks(self,book):
        if book not in self.lendedBooks:
            print("It is not our book")
        elif book in self.lendedBooks:
            if self.lendedBooks[book]==1:
                del self.lendedBooks[book]
            self.lendedBooks[book]-=1

listofBooks=["Techmax","NCERT","Huddy","Slate","Wanda","Techmax","Slate"]
library_name="AkashLibrary"
AkashLibrary=Library(library_name,listofBooks)
while(True):
    choice=int(input("Enter 1 for Display Book\n2 for Lend Book\n3 for add Book\n4 for Return Book\n5 for Display Lended Book:"))
    if choice==1:
        AkashLibrary.displayBook()
    elif choice==2:
        book=input("Enter the name of Book:")
        AkashLibrary.lendBooks(book)
    elif choice==3:
        book=input("Enter the name of Book:")
        AkashLibrary.addBooks(book)
    elif choice==4:
        book=input("Enter the name of Book:")
        AkashLibrary.returnBooks(book)
    elif choice==5:
        AkashLibrary.displayLendedBook()
    else:
        break


