
from pubmed import search_count

def get_search_count(query):
	return {"pubmed": search_count(query)}