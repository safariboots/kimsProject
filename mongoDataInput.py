#파이썬으로 MongoDB에 데이터 저장하기

from pymongo import MongoClient   #mongodb 모듈 지정
import datetime
import pprint

from bson.objectid import ObjectId  #objectid 모듈 지정

#mongodb 연결객체 생성
# client = MongoClient()
# client = MongoClient('192.168.19.132', '27017')  #접속IP, 포트
# client = MongoClient('mongodb://192.168.19.132:9563/') 
# 쪽잠 클라우드 http://211.188.65.224:19999/

client = MongoClient('http://211.188.65.224:19999/')
#데이터베이스 개체 가져오기
# db = client['------']
db = client


#컬렉션 확인하기
print(db.collection_names())


#컬렉션 개체 가져오기
# foods = db['restaurants']
foods = db.restaurants


#restaurants 전체 데이터 조회
for food in foods.find():
    # print(food)
    # pprint.pprint(food)   #json을 보기 좋게 들여쓰기 적용후 출력
    pass

#zipcode가 10302 인 음식점 조회

for food in foods.find({'address.zipcode':'10302'}):
    # print(food)
    pass


#새로운 컬렉션 생성
posts = db.posts

#JSON 문서 생성
#MongoDB 안에 데이터는 JSON 형식으로 저장
#pymongo 모듈에서는 파이썬의 딕셔너리 자료구조를 활용해서 표현
#post는 "이름, 소개글, 태그, 작성일" 로 구성
post = { 'author':'------',
        'text':'Hello, World!!',
        'tags':['python','bigdata','pycharm'],
        'date':datetime.datetime.utcnow() }

#데이터 추가하기
# posts.insert_one(post)    #단순 데이터 추가
# post_id = posts.insert_one(post).inserted_id
# 데이터 추가시 생성된 ObjectId를 변수에 저장
# print(post_id)

#posts 전체 데이터 조회
for post in posts.find():
    print(post)


#posts 특정 데이터 조회
for post in posts.find({'author':'------'}):
    print(post)


#데이터 수정하기
result = posts.update_one(
    {'author':'------'},   #수정할 데이터 찾을 조건
    {
        '$set':{'text':'Hello, Python3!!',
                'date':'datetime.datetime(2018,6,20, 11,20,30)'},
                #수정값
    })
print(result.matched_count)  #수정할 데이터 찾은 건수
print(result.modified_count)  #수정된 데이터 건수


#데이터 삭제하기
# result = posts.delete_one()      #조건과 일치하는 데이터중 하나만 삭제
# result = posts.delete_many()     #조건과 일치하는 데이터 모두 삭제
# result = posts.delete_many({})   #모두 삭제 (조건지정x)

result = posts.delete_many({'author':'-----'})
print(result.deleted_count)    #삭제된 데이터 건수

#접속 해제
client.close()