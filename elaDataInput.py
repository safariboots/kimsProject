from elasticsearch import Elasticsearch
import json
from datetime import datetime

es = Elasticsearch("http://192.168.5.133:9200")
# es = Elasticsearch('http://211.188.65.224:9200/')
print(es)


file = open('./qnahidoc0.json','r',encoding='UTF-8')
data = json.load(file,strict=False)	# 정상


n=0
for i in range(0, 30):
    print(data[str(i)]["title"])
    print(data[str(i)]["question"])
    print(data[str(i)]["answer"])
    print(data[str(i)]["date"])
    print(i,"번째...\n")
    
    
    


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

print("data count: _" ,n)



# file = open('./qnahidoc0.json','r',encoding='UTF-8')
# data = json.load(file,strict=False)	# 정상
# print(data["0"]["title"])
# print(data["1"]["question"])
# print(data["2"]["answer"])
# print(data["3"]["date"])
# print(len(data))
# i = 0
# for n in data:
#     print(i)
#     try:
#         if i > 10:

#             break
#         else:
#             j=str(i)
#             print(n[j].title)
#     except:
#         print(i, "가 존재하지 않습니다.\n")
#     i += 1
