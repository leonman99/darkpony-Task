from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Content(Base):
    __tablename__ = "content"

    # id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")


class Section(Base):
    __tablename__ = "section"

    # id = Column(Integer, primary_key=True, index=True)
    # title = Column(String, index=True)
    # description = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="items")


class Content-to-sections(Base):
    __tablename__ = "content-to-section"