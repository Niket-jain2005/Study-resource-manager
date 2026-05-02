from utils.helper import load_books,save_books

def display_books(books):
    if not books:
        print("No Books Found")
        return

    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title'].title()} - ₹{book['price']}")
        print(f"   Subject: {book['subject'].title()}")
        print(f"   Description: {book['description'].capitalize()}\n")


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
        except ValueError:
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
    display_books(books)

def search_books():
    books=load_books()
    key=input("Enter keyword : ").lower()
    if not key.strip():
        print("Keyword cannot be empty")
        return
    result=[]

    for b in books:
        if key in b["title"] or key in b["subject"] or key in b["description"]:
            result.append(b)
    
    if not result:
        print("No matching books")
    else:
        print(f"\nFound {len(result)} books:\n")
        display_books(result)
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
        display_books(result)

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
        except ValueError:
            print("Enter Valid Choice")
    
    books.pop(choice-1)
    save_books(books)

    print("Book deleted successfully")
    input("Press Enter to continue...")

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
        except ValueError:
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
            except ValueError:
                print("Invalid price, must be a positive number")
                continue


        book[key] = new_value.lower() if key != "price" else new_value
        print(f"{key.title()} changed successfully")
    
    save_books(books)
    print("Book updated successfully")
    input("Press Enter to continue...")

def sort_books():
    books=load_books()

    if not books:
        print("No book to sort")
        return
    print("1. Low to High")
    print("2. High to Low")
    while True:
        try:
            sort_choice=int(input("Enter choice 1 or 2 : "))
            if sort_choice not in [1, 2]:
                print("Enter choice 1 or 2")
                print("Try again")
                continue
            break            
        except ValueError:
            print("Invalid choice")
            print("Try again")
    
    if sort_choice==1:
        sorted_books=sorted(books,key= lambda x:x["price"])
    else:
        sorted_books=sorted(books,key= lambda x:x["price"], reverse=True)
    
    print("\n====SORTED BOOK LIST ====\n")
    display_books(sorted_books)

def show_stats():
    books=load_books()

    if not books:
        print("No books available")
        return
    
    total_books=len(books)
    total_price=0

    max_price_book=""
    max_price=0

    min_price_book=""
    min_price=float("inf")

    for book in books:
        total_price += book["price"]
        if book["price"]>max_price:
            max_price=book["price"]
            max_price_book=book["title"]
        if book["price"]<min_price:
            min_price=book["price"]
            min_price_book=book["title"]

    average_price=total_price / total_books

    print("\n==== STATS ====\n")

    print(f"Total Books: {total_books}")
    print(f"Average Price: ₹{average_price:.2f}")
    print(f"\nHighest Price Book:\n{max_price_book.title()} - ₹{max_price}")  
    print(f"\nLowest Price Book:\n{min_price_book.title()} - ₹{min_price}")
    

while True:            
    print("\n====MENU====\n")
    print("1. Add Book")
    print("2. View")
    print("3. Search")
    print("4. Filter by Price")
    print("5. Delete Book")
    print("6. Update Book")
    print("7. Sort by Price")
    print("8. Show Stats")
    print("9. Exit")
    try:
        choice=int(input(f"Enter Your Choice : "))
    except ValueError:
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
            except ValueError:
                print("Invalid input, enter numbers only")
        filter_by_price(min_price,max_price)
    elif choice==5:
        delete_book()
    elif choice==6:
        update_book()
    elif choice==7:
        sort_books()
    elif choice==8:
        show_stats()
    elif choice==9:
        print("\n====BYE====\n")
        break
    else:
        print("Invalid choice")
