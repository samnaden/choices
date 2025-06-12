from typing import Dict

import bleach
from pydantic import BaseModel, field_validator


class AnswerForm(BaseModel):
    name: str
    answers: Dict[str, str]  # question_id -> answer_id

    @field_validator("name", mode="before")
    @classmethod
    def sanitize_name(cls, v: str) -> str:
        return bleach.clean(v.strip(), tags=[], attributes={}, strip=True)

    @field_validator("answers", mode="before")
    @classmethod
    def sanitize_answers(cls, v: dict) -> dict:
        return {
            bleach.clean(k.strip(), tags=[], attributes={}, strip=True): bleach.clean(
                val.strip(), tags=[], attributes={}, strip=True
            )
            for k, val in v.items()
        }
