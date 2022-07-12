from elasticsearch import Elasticsearch


es = Elasticsearch('http://192.168.5.135:9200')

# es = Elasticsearch(f'http://192.168.0.135:9200')


es.info()

def srvHealthCheck():
	health = es.cluster.health()
	print(health)


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
print("start ..............\n")
# srvHealthCheck()
# createIndex()
