import json
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

with open("books.json", "r") as FileBook:
    BookJson = json.load(FileBook)
if 0:
    with open("textbook.json", "r") as TextBook:
        TextJson = json.load(TextBook)

#FileBook = open('books.json')
#BookJson = json.load(FileBook)

class Post(BaseModel):
    author: str
    country: str
    imageLink: str
    language: str
    link: str
    pages: int
    title: str
    year: int
'''
TestBook = {
    "author": "Butterbear",
    "country": "Thailand",
    "imageLink": "butterbear.co.th",
    "language": "Thai",
    "link": "NongNeay.com",
    "pages": 3,
    "title": "NoeyNoi School",
    "year": 1993
}
'''
#Get all books
@app.get("/books")
def get_all_book():
    return {"Books": BookJson}


#Post a new book(Create)
@app.post("/books", status_code =status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    BookJson.append(post_dict)
    with open("books.json", "w") as FileBook:
        json.dump(BookJson, FileBook, indent=4)   
    return{"Books": BookJson}

#Get lastest book(Read)
@app.get("/books/lastest")
def get_latest_book():
    return {"Books": BookJson[-1]}

#Get books from year
@app.get("/books/{post_year}")
def get_books_by_year(post_year: int):
    book = find_year(post_year)
    if book is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Book with year {post_year} not Found")
    return {"Books": book}

def find_year(year):
    for book in BookJson:
        if book["year"] == year:
            return book
    return None

#Delete post by year
@app.delete("/books/{post_year}")
def delete_book_by_year(post_year: int):
    book_index = find_index_year(post_year)
    if book_index is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Book with this year {post_year} not Found")
    deleted_post = BookJson.pop(book_index)
    return {"message": f"Book with this year {post_year} has been deleted"}

#Update a book by year
@app.put("/books/{post_year}")
def update_post_by_id(post_year: int, post: Post):
    book_index = find_index_year(post_year)
    if book_index is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Book with year {post_year} not Found")
    post_dict = post.dict()
    post_dict["year"] = post_year
    BookJson[book_index] = post_dict
    return {"message": f"Book with year {post_year} has been updated"}

def find_index_year(year):
    for index, book in enumerate(BookJson):
        if book["year"] == year:
            return index
    return None 