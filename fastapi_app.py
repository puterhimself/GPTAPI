from fastapi import FastAPI

import os
import openai

app = FastAPI()

from fastapi import APIRouter, FastAPI, Path, WebSocket
from pydantic import BaseModel
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware
from database import db as Collections
from datetime import datetime
from settings import API_KEY


# openai.organization = os.getenv('organisation')# "org-VgYqHHC2seYeXwoHsU05U3yT"
openai.api_key = API_KEY #

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
async def home(args: Item):
    prompt = args.prompt
    config = args.config
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        **dict(config)
    )

    _obj = await Collections.Prompts.insert_one(
        {
            "prompt": prompt,
            "config": config,
            "response": res,
            "date_created": datetime.now()
        }

    )
    return res
  

app.include_router(router)
