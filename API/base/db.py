import os
from typing import Any
from motor import motor_asyncio


class Cache:
    def __init__(self, conf: dict) -> None:
        self.conf = conf

        self.client: motor_asyncio = motor_asyncio.AsyncIOMotorClient(
            os.getenv("MONGO_URL")
        )
        self.database = getattr(self.client, conf.get("database", "KrishnAI"))
        # self.Prompts= self.database.get_collection(conf.get('collection', 'chats'))
        self.loop = self.client.get_io_loop()

    async def _insertOne(self, document: dict, collection: str = None, DB=None) -> Any:
        DB = DB if DB else self.database
        collection = DB.get_collection(collection)
        _object = await collection.insert_one(document)
        return _object

    async def _findOne(self, document: dict, collection: str, DB=None) -> Any:
        DB = DB if DB else self.database
        collection = DB.get_collection(collection)
        _object = await collection.find_one(document)
        return _object

    def cachePrompt(self, prompt, response, params):
        document: dict = {
            "prompt": prompt,
            "response": response,
            "params": params,
        }
        self.loop.run_until_complete(self._insertOne(document, "chats"))

    def retrieveCache(self, prompt: dict):
        response = self.loop.run_until_complete(self._findOne(prompt, "chats"))
        return response


if __name__ == "__main__":
    c = Cache()
    print(c.retrieveCache({}))
