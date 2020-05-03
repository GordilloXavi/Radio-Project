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
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=True)
    artist = Column(String(255)) #TODO: support multiple artists or concatenate them
    picture_url = Column(String(1024))
    yt_title = Column(String(255))
    yt_url = Column(String(1024), index=True) #FIXME: youtube_id 
    yt_thumbnail_url = Column(String(1024))
    yt_meta = Column(JSON)
    spotify_meta = Column(JSON)
    duration = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    
    added_by = relationship("User", back_populates='added_songs')

    queue_entries = relationship('Queue', back_populates='song')

    categories = relationship(
        "SongCategory",
        back_populates="song"
    )

    def to_dict(self) -> dict:
        return {
            'id': str(self.id),
            'title': self.title,
            'artist': self.artist,
            'picture_url': self.picture_url,
            'youtube_title': self.yt_title,
            'youtube_url': self.yt_url,
            'duration': self.duration,
            'categories': [c.category.name.value for c in self.categories],
            'youtube_thumbnail_url': self.yt_thumbnail_url,
            'youtube_meta': self.yt_meta
        }

class CategoryType(enum.Enum):
    CHILL = 'CHILL'
    HYPE = 'HYPE'
    HIP_HOP = 'HIP_HOP'
    INDIE = 'INDIE'
    R_B = 'R_B'
    
class Category(db.Model):
    __tablename__ = 'category'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(Enum(CategoryType), unique=True, nullable=False)
    songs = relationship(
        "SongCategory",
        back_populates="category"
    )
