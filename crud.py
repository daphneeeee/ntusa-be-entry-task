from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

import models
import schema


def browse_post(db: Session) -> [schema.Post]:
    posts = db.query(models.Post).all()
    if not posts:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return posts


def read_post(db: Session, post_id: int) -> schema.Post:
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return post


def edit_post(db: Session, post_id: int, time: datetime, title: str = None, content: str = None) -> None:
    if not (title or content):
        return

    if title:
        db.query(models.Post).filter(models.Post.id == post_id).update({"title": title, "time": time})
    if content:
        db.query(models.Post).filter(models.Post.id == post_id).update({"content": content, "time": time})
    db.commit()


def add_post(db: Session, author: str, title: str, content: str, time: datetime) -> int:
    new_post = models.Post(author=author, title=title, content=content, time=time)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post.id


def delete_post(db: Session, post_id: int) -> None:
    deleted_post = db.query(models.Post).filter(models.Post.id == post_id).delete()
    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.commit()


def add_comment(db: Session, post_id: int, author: str, content: str, time: datetime) -> schema.Comment:
    if not db.query(models.Post).filter(models.Post.id == post_id).first():
        raise HTTPException(status_code=404, detail="Post not found")

    new_comment = models.Comment(post_id=post_id, author=author, content=content, time=time)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment.id
