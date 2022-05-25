from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.hidoc.co.kr/healthqna/"
boardUrl = 'https://www.hidoc.co.kr/healthqna/list?page='   # 게시물 리스트
no = 1  # 게시물 번호
crawlingUrl=boardUrl+str(no)    # 실제가져올 게시물 페이지 url

# print(crawlingUrl)
request = requests.get(crawlingUrl, headers={"User-Agent": "Mozilla/5.0"}) # 게시물페이지 가져오기
#print(request)


###  크롤링을 하지 못하도록 접근 차단을 했기 때문인지 확인 ###
# url = 'https://www.hidoc.co.kr/healthqna/list?page=1'
# req = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) # headers 부분추가
# print(req.content.decode('utf-8'))

###  requests를 호출 할때 User-Agent 를 지정해서 크롬 브라우저에서의 요청인것으로 인식하게 만들어 오류를 해결 ###
# url = 'https://www.hidoc.co.kr/healthqna/list?page=1'
# req = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) # headers 부분추가
# print(req.content.decode('utf-8'))


soup = BeautifulSoup(request.content, features="html.parser")   # html 파싱
request.close()

find_str = soup.find('div', attrs={'container_inner clear_g'})    # 가져올 div 전체 내용 부분 탐색
# print(find_str)
file = open("./saveJsonTest.json", "w", encoding='UTF-8')   # json 생성

for info in find_str.find_all('div', attrs={'class':'box_type1 qna_main'}): # div 부분 핵심 내용 탐색
    temp_dict = {}
  
    title = info.find("strong").text
    nUrl = url + str(info.find("div", attrs={'class':'cont'}).a['href']).strip()
    contents = info.find('p', attrs={'class': 'desc'}).text
    # print(title + ' ok')
    # print(nUrl + ' ok')
    # print(contents + ' end' + '\n')
    temp_dict = {'title': title, 'nUrl': nUrl, 'contents': contents}
    file.write(json.dumps(temp_dict,ensure_ascii=False,indent='\t'))
    # print(temp_dict)

file.close()