#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Flask, request
from flask_cors import CORS

from search_counter_service import get_search_count

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def to_unicode(text):
    if type(text) == unicode:
        return text
    return text.decode("utf-8")


@app.route("/search-count/<query>", methods=['GET'])
def search_count(query):
    return json.dumps(get_search_count(to_unicode(query)))

@app.route("/search-count", methods=['POST'])
def search_count_post():
    query = to_unicode(request.get_data())

    return json.dumps(get_search_count(query))

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", threaded=True)