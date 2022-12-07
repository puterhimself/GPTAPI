
import settings
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_DB_URL)
database = getattr(client, settings.DB_NAME)

Prompts = database.get_collection("prompts")





