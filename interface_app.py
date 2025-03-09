## Solace Interface Prototype

# This is the first structure of the app that will provide a direct interface
# for communication with Solace Intelligence.

import fastapi
from flask import input, output

server = fastapi.FastApi()

@server.route("/", methods=["GET"])
def home():
    "return {"Message": "Welcome to Solace Higher Interface"}"

@server.route("/query", methods=["POST"])
def query():
    data = input()
    return {"SolaceResponse": f\"Highly adapted response: {data}\"}"

server.run()