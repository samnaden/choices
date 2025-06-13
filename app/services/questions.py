import uuid
from datetime import datetime, timezone
from typing import cast

from sqlalchemy.orm import selectinload

from app.db.client import SessionLocal
from app.db.models import Answer, Question


def get_all_questions() -> list[Question]:
    with SessionLocal() as session:
        questions = cast(
            list[Question],
            session.query(Question)
            .options(selectinload(Question.answers), selectinload(Question.visitor))
            .order_by(Question.created_at)
            .all(),
        )

    return questions


def insert_question(
    visitor_id: uuid.UUID, question_text: str, options: list[str]
) -> None:
    now = datetime.now(tz=timezone.utc)

    with SessionLocal() as session:
        question = Question(
            id=uuid.uuid4(),
            visitor_id=visitor_id,
            text=question_text,
            created_at=now,
        )

        answers = [
            Answer(
                id=uuid.uuid4(),
                question_id=question.id,
                created_at=now,
                updated_at=now,
                text=option,
                rank=idx,
                votes=0,
            )
            for idx, option in enumerate(options)
        ]

        session.add(question)
        session.add_all(answers)
        session.commit()
