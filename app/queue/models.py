from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, Enum
from sqlalchemy.orm import relationship
import uuid
import enum
from datetime import datetime

from app.db import db

class QueueStatus(enum.Enum):
    PLAYING = 'PLAYING'
    UPCOMING = 'UPCOMING'
    PLAYED = 'PLAYED'
    REMOVED = 'REMOVED'
    SKIPPED = 'SKIPPED'

class Queue(db.Model):
    __tablename__ = 'queue'
    position = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True, index=True)
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True)
    song_id = Column(UUID(as_uuid=True), ForeignKey('song.id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    status = Column(Enum(QueueStatus), nullable=False, default=QueueStatus.UPCOMING)
    user_request = Column(Boolean, default=False)
    requested_at = Column(DateTime, nullable=False)
    current_second = Column(Integer, nullable=False, default=0)
    played_at = Column(DateTime)

    song = relationship("Song", back_populates='queue_entries')
    user = relationship("User", back_populates='song_requests')

    def to_dict(self) -> dict:
        return {
            'id': str(self.id),
            'user_request': self.user_request,
            'song': self.song.to_dict(),
            'added_by': self.user.to_dict() if self.user else None,
            'status': self.status.value,
            'current_second': self.current_second
        }
