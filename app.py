import sys
from API import routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}", level="DEBUG")


app = FastAPI()
logger.info('--FastAPI loaded-- {}'.format(app))
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
app.include_router(routes.router)