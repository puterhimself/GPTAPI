from fastapi import APIRouter
from .models import Item
from .main import App
from loguru import logger

logger.debug('--Router Loaded--')
router = APIRouter()
app = App()
logger.debug('--Router Loaded-- {} {}'.format(app, router))

@router.post('/')
def GPT(query: Item):
    logger.debug('--"/" post GPT-- {}'.format(query))
    return app.GPT(query.request)