import json
file_path="data/books.json"

def load_books():
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading data:", e)
        return []

def save_books(books):
    with open(file_path,"w") as f:
        json.dump(books,f,indent=4)

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
    

while True:            
    print("====MENU====\n")
    print("1 = Add Book")
    print("2 = View")
    print("3 = Search")
    print("4 = Filter by Price")
    print("5 = Exit")
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
        print("\n====BYE====\n")
        break
    else:
        print("Invalid choice")
