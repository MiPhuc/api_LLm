from pydantic import BaseModel
from typing import List

class request_json(BaseModel):
    content: str

class response_json(BaseModel):
    answer: List[str]
