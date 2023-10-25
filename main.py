def mainfunc():
    #initialize the bookslist
    bookslist=[]
    try:
        with open("thebookslist.txt", "r") as infile:
            line=infile.readline()
            while line:
                bookslist.append(line.rstrip("\n").split(","))
                line=infile.readline()
    except FileNotFoundError:
        print("No <bookslist> was found.")
        print("Start a new booklist.")


    choice=0
    while choice != 4:
        print("""
***Welcome to book store***
1.Add a book.
2.Look up for book.
3.Display book
4.Quit
    """)
        choice=int(input())
        if choice==1:
            print("Adding a book >>>>")
            bk_name=input("Enter the name of the book: ")
            author=input("Enter the author of the book: ")
            pages=input("Enter number of pages: ")
            bookslist.append([bk_name, author, pages])
        elif choice==2:
            print("Looking up for the book>>>")
            keyword=int("Enter search item: ")
            for book in bookslist:
                if keyword in book:
                    print(book)
        elif choice==3:
            print("The books display ...")
            for i in range(len(bookslist)):
                print(bookslist[i])
        elif choice==4:
            print("Exiting the program")
    print("Program terminated!")

    #save the books in an external .txt file.
    with open("thebookslist.txt", "w") as outfile:
        for book in bookslist:
            outfile.write(",".join(book) + "\n")


    

if __name__ == "__main__":
    mainfunc()
