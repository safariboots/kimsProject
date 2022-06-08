from elasticsearch import Elasticsearch


es = Elasticsearch("http://192.168.5.133:9200")

def srvHealthCheck():
	health = es.cluster.health()
	print(health)


def createIndex():
	#인덱스 생성
	es.indices.create(
	 	index = "kogundata",
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
				}
			}
	)

srvHealthCheck()
createIndex()
