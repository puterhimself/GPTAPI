import requests
from requests.structures import CaseInsensitiveDict

url = "http://34.134.94.162/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = """
{
    "prompt": "You: How do I become consistent and give up laziness?Krishna is a chatbot that answers questions like the god he is using his Dharmic principles",
    "config": {"temperature": 1, "max_tokens": 500}
}
"""


resp = requests.get(url, headers=headers)

print(resp.json())

