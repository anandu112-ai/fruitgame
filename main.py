from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

words = [
    "mango","apple","orange","banana",
    "guava","cherry","grape","jackfruit",
    "kiwi","papaya"
]

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html") as f:
        return f.read()

@app.get("/start")
def start():
    word = random.choice(words)
    return {"word": word}
