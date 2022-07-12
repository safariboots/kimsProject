from elasticsearch import Elasticsearch
import json

es = Elasticsearch("http://192.168.5.135:9200")


file = open('./qnahidoc0.json','r',encoding='UTF-8')
data = json.load(file,strict=False)	# 정상
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
for i in range(0, 30):
    print(data[str(i)]["title"])
    print(data[str(i)]["question"])
    print(data[str(i)]["answer"])
    print(data[str(i)]["date"])
    print(i,"번째...\n")