from bottle import route, run, get, post, request, response
import openai
import os
from dotenv import load_dotenv

load_dotenv()


openai.organization = os.getenv('organisation')# "org-VgYqHHC2seYeXwoHsU05U3yT"
openai.api_key = os.getenv('api') #"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"


@route("/", method='POST')
def GPT3():
    prompt = request.params.prompt
    params = request.POST.config
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        **dict(params)
    )
    return(res)

@route("/", method='GET')
def test():
    return('working')

run(host='localhost', port=3000)