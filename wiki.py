from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI(
    title='Поиск информации по заголовку(Wikipedia)'
)


@app.get("/{text}/")
def title(text: str):
    wikipedia.set_lang('ru')
    return wikipedia.search(text)

@app.get("/wikiped")
def page(enter_title: str):
    wikipedia.set_lang('ru')
    return wikipedia.page(enter_title).content

class Wiki(BaseModel):
    title: str = 'Vkontakte'
    sentences: int = 10


@app.post("/")
def parametrs_state(wiki: Wiki):
    wikipedia.set_lang('ru')
    return wiki.title + "" + wikipedia.summary(wiki.title, sentences = wiki.sentences)


