from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI(
    title='Поиск информации по заголовку(Wikipedia)'
)


@app.get("/{wiki}/")
def title(enter_word: str):
    wikipedia.set_lang('ru')
    return wikipedia.search(enter_word, results = 20)

@app.get("/wikiped")
def page(enter_title: str):
    wikipedia.set_lang('ru')
    return wikipedia.page(enter_title).content

class Wiki(BaseModel):
    title: str = 'FastAPI'
    sentences: int = 10


@app.post("/")
def parametrs_state(wiki: Wiki):
    return wiki.title + "" + wikipedia.summary(wiki.title, sentences = wiki.sentences)




