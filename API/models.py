from urllib import request
from pydantic import BaseModel
# from typing import Dict


class Item(BaseModel):
    request: str
    # config: Dict = {"max_tokens": 250}
