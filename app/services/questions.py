from typing import cast

from sqlalchemy.orm import selectinload

from app.db.client import SessionLocal
from app.db.models import Question


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
