import json
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

FileBook = open('books.json')

BookJson = json.load(FileBook)

#Get all books
@app.get("/books")
def get_all_book():
    return {"data": BookJson}
