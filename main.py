from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

words = [
    "mango","apple","orange","banana",
    "guava","cherry","grape","jackfruit",
    "kiwi","papaya"
]

secret_word=""
display=[]
chance=5


@app.get("/",response_class=HTMLResponse)
def home():
    with open("index.html") as f:
        return f.read()


@app.get("/start")
def start():

    global secret_word,display,chance

    secret_word=random.choice(words)
    display=["_"]*len(secret_word)
    chance=5

    return {"word":display,"chance":chance}


@app.get("/guess")
def guess(letter:str):

    global secret_word,display,chance

    letter=letter.lower()

    correct=False

    for i in range(len(secret_word)):
        if secret_word[i]==letter:
            display[i]=letter
            correct=True

    if not correct:
        chance-=1

    status="playing"

    if "_" not in display:
        status="won"

    if chance<=0:
        status="lost"

    return {
        "word":display,
        "chance":chance,
        "status":status,
        "answer":secret_word
    }
