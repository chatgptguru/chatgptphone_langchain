import os
from flask import Flask, request, jsonify
from flask import Flask
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/getAnswer', methods=["post"])
def getAnswer():
    try:
        print(request.form["question"])
        llm = OpenAI(temperature=0.9)
        result = llm(request.form["question"])
        return jsonify({'message': result}), 200
    except Exception as err:
        print(err)
        return jsonify({'message': 'Langchain Error'}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0')
