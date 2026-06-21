from pathlib import Path
import json
import string
from textwrap import indent
path=Path(__file__).parent / "data.json"

def view():
    if path.exists() and path.read_text():
        data=json.loads(path.read_text())
    else: data=[]
    return data

data=view()
class Book:
    bookId=1
    def add_book(self,book):
        self.book=book
        self.bookId=Book.bookId
        Book.bookId+=1
        newbook={
            "book":self.book,
            "bookId":self.bookId
        }
        data.append(newbook)
        path.write_text(json.dumps(data,indent=4))

    def view_all(self):
        data=view()
        print(data)

obj1=Book()
obj1.add_book("It ends with us")
obj1.view_all()