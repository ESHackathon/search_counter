#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from search_counter_service import get_search_count

from flask import Flask
app = Flask(__name__)

@app.route("/search-count", methods=['GET'])
def search_count():
    return json.dumps(get_search_count("colon AND cancer"))


app.run()