import json
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

FileBook = open('books.json')

BookJson = json.load(FileBook)

class Post(BaseModel):
    author: str
    country: str
    imageLink: str
    language: str
    link: str
    pages: int
    title: str
    year: int

#Get all books
@app.get("/books")
def get_all_book():
    return {"Books": BookJson}

#Post a new post(Create)
@app.post("/books", status_code =status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["pages"] = len(BookJson) + 1
    BookJson.append(post_dict)
    return{"Books": BookJson}
