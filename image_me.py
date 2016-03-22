import os
import sys
from google_search import GoogleCustomSearch

if len(sys.argv) < 2:
  print 'You must search query'
  sys.exit()

SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']                           
API_KEY = os.environ['GOOGLE_CLOUD_API_KEY']

api = GoogleCustomSearch(SEARCH_ENGINE_ID, API_KEY)

results = api.search(sys.argv[1])
first = results.next()
if first:
  print first['link']
