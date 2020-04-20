from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from app.db import db

class Queue(db.Model):
    __tablename__ = 'queue'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    song_id = Column(UUID(as_uuid=True), ForeignKey('song.id')) #, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    played = Column(Boolean, default=False)
    user_request = Column(Boolean, default=False)
    played_at = Column(DateTime, default=datetime.now()) #FIXME: status instead of bool
    position = Column(Integer, autoincrement=True, nullable=False, unique=True)

    song = relationship("Song", back_populates='queue_entries')

    def to_dict(self) -> dict:
        return {} #TODO
