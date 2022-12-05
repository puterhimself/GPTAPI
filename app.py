import os
import openai

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# openai.organization = os.getenv('organisation')# "org-VgYqHHC2seYeXwoHsU05U3yT"
openai.api_key = os.getenv('api') #

class Item(BaseModel):
    prompt: str
    config: Dict = {}

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

router = APIRouter(prefix="")

@router.post("/")
def home(args: Item):
    prompt = args.prompt
    config = args.config
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        **dict(config)
    )
    return res
  

app.include_router(router)
