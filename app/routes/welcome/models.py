import bleach
from pydantic import BaseModel, field_validator


class WelcomeForm(BaseModel):
    name: str
    action: str

    @field_validator("name", "action", mode="before")
    @classmethod
    def sanitize(cls, v: str) -> str:
        return bleach.clean(v.strip(), tags=[], attributes={}, strip=True)
