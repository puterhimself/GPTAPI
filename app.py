# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os
import openai
  
# creating a Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

openai.organization = os.getenv('organisation')# "org-VgYqHHC2seYeXwoHsU05U3yT"
openai.api_key = os.getenv('api') #
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['POST'])
@cross_origin()
def home():
    request_data = request.json
    prompt = request_data.get('prompt')
    config = request_data.get('config')
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        **dict(config)
    )
    return(res)
  


@app.route("/", methods=['GET'])
def test():
    return({"message": "working"})

  
