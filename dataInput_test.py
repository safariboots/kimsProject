from elasticsearch import Elasticsearch
import json
from datetime import datetime
import time



es = Elasticsearch("http://192.168.5.135:9200")
# es = Elasticsearch('http://211.188.65.224:9200/')
# print(es)

n=0
fileName='./qnahidoc'
fileEx='.json'

# for fileNo in range(0,369):
for fileNo in range(0,2):
    fullName = fileName + str(fileNo) + fileEx
    
    print(fullName)

    file = open(fullName,'r',encoding='UTF-8')
    data = json.load(file,strict=False)	# 정상


    # for i in range(0, 699):
    for i in range(0, 10):
        
        time_result = datetime.strptime(data[str(i)]["date"], "%Y.%m.%d").strftime('%Y-%m-%d')

        doc = {
            "title" : data[str(i)]["title"],
            "Url" : data[str(i)]["Url"],
            "date" : time_result,
            "question" : data[str(i)]["question"],
            "answer" : data[str(i)]["answer"]
            }
        print("doc:", doc)
        res = es.index(index="medihook_test1", doc_type="_doc", id=n+1, body=doc)
        print(res)
        n=n+1
        

    print("data count: _" ,n)
    
    
