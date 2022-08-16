
from elasticsearch import Elasticsearch
import json



#connect to the server
elastic_client= Elasticsearch('http://localhost:9200')


#check if the file exists, if it does not, create new file
filename = 'Search_query.json'

query_body = {
  "query": {
    "match_all": {}
  }
}

total_documents = 100

result = elastic_client.search(index="tweets", body=query_body, size= total_documents)

all_hits = result['hits']['hits']

with open(filename, 'w') as f:
      json.dump(all_hits, f, indent= 4)
      
