from elasticsearch import Elasticsearch
import json

es = Elasticsearch("http://192.168.5.133:9200")


n=0
file = open('ex1.json','r',encoding='utf-8')
for line in file.readlines():
	dic = json.loads(line)
	doc = {
		"public_date":dic["public_date"],
		"newspaper":dic["newspaper"],
		"title":dic["title"],
		"content":dic["content"]
		}
	
	#print(doc)

	res = es.index(index="kogundata", doc_type="_doc", id=n+1, body=doc)
	n=n+1
	#print(n)
	#print(res)
	#print(dic)
	#print(dic["title"])
print("data count: _" ,n)
