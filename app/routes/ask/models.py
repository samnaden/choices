import bleach
from pydantic import BaseModel, field_validator


class AskForm(BaseModel):
    name: str
    question: str
    options: list[str]

    @field_validator("name", "question", mode="before")
    @classmethod
    def sanitize(cls, v: str) -> str:
        return bleach.clean(v.strip(), tags=[], attributes={}, strip=True)

    @field_validator("options", mode="before")
    @classmethod
    def sanitize_options(cls, v: list) -> list:
        return [bleach.clean(e.strip(), tags=[], attributes={}, strip=True) for e in v]
