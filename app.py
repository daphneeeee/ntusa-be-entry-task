from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime

import crud
import models
import schema
from database import SessionLocal, engine

from config import app_config

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=app_config.title,
    docs_url=app_config.docs_url,
    redoc_url=app_config.redoc_url,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/post', response_model=list[schema.Post])
def browse_post(db: Session = Depends(get_db)) -> [schema.Post]:
    return crud.browse_post(db=db)


@app.get('/post/{post_id}', response_model=schema.Post)
def read_post(post_id: int, db: Session = Depends(get_db)) -> schema.Post:
    return crud.read_post(db=db, post_id=post_id)


@app.post('/post/', response_model=int)
def add_post(author: str, title: str, content: str, db: Session = Depends(get_db)) -> int:
    time = datetime.now()
    post_id = crud.add_post(db=db, author=author, title=title, content=content, time=time)
    return post_id


@app.patch('/post/{post_id}')
def edit_post(post_id: int, title: str = None, content: str = None, db: Session = Depends(get_db)) -> None:
    time = datetime.now()
    crud.edit_post(db=db, post_id=post_id, time=time, title=title, content=content)


@app.delete('/post/{post_id}')
def delete_post(post_id: int, db: Session = Depends(get_db)) -> None:
    crud.delete_post(db=db, post_id=post_id)


@app.post('/post/{post_id}/comment', response_model=int)
def add_comment(post_id: int, author: str, content: str, db: Session = Depends(get_db)) -> schema.Comment:
    time = datetime.now()
    comment_id = crud.add_comment(db=db, post_id=post_id, author=author, content=content, time=time)
    return comment_id
