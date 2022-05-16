from pydantic.main import BaseModel


class Blog(BaseModel):
    title: str
    body: str
