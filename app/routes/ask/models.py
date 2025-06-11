import bleach
from pydantic import BaseModel, field_validator


class AskForm(BaseModel):
    name: str
    question: str

    @field_validator("name", "question", mode="before")
    @classmethod
    def sanitize(cls, v: str) -> str:
        return bleach.clean(v.strip(), tags=[], attributes={}, strip=True)
