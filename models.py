from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    author = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    time = Column(DateTime, nullable=False)

    # comment = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    author = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    time = Column(DateTime, nullable=False)

    # comment = relationship("Post", back_populates="post")
