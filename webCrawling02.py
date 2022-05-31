from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.hidoc.co.kr"
boardUrl = 'https://www.hidoc.co.kr/healthqna/list?page='   # 게시물 리스트
contentsUrl = 'https://www.hidoc.co.kr/healthqna/view/'   # 실제 내용이 있는 주소
no = 1  # 게시물 번호

# crawlingUrl=boardUrl+str(no)    # 실제가져올 게시물 페이지 url

for page in range(1,3):
      crawlingUrl=boardUrl+str(page)    # 실제가져올 게시물 페이지 url
  #print(crawlingUrl)
  request = requests.get(crawlingUrl, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기

  soup = BeautifulSoup(request.content, features="html.parser")   # html 파싱
  request.close()

  find_str = soup.find('div', attrs={'container_inner clear_g'})    # 가져올 div 전체 내용 부분 탐색


  tempList_nUrl=[]    # 게시판 각 페이지의 url목록 
  for info in find_str.find_all('div', attrs={'class':'box_type1 qna_main'}): # div 부분 핵심 내용 탐색
    temp_dict = {}
    nUrl = url + str(info.find("div", attrs={'class':'cont'}).a['href']).strip()    # 공백문자처리후 url가져오기
    tempList_nUrl.append(nUrl)  # 목록에 url추가

  #print(tempList_nUrl)   # 게시판 페이지별 url목록 출력 

  for addrNo in tempList_nUrl:
    contentsAddr = contentsUrl+str(addrNo)    # 컨텐츠 페이지 주소 (coontentsAddr)
    #print(contentsAddr)


    request = requests.get(contentsAddr, headers={"User-Agent": "Mozilla/5.0"}) # 컨텐츠 페이지 내용 가져오기
    soup = BeautifulSoup(request.content, features="html.parser")   # html 파싱
    request.close()

    ##### 질문제목,날짜,답변 데이터 가져오기 #############
    find_str = soup.find('div', attrs={'health_view'})    # 가져올 div 전체 내용 부분 탐색
    title = find_str.find("strong",{"class": "tit"}).text
    
    print(title)

    # for info in find_str.find_all('div', attrs={'class':'box_type1 qna_main'}): # div 부분 핵심 내용 탐색
    #     title = info.find("strong").text    # 제목가져오기
    #     nUrl = url + str(info.find("div", attrs={'class':'cont'}).a['href']).strip()    # 공백문자처리후 url가져오기
    #     contents = info.find('p', attrs={'class': 'desc'}).text     # 내용가져오기
    #     print(title)

 
 
 
 
 
 
 
    #contents = info.find('p', attrs={'class': 'desc'}).text     # 내용가져오기
    #print(title + ' ok')
    #print(nUrl + ' ok')
    #print(contents + ' end' + '\n')
