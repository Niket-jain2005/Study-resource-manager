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