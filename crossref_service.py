#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crossref.restful import Types


def search_count(query):
	return Types().works('journal-article').query(query).count()