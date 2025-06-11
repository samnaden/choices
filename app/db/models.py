from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(UUID(as_uuid=True), primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    name = Column(String(100), nullable=False)

    questions = relationship("Question", back_populates="visitor")


class Question(Base):
    __tablename__ = "questions"

    id = Column(UUID(as_uuid=True), primary_key=True)
    visitor_id = Column(UUID(as_uuid=True), ForeignKey("visitors.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    text = Column(Text, nullable=False)

    visitor = relationship("Visitor", back_populates="questions")
    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(UUID(as_uuid=True), primary_key=True)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

    text = Column(Text, nullable=False)
    rank = Column(Integer, nullable=False)
    votes = Column(Integer, nullable=False)

    question = relationship("Question", back_populates="answers")

    __table_args__ = (
        CheckConstraint("rank >= 0", name="check_rank_non_negative"),
        CheckConstraint("votes >= 0", name="check_votes_non_negative"),
    )
