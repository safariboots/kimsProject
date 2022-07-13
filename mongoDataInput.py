#파이썬으로 MongoDB에 데이터 저장하기

from pymongo import MongoClient   #mongodb 모듈 지정
from datetime import datetime
import pprint
import json

from bson.objectid import ObjectId  #objectid 모듈 지정

#mongodb 연결객체 생성
# client = MongoClient()
# client = MongoClient('192.168.19.132', '27017')  #접속IP, 포트
# client = MongoClient('mongodb://192.168.19.132:9563/') 
# 쪽잠 클라우드 mongdb://211.188.65.224:27017/

client = MongoClient('mongodb://211.188.65.224:27017/')
#데이터베이스 개체 가져오기
# mydb = client['db명']
# mydb = client['jjokjam']                # db객체 가져오기
# myCollection = mydb['medihook']        # collection 객체 가져오기

# print(client.list_database_names())         # 모든 db 출력하기

db = client['jjokjam']
colletion = client['medihook']


######################### Json File Data Input #################
n=0
fileName='./qnahidoc'
fileEx='.json'

for fileNo in range(0,369):
# for fileNo in range(0,1):
    fullName = fileName + str(fileNo) + fileEx
    
    # print(fullName+'\n')

    file = open(fullName,'r',encoding='UTF-8')
    data = json.load(file,strict=False)	# 정상
    
    # print(data)

    for i in range(0, 700):
    # for i in range(0, 2):
        
        try:            
            time_result = datetime.strptime(data[str(i)]["date"], "%Y.%m.%d").strftime('%Y-%m-%d')
            
            # time_result = datetime.strptime(data[str(i)]["date"], '%Y.%m.%d').date()
            
            doc = {
                "_id": n+1,
                "title" : data[str(i)]["title"],
                "Url" : data[str(i)]["Url"],
                "date" : time_result,
                "question" : data[str(i)]["question"],
                "answer" : data[str(i)]["answer"]
                }
            # print("doc:", doc)
            # res = es.index(index="medihook", doc_type="_doc", id=n+1, body=doc)
            # print(res)
            
            ########### 콜렉션에 도큐먼트 생성 ###############
            posts = db.medihook
            post_id = posts.insert_one(doc).inserted_id
            print('현재 id값은 : ', post_id)
            
            n=n+1
            
        except:
            print(i,"번째 번호가 없습니다.\n")
            
    
        # print(data[str(i)]["title"])
        # print(data[str(i)]["question"])
        # print(data[str(i)]["answer"])
        # print(data[str(i)]["date"])
        # print(i,"번째...\n")
        
    print("ID할당은 : " ,n,"번째 입니다.")
    
    
# Collection 리스트 조회
print(db.list_collection_names(), '\n')
# 컬렉션 내 도큐먼트 수 조회
print('컬렉션 내 도큐먼수 : ', posts.count_documents({}),'개')
########### 데이터베이스 접속 해제 ###############
client.close()


#####################################################################################

# 단일 도큐먼트 조회
# pprint.pprint(posts.find_one())             # 상위 1개 도큐먼트 출력
# pprint.pprint(posts.find_one({"_id": 2}))   # 지정한 _id 값에 맞는 도큐먼트 출력

# # 다중 도큐먼트 조회
# new_posts = [
#     {
#     "_id": "1"
#     # "author": "Mike",
#     # "text": "Another post!",
#     # "tags": ["bulk", "insert"],
#     # "date": datetime.datetime(2009, 11, 12, 11, 14)
#     },
#     {
#     "_id": "2"
#     # "author": "Mike",
#     # "text": "Another post!",
#     # "tags": ["bulk", "insert"],
#     # "date": datetime.datetime(2009, 11, 12, 11, 14)
#     },
    
# ]

# result = posts.insert_many(new_posts)
# result.inserted_ids

############################################################


#컬렉션 확인하기
# print(mydb.list_collection_names())

# # medihook collection 전체 데이터 조회
# for contents in myCollection.find():
#     print(contents)
#     pprint.pprint(contents)   #json을 보기 좋게 들여쓰기 적용후 출력

## 데이터 로드하기
# for i in range(0, 3): 
#     post = { 
#             'title':data[str(i)]["title"],
#             'Url':data[str(i)]["title"],
#             'date':data[str(i)]["title"],
#             'question':data[str(i)]["title"],
#             'answer':data[str(i)]["title"]
#             }


# ################ 여기 부터 주석처리 #################
# #컬렉션 개체 가져오기
# # foods = db['restaurants']
# foods = db.restaurants


# #restaurants 전체 데이터 조회
# for food in foods.find():
#     # print(food)
#     # pprint.pprint(food)   #json을 보기 좋게 들여쓰기 적용후 출력
#     pass

# #zipcode가 10302 인 음식점 조회

# for food in foods.find({'address.zipcode':'10302'}):
#     # print(food)
#     pass


# #새로운 컬렉션 생성
# posts = db.posts

# #JSON 문서 생성
# #MongoDB 안에 데이터는 JSON 형식으로 저장
# #pymongo 모듈에서는 파이썬의 딕셔너리 자료구조를 활용해서 표현
# #post는 "이름, 소개글, 태그, 작성일" 로 구성
# post = { 'author':'------',
#         'text':'Hello, World!!',
#         'tags':['python','bigdata','pycharm'],
#         'date':datetime.datetime.utcnow() }

# #데이터 추가하기
# # posts.insert_one(post)    #단순 데이터 추가
# # post_id = posts.insert_one(post).inserted_id
# # 데이터 추가시 생성된 ObjectId를 변수에 저장
# # print(post_id)

# #posts 전체 데이터 조회
# for post in posts.find():
#     print(post)


# #posts 특정 데이터 조회
# for post in posts.find({'author':'------'}):
#     print(post)


# #데이터 수정하기
# result = posts.update_one(
#     {'author':'------'},   #수정할 데이터 찾을 조건
#     {
#         '$set':{'text':'Hello, Python3!!',
#                 'date':'datetime.datetime(2018,6,20, 11,20,30)'},
#                 #수정값
#     })
# print(result.matched_count)  #수정할 데이터 찾은 건수
# print(result.modified_count)  #수정된 데이터 건수


# #데이터 삭제하기
# # result = posts.delete_one()      #조건과 일치하는 데이터중 하나만 삭제
# # result = posts.delete_many()     #조건과 일치하는 데이터 모두 삭제
# # result = posts.delete_many({})   #모두 삭제 (조건지정x)

# result = posts.delete_many({'author':'-----'})
# print(result.deleted_count)    #삭제된 데이터 건수

# #접속 해제
# client.close()