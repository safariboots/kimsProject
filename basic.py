from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json

# response = requests.get("https://www.hidoc.co.kr/healthstory/news/C0000707363")
# print(response.text)

contentsAddr = "https://www.hidoc.co.kr/healthstory/news/C0000707363"
request = requests.get(contentsAddr, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
soup = BeautifulSoup(request.text, features="html.parser")   # html 파싱
request.close()

# test = soup.find('div', attrs={'class': 'container_inner clear_g'}).text

# print(test)
nTitle = soup.find('h3', attrs={'class': 'article_tit'}).text # 컨텐츠 목록내용 가져오기 - 질문 제목
nDate = soup.find('span', attrs={'class': 'date'}).text # 컨텐츠 목록내용 가져오기 - 질문 날짜
print(nTitle, nDate)

########################### 여기부터 끝까지 주석처리 #############################

# # url = "https://www.hidoc.co.kr"
# boardUrl = 'https://www.hidoc.co.kr/healthstory/news?page=1'   # 게시물 리스트
# contentsUrl = 'https://www.hidoc.co.kr'   # 실제 내용이 있는 주소
# request = requests.get(boardUrl,headers={"User-Agent": "Mozilla/5.0"})

# soup = BeautifulSoup(request.content, features="html.parser")
# request.close()

# find_str = soup.find('ul', attrs={'news_list'})
# # print(find_str)




# for info in find_str.find_all('li', attrs={'class':'news_item'}):
#     tempList_nUrl=[]
#     # print(news.find("a", attrs={'class': 'tit'}).text)  # 기사제목
#     # print(info)
   
    
#     nUrl = contentsUrl + str(info.find('div', attrs={'class':'news_info'}).a['href']).strip()    # 공백문자처리후 url가져오기
#     print(nUrl)
#     tempList_nUrl.append(nUrl)  # 주소 목록 배열에 url추가



#     contentsTojson = {}  # json 딕셔너리 생성






# ####################### 질문, 답변 게시물 컨텐츠 크롤링 ##########################
# count_newsContents = 0           # 확인 - 질문 갯수 확인
# for contentsAddr in tempList_nUrl:    # 컨텐츠 페이지 주소 (coontentsAddr) # ID로 활용 
#     temp_dict = {}  # 임시 딕셔너리 생성
#     print(count_newsContents, '....컨텐츠 페이지 처리중\n')     # 멈춤효과가 좀 더 있음(for문에서 한번씩 쉬어주는효과?)
    
    
#     request = requests.get(contentsAddr, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
#     soup = BeautifulSoup(request.text, features="html.parser")   # html 파싱
#     request.close()
    
#     print(contentsAddr, '\n')   # 확인 - 현재 해당 주소 확인
    
#     try:
#         nTitle = soup.find('h3', attrs={'class': 'article_tit'}).text # 컨텐츠 목록내용 가져오기 - 질문 제목
#         nDate = soup.find('span', attrs={'class': 'date'}).text # 컨텐츠 목록내용 가져오기 - 질문 날짜
#         # print(nTitle, nDate)
  
            
#         ### 뉴스내용 탐색 및 저장 ###
#         tag_search  = soup.find('div', attrs={'class': 'article_body'})  # 컨텐츠 목록내용 가져오기
#         # print(tag_search)
        
#         check_answerCount=1     # 답변번호 카운트
#         newsContentsList=[]       # 답변목록 배열 생성
#         for news in tag_search.find_all('p'):
#             check_null = news.text      # 답변내용 임시 저장공간 생성
#             if check_null != '\n':      # 내용이 있는지 확인
#                 # print('Thank you!! \n')    # 확인 - 개행문자 유무 확인
#                 # print('Answer_', check_answerCount,': ', news.text,'\n----------------------------\n\n') # 확인 - 뉴스 갯수
#                 tempContents = news.text  # 답변 정형화
#                 newsContentsList.append(tempContents)    # 답변 목록에 추가
#                 # check_answerCount += 1      # 답변 번호 증가

#         temp_dict[str(count_newsContents)] = {'title': nTitle, 'Url': contentsAddr, 'date': nDate, 'answer': newsContentsList} # json 형태로 임시 저장
#         # print(temp_dict)        # temp_dict 내용 확인
#         contentsTojson = dict(contentsTojson, **temp_dict)  # json 목록 생성 

#     except :
#         errUrl = nUrl
#         print(errUrl, '페이지에러발생 \n')
# fileName = 'hidocNews' + str(1) + '.json'
# file = open(fileName, "w", encoding='UTF-8')   # json 생성
# file.write(json.dumps(contentsTojson,ensure_ascii=False,indent='\t'))    # json파일 만들기
# file.close()    # 파일 닫기
