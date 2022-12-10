import os
import openai
from dotenv import load_dotenv
from .base.crypto import Cryptograph
from loguru import logger

load_dotenv()
# from .models import Item
# from .base.db import cache

openai.organization = os.getenv("organisation")
openai.api_key = os.getenv("API")
logger.debug("openAI api set: {}".format(len(openai.api_key)))

class App:
    def __init__(self) -> None:
        logger.info("--App Loaded--")
        self.crypto = Cryptograph(new=False)

    def GPT(self, request: str):
        logger.debug("--App.GPT incoming request-- {}".format(request))
        request: dict = self.crypto.decyrpt(request, jsonify=True)
        logger.debug("--App.GPT Request Decrypted-- {}".format(request))
        gptResponse = openai.Completion.create(
            model="text-davinci-003", prompt=request['prompt'], **dict(request['config'])
        )
        logger.debug("--App.GPT OpenAI API response--{}".format(gptResponse))
        return self.crypto.encyrpt(str(gptResponse['choices'][0]['text']).strip())