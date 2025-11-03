import sys
from flask import Flask, jsonify, make_response

from utils.cpu import count_x
from utils.io import crawl, links
app = Flask(__name__)

@app.route("/cpu")
def cpu():
    count_x()
    return jsonify(message="Hello, world!")

@app.route("/io")
def io():
    for link in links:
        crawl(link)
    response = make_response(b"Hello, finished crawling")
    response.content_type = "text/plain"
    return response