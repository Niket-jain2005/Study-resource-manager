import json
file_path="data/books.json"

def load_books():
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except:
        return []

def save_books(books):
    with open(file_path,"w") as f:
        json.dump(books,f,indent=4)

def add_books():
    books=load_books()

    title=str(input("Enter Book Title : ")).lower()
    subject=str(input("Enter Book Subject : ")).lower()
    price=int(input("Enter Price : "))
    description=str(input("Enter Other Details : "))
    book={
        "title" : title,
        "subject" : subject,
        "price" : price,
        "description" : description        
    }

    books.append(book)
    save_books(books)
    print("Book Saved Successfully!")


def view_books():
    books=load_books()
    if books:
        i=1
        for book in books:
            print(f"{i}.\n Title = {book['title']} \nSubject ={book['subject']} \nPrice = ₹{book['price']} \nDescription = {book['description']}")
            i+=1
    else:
        print("No Books Found")
def search_books():
    books=load_books()
    key=input("Enter keyword : ").lower()
    result=[]

    for b in books:
        if key in b["title"] or key in b["subject"]:
            result.append(b)
    
    if not result:
        print("No matching books")
    else:
        for i, b in enumerate(result):
            print(f"{i+1}. {b['title']} - ₹{b['price']}")
    
while True:            
    print("====MENU====\n")
    print("1 = Add \n2 = View \n3 = Search \n4 = Exit \n")
    choice=int(input(f"Enter Your Choice : "))

    if choice==1:
        add_books()
    elif choice==2:
        view_books()
    elif choice==3:
        search_books()
    elif choice==4:
        print("\n====BYE====\n")
        break
    else:
        print("===Invalid Input===")
    

