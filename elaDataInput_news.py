from elasticsearch import Elasticsearch
import json
from datetime import datetime

# es = Elasticsearch("http://192.168.5.135:9200")
es = Elasticsearch('http://211.188.65.224:9200')
# print(es)

n=258050                # 엘라스틱 서치에서 입력 총 갯 수 확인 후 설정 현재는  '258050' 이므로 이 갯수에서 시작
fileName='./hidocNews'  # 파일명
fileEx='.json'          # 확장자

for fileNo in range(0,28):     # 파일 갯수 +1     # 증가하는 파일명
# for fileNo in range(0,1):     # 테스트
    fullName = fileName + str(fileNo) + fileEx    
    print(fullName)

    file = open(fullName,'r',encoding='UTF-8')
    data = json.load(file,strict=False)	# 정상


    # for i in range(0, 1000):     # 파일내 컨텐츠 갯수 0 ~ 999까지
    for i in range(0, 10):    # 테스트  컨텐츠 10개만 출력
        
        try:            
            # time_result = datetime.strptime(data[str(i)]["date"], "%Y.%m.%d").strftime('%Y-%m-%d')  # 날짜 형식 변경
            # time_result =data[str(i)]["date"].strftime('%Y-%m-%d')
            # print('time_result: ', time_result)
            
            time_result = datetime.strptime(data[str(i)]["date"], '%Y-%m-%d %H:%M').date()      # Time제거 date 형식 변환
            print('time_result: ', time_result)
            
            
            # 실제 전송될 데이터 셋
            doc = {
                "title" : data[str(i)]["title"],
                "Url" : data[str(i)]["Url"],
                "date" : time_result,
                "question" : data[str(i)]["title"],
                "answer" : data[str(i)]["answer"]
                }
            print("doc:", doc)      # 확인 데이터 출력
            res = es.index(index="medihook", doc_type="_doc", id=n+1, body=doc)       # 데이터 전송 id값을 1부터 시작하도록
            print(res)    # 확인 (전송데이터)
            n=n+1       # id 값 증가
            
        except:
            print(i,"번째 번호가 없습니다.\n")          # 컨텐츠가 없을 경우 skip
            
    
        # print(data[str(i)]["title"])
        # print(data[str(i)]["question"])
        # print(data[str(i)]["answer"])
        # print(data[str(i)]["date"])
        # print(i,"번째...\n")
        
    print("ID할당은 : _" ,n,"번째 입니다.")           # 몇 번째 도큐먼트 ID가 생성중인지 확인
    
    



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
