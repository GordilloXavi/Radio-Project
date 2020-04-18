from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum
import uuid
import enum

from app.db import db

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
    duration = Column(Integer) # seconds
    created_at = Column(DateTime, default=func.now(), nullable=False)

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

class SongCategory(db.Model):
    """
    Establishes a many to many relationship between relations 'song' and 'category'
    """
    __tablename__ = 'song_category'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey('category.id'))
    song_id = Column(UUID(as_uuid=True), ForeignKey('song.id'))
