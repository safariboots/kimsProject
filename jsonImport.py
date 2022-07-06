from elasticsearch import Elasticsearch
import pprint as ppr
import json

es = Elasticsearch("http://192.168.5.133:9200")   # 객체 생성
def srvHealthCheck():
        health = es.cluster.health()
        print (health)

def allIndex():
        # Elasticsearch에 있는 모든 Index 조회
        print (es.cat.indices())

def createIndex_sample():
	# 인덱스 생성
	es.indices.create(
		index = "today20220412",
		body = {
			"settings":{
				"number_of_shards":3
				},
			"mappings":{
				"properties":{
					"cont": {"type":"text"},
					"mnagnnm":{"type":"text"},            
					"post":{"type":"text"},
					"rgdt":{"type":"text"},
					"rgter":{"type":"text"},
					"tel":{"type":"text"},
					"title":{"type":"text"}
					}		
				}
		}
)

def createIndex():
	es.indices.create(
		index = "kogundata",
		body = {
			"settings":{
				"number_of_shards":3
				},
			"mappings":{
				"properties":{
					"public_date":{
						"type": "date"
						#"format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
						},
					"newspaper":{"type": "keyword"},
					"title":{
						"type": "text",
						"fields": {
							"keyword" : {
								"type":"keyword",
								"ignore_above": 256
								}
							}
						},
					"content":{"type":"text"}							
					}
				}
			}
		)


def dataInsert():
	#===================
	#대용량 Json 파일 데이터 삽입
	#===================
	
	with open("/home/kobic/tmp/ex.json","r",encoding="utf-8") as fjson:
		data = json.loads(fjson.read())
		#print(data)
		for n, i in enumerate(data):
			doc = {
				"public_date":i["public_date"],
				"newspaper":i["newspaper"],
				"title":i["title"],
				"content":i["content"]
				}
			
			print(doc)
			res = es.index(index="kogundata", doc_type="_doc", id=n+1, body=doc)
			print ("::::::::::::::::: doc :::::::::::::::::\n")
			print (res)
			print ("::::::::::::::::: res :::::::::::::::::\n")

def dataInsert_sample():
        # ===============
        # (샘플)데이터 삽입
        # ===============
        with open("../json_doc_make/tst.json", "r", encoding="utf-8") as fjson:
            data = json.loads(fjson.read())
            for n, i in enumerate(data):
                doc = {"cont"   :i['cont'],
                       "mnagnnm":i["mnagnnm"],
                       "post"   :i["post"],
                       "rgdt"   :i["rgdt"],
                       "rgter"  :i["rgter"],
                       "tel"    :i["tel"],
                       "title"  :i["title"]}
                #print("hello")
                res = es.index(index="today19020301", doc_type="today", id=n+1, body=doc)
                print (res)

#srvHealthCheck()
#createIndex()
#allIndex()
dataInsert()
