from pydantic import BaseModel


class quote(BaseModel):
    character_name: str
    quote_content: str

    class Config:
        orm_mode: True
