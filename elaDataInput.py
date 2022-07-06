# from elasticsearch import Elasticsearch
import json

# es = Elasticsearch("http://192.168.5.133:9200")


file = open('./saveJsonTest.json','r',encoding='UTF-8')
data = json.load(file,strict=False)	# 정상
print(data["0"]["title"])

