import bleach
from pydantic import BaseModel, field_validator


class AnswerForm(BaseModel):
    name: str
    answer: str

    @field_validator("name", "answer", mode="before")
    @classmethod
    def sanitize(cls, v: str) -> str:
        return bleach.clean(v.strip(), tags=[], attributes={}, strip=True)
