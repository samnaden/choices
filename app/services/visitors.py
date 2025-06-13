import uuid
from datetime import datetime, timezone

from app.db.client import SessionLocal
from app.db.models import Visitor


def insert_visitor(visitor_name: str) -> uuid.UUID:
    now = datetime.now(tz=timezone.utc)

    surrogate_id = uuid.uuid4()

    with SessionLocal() as session:
        visitor = Visitor(
            id=surrogate_id,
            created_at=now,
            name=visitor_name,
        )

        session.add(visitor)
        session.commit()

    return surrogate_id
