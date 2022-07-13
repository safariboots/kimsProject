from elasticsearch import Elasticsearch
import json
from datetime import datetime

# es = Elasticsearch("http://192.168.5.135:9200")
es = Elasticsearch('http://211.188.65.224:9200')
# print(es)

n=0
fileName='./qnahidoc'
fileEx='.json'
################################
# 0~258050까지
################################
for fileNo in range(0,369):
# for fileNo in range(0,2):
    fullName = fileName + str(fileNo) + fileEx
    
    print(fullName)

    file = open(fullName,'r',encoding='UTF-8')
    data = json.load(file,strict=False)	# 정상


    for i in range(0, 700):
    # for i in range(0, 10):
        try:            
            time_result = datetime.strptime(data[str(i)]["date"], "%Y.%m.%d").strftime('%Y-%m-%d')

            doc = {
                "title" : data[str(i)]["title"],
                "Url" : data[str(i)]["Url"],
                "date" : time_result,
                "question" : data[str(i)]["question"],
                "answer" : data[str(i)]["answer"]
                }
            print("doc:", doc)
            res = es.index(index="medihook", doc_type="_doc", id=n+1, body=doc)
            print(res)
            n=n+1
            
        except:
            print(i,"번째 번호가 없습니다.\n")
            
    
        # print(data[str(i)]["title"])
        # print(data[str(i)]["question"])
        # print(data[str(i)]["answer"])
        # print(data[str(i)]["date"])
        # print(i,"번째...\n")
        
    print("ID할당은 : _" ,n-1,"번째 입니다.")
    
    



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
