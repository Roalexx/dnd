from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models import Base
from models.player.character import Character

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    characters = relationship(
        "Character",
        back_populates="user",
        foreign_keys=[Character.user_id],  # ✅ DİKKAT: str değil, direkt referans
        cascade="all, delete-orphan"
    )

    managed_characters = relationship(
        "Character",
        back_populates="dungeon_master",
        foreign_keys=[Character.dungeon_master_id]
    )
