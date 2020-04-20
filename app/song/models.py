from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum
from sqlalchemy.orm import relationship
import uuid
import enum
from datetime import datetime
from app.queue.models import Queue
from app.db import db


class SongCategory(db.Model):
    """
    Establishes a many to many relationship between relations 'song' and 'category'
    """
    __tablename__ = 'song_category'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey('category.id'), nullable=False)
    song_id = Column(UUID(as_uuid=True), ForeignKey('song.id'), nullable=False)

    song = relationship("Song", back_populates="categories")
    category = relationship("Category", back_populates="songs")

class Song(db.Model):
    __tablename__ = 'song'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String(255))
    artist = Column(String(255))
    picture_url = Column(String(500))
    youtube_title = Column(String(255))
    youtube_url = Column(String(500))
    file_path = Column(String(500))
    meta = Column(JSON)
    duration = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    #queue_entries = relationship('Queue', order_by=Queue.position, back_populates='song') #FIXME: order_by might not work
    queue_entries = relationship('Queue', back_populates='song')

    categories = relationship(
        "SongCategory",
        back_populates="song"
    )

class CategoryType(enum.Enum):
    CHILL = 'CHILL'
    HYPE = 'HYPE'
    HIP_HOP = 'HIP_HOP'
    INDIE = 'INDIE'
    R_B = 'R_B'
    
class Category(db.Model):
    __tablename__ = 'category'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    category = Column(Enum(CategoryType), unique=True, nullable=False)
    songs = relationship(
        "SongCategory",
        back_populates="category"
    )
