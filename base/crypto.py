import os
import base64
from sre_constants import ANY
from tkinter.tix import Select
from typing import Any
from Cryptodome.Cipher import AES as aes



class Cryptograph:
    
    def __init__(self) -> None:
        key = bytes(os.getenv('KEY'))
        iv = os.getenv('IV')
        # moo = 'CBF'
        self.AES = aes(key, aes.MODE_CFB, iv=iv)
    
    def encyrpt(self) -> Any:
        pass
        
        
    def decyrpt(self, data: ANY) -> Any:
        return self.AES.decrypt(data)