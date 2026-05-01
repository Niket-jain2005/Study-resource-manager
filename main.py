from utils.helper import load_books,save_books
def add_book():
    books=load_books()
    
    while True:
        title = input("Enter Book Title: ").strip().lower()
        if not title:
            print("Title cannot be empty")
            continue
        break
    while True:
        subject = input("Enter Book Subject: ").strip().lower()
        if not subject:
            print("Subject cannot be empty")
            continue
        break

    while True:
        try:
            price = int(input("Enter Price: "))
            if price < 0:
                print("Price must be greater than or equal to 0")
                continue
            break
        except:
            print("Invalid Price")
    
    description = input("Enter Description: ").strip().lower()

    book = {
        "title": title,
        "subject": subject,
        "price": price,
        "description": description
    }

    books.append(book)
    save_books(books)

    print("\nBook Saved Successfully!\n")
    input("Press Enter to continue...")

def view_books():
    books = load_books()

    if not books:
        print("No Books Found")
        return

    print("\n==== BOOK LIST ====\n")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title'].title()} - ₹{book['price']}")
        print(f"   Subject: {book['subject'].title()}")
        print(f"   Description: {book['description'].capitalize()}\n")


def search_books():
    books=load_books()
    key=input("Enter keyword : ").lower()
    result=[]

    for b in books:
        if key in b["title"] or key in b["subject"] or key in b["description"]:
            result.append(b)
    
    if not result:
        print("No matching books")
    else:
        print(f"\nFound {len(result)} books:\n")
        for i, b in enumerate(result,1):
            print(f"{i}. {b['title'].title()} - ₹{b['price']} ({b['subject'].title()})")

def filter_by_price(min_price,max_price):
    books=load_books()
    result=[]

    for b in books:
        if min_price<=b["price"] <=max_price:
            result.append(b)
    
    if not result:
        print("No books found in this price range")
    else:
        print(f"\nFound {len(result)} books: \n")
        for i,b in enumerate(result,1):
            print(f"{i}. {b['title'].title()} - ₹{b['price']}")       
    
def delete_book():
    books=load_books()

    if not books:
        print("No books to delete")
        return
    
    print("\n====Choose Book Number TO Delete====\n")

    view_books()

    while True:
        try:
            choice=int(input("Enter book number to delete : "))
            if choice > 0 and choice<=len(books):
                break
            else:
                print(f"Invalid input. Your choice must be between 1 and {len(books)}.Please try again.")
        except:
            print("Enter Valid Choice")
    
    books.pop(choice-1)
    save_books(books)

    print("Book deleted successfully")

def update_book():
    books=load_books()

    if not books:
        print("No book to update")
        return
    
    view_books()

    while True:
        try:
            index=int(input("Enter book number to update : "))
            
            if index <= 0 or index > len(books): 
                print(f"Enter number between 1 and {len(books)}")
                print("Try again")
                continue
            break
        except:
            print("Enter a valid number")
            print("Try again")

    book=books[index-1]

    for key in book:
        print(f"old {key.title()} - {book[key]}")
       
        new_value=input(f"Enter new {key.title()} (leave blank to keep old) : ").strip()

        if not new_value:
            continue

        if key=="price":
            try:
                new_value=int(new_value)
                if new_value<0:
                    print("Invalid price, must be a positive number")
                    continue
            except:
                print("Invalid price, must be a positive number")
                continue


        book[key] = new_value.lower() if key != "price" else new_value
        print(f"{key.title()} changed successfully")
    
    save_books(books)
    print("Book updated successfully")
    input("Press Enter to continue...")


        
    



while True:            
    print("====MENU====\n")
    print("1 = Add Book")
    print("2 = View")
    print("3 = Search")
    print("4 = Filter by Price")
    print("5 = Delete Book")
    print("6 = Update Book")
    print("7 = Exit")
    try:
        choice=int(input(f"Enter Your Choice : "))
    except:
        print("Invalid input (Enter number)")
        continue


    if choice==1:
        add_book()
    elif choice==2:
        view_books()
    elif choice==3:
        search_books()
    elif choice==4:
        while True:
            try:
                min_price = int(input("Enter Minimum Price: "))
                max_price = int(input("Enter Maximum Price: "))
                if min_price>max_price:
                    print("Minimum price cannot be greater than maximum price")
                    continue
                break
            except:
                print("Invalid input, enter numbers only")
        filter_by_price(min_price,max_price)
    elif choice==5:
        delete_book()
    elif choice==6:
        update_book()
    elif choice==7:
        print("\n====BYE====\n")
        break
    else:
        print("Invalid choice")
