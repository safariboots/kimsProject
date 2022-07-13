#파이썬으로 MongoDB에 데이터 저장하기

from pymongo import MongoClient   #mongodb 모듈 지정
from datetime import datetime
import pprint
import json

from bson.objectid import ObjectId  #objectid 모듈 지정

#mongodb 연결객체 생성
client = MongoClient('mongodb://211.188.65.224:27017/')


# print(client.list_database_names())         # 모든 db 출력하기

db = client['jjokjam']
colletion = client['medihook']




# ##################### 단일 도큐먼트 입력 테스트 #################
# doc = {
#     "_id": 258052,
#     "title" : "공부합시다",
#     "Url" : "이건 url",
#     "date" : "2022-06-06",
#     "question" : "질문 있어요",
#     "answer" : "답변입니다........"
#     }
# print(doc)

# posts = db.medihook            
# post_id = posts.insert_one(doc).inserted_id
# print('현재 id값은 : ', post_id)
# print(db.list_collection_names(), '\n')


# # 컬렉션 내 도큐먼트 수 조회
# print('컬렉션 내 도큐먼수 : ', posts.count_documents({}),'개')
# ########### 데이터베이스 접속 해제 ###############
# client.close()
# #####################################################################








######################### Json File Data Input #################
#################### n초기값 수정 -> id 258051 ~ id 285235 까지 ######################
n=258050
fileName='./hidocNews'  # 파일명
fileEx='.json'          # 확장자

for fileNo in range(0,28):
# for fileNo in range(0,1):
    fullName = fileName + str(fileNo) + fileEx
    
    # print(fullName+'\n')

    file = open(fullName,'r',encoding='UTF-8')
    data = json.load(file,strict=False)	# 정상
    
    # print(data)

    for i in range(0, 1000):
    # for i in range(0, 2):
        
        try:            
            # time_result = datetime.strptime(data[str(i)]["date"], "%Y.%m.%d").strftime('%Y-%m-%d')            
            time_result = datetime.strptime(data[str(i)]["date"], '%Y-%m-%d %H:%M').date()      # Time제거 date 형식 변환
            # print(time_result, '...........................')

            doc = {
                "_id": n+1,
                "title" : data[str(i)]["title"],
                "Url" : data[str(i)]["Url"],
                "date" : str(time_result),
                "question" : data[str(i)]["title"],
                "answer" : data[str(i)]["answer"]
                }
            print(doc.get('date'))
            # doc = {
            #     "_id": 258051,
            #     "title" : "제목입니다.",
            #     "Url" : "url 입니다",
            #     "date" : "2021-01-01",
            #     "question" : "질문입니다.",
            #     "answer" : "답변입니다"
            #     }
            
            # for key, value in doc.items():
            #     print('key:', key, 'value: ', value)
           
    
            ########## 콜렉션에 도큐먼트 생성 ###############
            posts = db.medihook
            print(posts)
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
        

print("최종 ID할당은 : " ,n,"번째 입니다.")
    
# Collection 리스트 조회
print(db.list_collection_names(), '\n')
# 컬렉션 내 도큐먼트 수 조회
print('컬렉션 내 도큐먼수 : ', posts.count_documents({}),'개')
########### 데이터베이스 접속 해제 ###############
client.close()


