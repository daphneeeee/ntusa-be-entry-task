from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    id: int
    author: str
    title: str
    content: str
    time: datetime

    class Config:
        orm_mode = True


class Comment(BaseModel):
    id: int
    post_id: int
    author: str
    content: str
    time: datetime

    class Config:
        orm_mode = True
