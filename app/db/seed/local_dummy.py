import uuid
from datetime import datetime, timezone

from app.db.client import SessionLocal
from app.db.models import Answer, Question, Visitor
from logger import logger


def seed() -> None:
    with SessionLocal() as session:
        try:
            now = datetime.now(tz=timezone.utc)

            # Visitor 1
            visitor1 = Visitor(id=uuid.uuid4(), created_at=now, name="Jesse")
            question1 = Question(
                id=uuid.uuid4(),
                visitor_id=visitor1.id,
                created_at=now,
                text="What's your favorite color?",
            )
            answer1a = Answer(
                id=uuid.uuid4(),
                question_id=question1.id,
                created_at=now,
                updated_at=now,
                text="Red",
                rank=0,
                votes=0,
            )
            answer1b = Answer(
                id=uuid.uuid4(),
                question_id=question1.id,
                created_at=now,
                updated_at=now,
                text="Blue",
                rank=1,
                votes=0,
            )

            # Visitor 2
            visitor2 = Visitor(id=uuid.uuid4(), created_at=now, name="James")
            question2 = Question(
                id=uuid.uuid4(),
                visitor_id=visitor2.id,
                created_at=now,
                text="Best season of the year?",
            )
            question3 = Question(
                id=uuid.uuid4(),
                visitor_id=visitor2.id,
                created_at=now,
                text="Favorite pet?",
            )

            answers2 = [
                Answer(
                    id=uuid.uuid4(),
                    question_id=question2.id,
                    created_at=now,
                    updated_at=now,
                    text="Summer",
                    rank=0,
                    votes=0,
                ),
                Answer(
                    id=uuid.uuid4(),
                    question_id=question2.id,
                    created_at=now,
                    updated_at=now,
                    text="Fall",
                    rank=1,
                    votes=0,
                ),
                Answer(
                    id=uuid.uuid4(),
                    question_id=question2.id,
                    created_at=now,
                    updated_at=now,
                    text="Winter",
                    rank=2,
                    votes=0,
                ),
            ]

            answers3 = [
                Answer(
                    id=uuid.uuid4(),
                    question_id=question3.id,
                    created_at=now,
                    updated_at=now,
                    text="Dog",
                    rank=0,
                    votes=0,
                ),
                Answer(
                    id=uuid.uuid4(),
                    question_id=question3.id,
                    created_at=now,
                    updated_at=now,
                    text="Cat",
                    rank=1,
                    votes=0,
                ),
                Answer(
                    id=uuid.uuid4(),
                    question_id=question3.id,
                    created_at=now,
                    updated_at=now,
                    text="Bird",
                    rank=2,
                    votes=0,
                ),
            ]

            session.add_all(
                [
                    visitor1,
                    question1,
                    answer1a,
                    answer1b,
                    visitor2,
                    question2,
                    question3,
                    *answers2,
                    *answers3,
                ]
            )
            session.commit()
            print("✅ Seed data inserted successfully.")
            logger.info("✅ Seed data inserted successfully.")
        except Exception:
            session.rollback()
            logger.exception("❌ Error during seed:")


def retrieve() -> None:
    with SessionLocal() as session:
        try:
            visitors = session.query(Visitor).all()
            for visitor in visitors:
                logger.info(f"Visitor: {visitor.name} ({visitor.id})")
                for question in visitor.questions:
                    logger.info(f"  Question: {question.text} ({question.id})")
                    sorted_answers = sorted(question.answers, key=lambda a: a.rank)
                    for answer in sorted_answers:
                        logger.info(
                            f"    Answer: {answer.text} (votes: {answer.votes}, rank: {answer.rank})"
                        )
        except Exception:
            logger.exception("❌ Error during retrieve:")


if __name__ == "__main__":
    seed()
    retrieve()
