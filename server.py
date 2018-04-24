#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Flask

from search_counter_service import get_search_count

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/search-count", methods=['GET'])
def search_count():
    return json.dumps(get_search_count("colon AND cancer"))



if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", threaded=True)