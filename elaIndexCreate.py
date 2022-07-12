from datetime import datetime
from elasticsearch import Elasticsearch
import pprint as ppr
import json

# es = Elasticsearch("http://192.168.5.135:9200/")   # 객체 생성
es = Elasticsearch('http://211.188.65.224:9200/')
print(es)

def srvHealthCheck():
        health = es.cluster.health()
        print (health)


def createIndex():
	#인덱스 생성
	es.indices.create(
	 	index = "_medihook_test1",
		body = {
			"settings": {
				"number_of_shards": 3
				},
			"mappings": {
				"properties": {
					"public_date": {
						"type": "date",
						"format": "yyyyMMdd"
						},
					"newspaper": {"type": "keyword"},
					"title": {
						"type": "text",
						"fields": {
							"keyword" : {
								"type": "keyword",
								"ignore_above": 256
								}
							}
						},
					"content": {"type": "text"}
					}
				},
			"analysis": {
					"tokenizer": {
						"nori_none": {
							"type": "nori_tokenizer",
							"decompound_mode": "none"
						},
						"nori_discard": {
							"type": "nori_tokenizer",
							"decompound_mode": "discard"
						},
						"nori_mixed": {
							"type": "nori_tokenizer",
							"decompound_mode": "mixed"
						}
					},
					"analyzer": {
						"korean": {
							"type": "nori",
							#"stopwords": "_korean_"
						}
					}
				}
			}
	)

srvHealthCheck()
# createIndex()
