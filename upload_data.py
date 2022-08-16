
from elasticsearch import Elasticsearch
import json
import os.path

#connect to the server
elastic_client= Elasticsearch('http://localhost:9200')

filename = 'Search_query.json'

with open(filename, "r") as f:
    data = json.load(f)

for i, doc in enumerate(data):
    elastic_client.index(index=doc["_index"], id = i, document= doc["_source"], ignore = 400)
