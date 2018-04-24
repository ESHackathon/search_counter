
from pubmed_service import search_count as pubmed_search_count
from crossref_service import search_count as crossref_search_count
from doaj_service import search_count as doaj_search_count

def get_search_count(query):
	return {
		"pubmed": pubmed_search_count(query),
		"crossref": crossref_search_count(query),
		"doaj": doaj_search_count(query) 
	}