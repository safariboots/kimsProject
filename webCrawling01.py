from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.hidoc.co.kr/healthqna/"
boardUrl = 'https://www.hidoc.co.kr/healthqna/list?page='   # 게시물 리스트
no = 1  # 게시물 번호
# crawlingUrl=boardUrl+str(no)    # 실제가져올 게시물 페이지 url
crawlingUrl=boardUrl+str('C0000547599') 

print(crawlingUrl)
request = requests.get(crawlingUrl, headers={"User-Agent": "Mozilla/5.0"}) # 게시물페이지 가져오기
print(request)


###  크롤링을 하지 못하도록 접근 차단을 했기 때문인지 확인 ###
# url = 'https://www.hidoc.co.kr/healthqna/list?page=1'
# req = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) # headers 부분추가
# print(req.content.decode('utf-8'))

###  requests를 호출 할때 User-Agent 를 지정해서 크롬 브라우저에서의 요청인것으로 인식하게 만들어 오류를 해결 ###
# url = 'https://www.hidoc.co.kr/healthqna/list?page=1'
# req = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) # headers 부분추가
# print(req.content.decode('utf-8'))

# 문제의 페이지 https://www.hidoc.co.kr/healthqna/view/C0000547631 

soup = BeautifulSoup(request.content, features="html.parser")   # html 파싱
request.close()

find_str = soup.find('div', attrs={'container_inner clear_g'})    # 가져올 div 전체 내용 부분 탐색
print(find_str)
# file = open("./saveJsonTest.json", "w", encoding='UTF-8')   # json 생성

mnet_dict = {}
page = 0

for info in find_str.find_all('div', attrs={'class':'box_type1 qna_main'}): # div 부분 핵심 내용 탐색
    temp_dict = {}
    
    try:
        title = info.find("strong").text    # 제목가져오기
        nUrl = url + str(info.find("div", attrs={'class':'cont'}).a['href']).strip()    # 공백문자처리후 url가져오기
        contents = info.find('p', attrs={'class': 'desc'}).text     # 내용가져오기
        print(title + ' ok')
        print(nUrl + ' ok')
        print(contents + ' end' + '\n')
        temp_dict[str(page)] = {'title': title, 'nUrl': nUrl, 'contents': contents} # json형태로 저장하기
        mnet_dict = dict(mnet_dict, **temp_dict)
    
    except:
        print(nUrl,'페이지 에러\n')
    

    page += 1
    
    print(temp_dict)
file.write(json.dumps(mnet_dict,ensure_ascii=False,indent='\t'))    # json파일 만들기
file.close()    # 파일 닫기

print('예외처리 정상 동작중..')