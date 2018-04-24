#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

def search_count(query):
    query = query.replace('"', '\\"')
    url = """https://doaj.org/query/journal,article/_search?source={"query":{"query_string":{"query":"%s","default_operator":"AND"}},"from":0,"size":10,"facets":{"_type":{"terms":{"field":"_type","size":102,"order":"reverse_term"}},"index.classification.exact":{"terms":{"field":"index.classification.exact","size":110,"order":"count"}},"index.has_seal.exact":{"terms":{"field":"index.has_seal.exact","size":110,"order":"count"}},"index.license.exact":{"terms":{"field":"index.license.exact","size":110,"order":"count"}},"index.publisher.exact":{"terms":{"field":"index.publisher.exact","size":110,"order":"count"}},"index.language.exact":{"terms":{"field":"index.language.exact","size":110,"order":"count"}}}}""" % query
    response = requests.get(url)
    return int(json.loads(response.content).get('hits', {}).get('total'))
