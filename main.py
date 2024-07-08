from flask import Flask
import os
import random

app = Flask(__name__)

@app.route("/hi")
def hi():
    return "Hi"

@app.route("/bye")
def bye():
    return "Bye"

app.run(host="0.0.0.0")