import json
import os
from base64 import b64decode, b64encode
from dotenv import load_dotenv
from typing import Any
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

load_dotenv()


class Cryptograph:
    def __init__(self, new) -> None: pass

    def _keyGen(self, _size=16) -> bytes:
        return get_random_bytes(_size)

    def _writeBytes(self, key=None, iv=None, new=False):
        if new:
            key = self._keyGen()
            iv = AES.new(key, AES.MODE_CFB).iv

        jsonKeys = {
            "bytes": {"key": key, "IV": iv},
            "encode": {
                "key": b64encode(key).decode("utf-8"),
                "IV": b64encode(iv).decode("utf-8"),
            },
        }

        for k, v in jsonKeys["bytes"].items():
            with open("./keys/" + k, "wb") as F:
                F.write(v)

        with open("./keys/encodedKeys.json", "w") as F:
            json.dump(jsonKeys["encode"], F)

        return jsonKeys

    def _safeGenerate(self, new=False):
        if new: 
            result = self._writeBytes(new=True)
            key = result["bytes"]["key"]
            cipher = AES.new(key, AES.MODE_CFB)
            
        else:
            key = b64decode(os.getenv("KEY"))
            iv = b64decode(os.getenv("IV"))
            cipher = AES.new(key, AES.MODE_CFB, iv=iv)

        return key, cipher

    def encyrpt(self, text: Any) -> Any:
        key, cipher = self._safeGenerate(new=False)
        if type(text) == str:
            text = bytes(text, "utf-8")
        if type(text) == dict:
            text = bytes(json.dumps(text), "utf-8")
            
        return b64encode(cipher.encrypt(text)).decode('utf-8')

    def decyrpt(self, text: Any, jsonify=False) -> Any:
        key, cipher = self._safeGenerate(new=False)
        text = b64decode(text)
        text = cipher.decrypt(text).decode("utf-8")
        
        if jsonify: return json.loads(text) 
        return text


if __name__ == "__main__":
    c = Cryptograph(new=False)
#     print(c.encyrpt(text:={
#     "prompt": "You: How do I become consistent and give up laziness?Krishna is a chatbot that answers questions like the god he is using his Dharmic principles",
#     "config": {"temperature": 1, "max_tokens": 500}
# }
#                     ))
    print(ct := c.decyrpt('s1JYLB6ZCfSARn7Hu/eUU5Ctjyhmz4V3CaDnzLW9XlcdEtefvuBCdR7YtbdSV+tjdwV/pYwsloLKQ+/PX+nlIVDa+fxpEKVsbMJLUVa6YBE6l1PL9dKd9Eub2zhzDir8vRU/gaIq9p4japvOkE1fmMUArF67jbo4BnByuIlLT+KfeRc4sE46NV6tJKGDDs4Y/3MFCtGE8FmR/C235bUMj69QuzRAwb3OPnn78NpQwRF4+V1V/u795kX5XEwcFrCUG/dWmNEZBNNsVPKgU2xDxAIVR43KeOsDOCW1n1bHnX4rJFXUrGd7ATbIqHbp+fbSd5lDJ2eFxNrI5V7uAOjai3popUC260Voqg7qZTK4UhVc8Gm3Yb1MUM84dRNgqvPYeqoGv9ZQjxA1OzhOO9JuKXKJB3bZQCj2lUvMoeaeE6fbz4ZqkwqAWSlUM6hAtlHmA0mOXXkv3qXti8l9xK8GFeP0c30b5MG5FwbAdsiVAn07M8BbDUDb4jBR+bQwxDWEA7fSxbJDX8Qv+KKE7NAZme3lvBOAIVsh7EE5etzhBMI70SLleHB2vtOlM7t1AQdspCToa9wnNBJ7ui7gZz3TdAXyKCfngnaRqFxEZHOMqE0OmmQ7pwh10bU8GhExKBF1gI+uPCF/hlJyMwXgeZFtVuIsT1h/m5+M3QJ1JBlv8sB3fut39c/w2sbAfJix5o6nxrn6vWdhg8JHhnjfqXpcaVHon4tIYwkDMfctbYm0BiEzTe8bI3grK42DQrNzINBBq4RerCEjfL4='
, jsonify=False))