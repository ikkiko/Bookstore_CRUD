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


#Post a new post(Create)
@app.post("/books", status_code =status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    BookJson.append(post_dict)
    with open("books.json", "w") as FileBook:
        json.dump(BookJson, FileBook, indent=4)   
    return{"Books": BookJson}
    

#with open('books.json' , 'w') as FileBook:
 #   json.dumps(BookJson,FileBook)

if 0:
    with open("books.json", "w") as FileBook:
        json.dump(BookJson, FileBook, indent=4)
        #FileBook.write(json.dump(BookJson, FileBook, indent=4))

if 0:
    TextJson.append(TestBook)
    with open("textbook.json", "w") as TextBook:
        json.dump(TextJson, TextBook, indent=4)
        #TextBook.write(json.dump(TextJson, TextBook, indent=4))    