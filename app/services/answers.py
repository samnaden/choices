from app.db.client import SessionLocal
from app.db.models import Answer


def update_answer_votes(answer_ids: list[str]) -> None:
    """
    Increment the vote count for each answer ID in the provided list.

    Each update is performed in a separate SQL statement within a single transaction.
    This approach leverages the database's atomicity guarantees to avoid race conditions
    when multiple users vote concurrently.

    Args:
        answer_ids (list[str]): A list of answer UUIDs (as strings) to increment votes for.
    """

    if not answer_ids:
        return

    with SessionLocal() as session:
        for answer_id in answer_ids:
            session.query(Answer).filter(Answer.id == answer_id).update(
                {Answer.votes: Answer.votes + 1}
            )
        session.commit()
