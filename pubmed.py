#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
# import urllib.parse

import requests

def search_count(query):
    # encoded_query = urllib.parse.quote_plus(query)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=0&term=%s" % query
    response = requests.get(url)
    print response.content
    return json.loads(response.content)['esearchresult']['count']

def main():
    term = "Forest*"
    total_count = search_count(term)
    print("%s: %s" % (term, total_count))

if __name__ == '__main__':
    main()
