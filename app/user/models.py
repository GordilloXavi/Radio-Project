from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime

import uuid

from app.db import db

class User(db.Model):
    __tablename__ = 'user'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(20), index=True, unique=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    last_seen = Column(DateTime, default=datetime.now(), nullable=False)

    song_requests = relationship('Queue', back_populates='user')

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'last_seen': self.last_seen
        }