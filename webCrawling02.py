from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.hidoc.co.kr/"
boardUrl = 'https://www.hidoc.co.kr/healthqna/list?page='   # 게시물 리스트
contentsUrl = 'https://www.hidoc.co.kr/healthqna/'   # 실제 내용이 있는 주소
no = 1  # 게시물 번호

# crawlingUrl=boardUrl+str(no)    # 실제가져올 게시물 페이지 url

tempList_nUrl=[]    # 게시판 각 페이지의 url목록 배열생성
for page in range(1,3):             #페이지 갯수 설정 시작~끝-1
    crawlingUrl=boardUrl+str(page)    # 실제가져올 게시물 페이지 url
    request = requests.get(crawlingUrl, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
    soup = BeautifulSoup(request.content, features="html.parser")   # html 파싱
    request.close()

    find_str = soup.find('div', attrs={'container_inner clear_g'})    # 가져올 div 전체 내용 부분 탐색
  
    for info in find_str.find_all('div', attrs={'class':'box_type1 qna_main'}): # div 부분 핵심 내용 탐색
        #temp_dict = {}
        nUrl = contentsUrl + str(info.find("div", attrs={'class':'cont'}).a['href']).strip()    # 공백문자처리후 url가져오기
        tempList_nUrl.append(nUrl)  # 주소 목록 배열에 url추가
    
# ### 중복 주소목록 제거 ###
# result = []     # 중복 제거된 값들이 들어갈 리스트
# c_count=0
# for value in tempList_nUrl:
#     if value not in result:
#         result.append(value)
#         c_count += 1
# print(result, '\n', '===============',c_count,'==========================') # 확인 - 중복제거 결과
# print(tempList_nUrl)   # 확인 - 게시판 페이지별 url목록 배열 출력 
# ##########################


####################### 질문, 답변 게시물 컨텐츠 크롤링 ##########################
count_question = 0           # 확인 - 질문 갯수 확인
for contentsAddr in tempList_nUrl:    # 컨텐츠 페이지 주소 (coontentsAddr) # ID로 활용 
    # print(contentsAddr)       # 확인 - 페이지 주소
    request = requests.get(contentsAddr, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
    soup = BeautifulSoup(request.text, features="html.parser")   # html 파싱
    request.close()
    
    qTitle = soup.find('strong', attrs={'class': 'tit'}).text # 컨텐츠 목록내용 가져오기 - 질문 제목
    qDate = soup.find('span', attrs={'class': 'txt_time'}).text # 컨텐츠 목록내용 가져오기 - 질문 날짜
    
    ### 컨텐츠 목록내용 가져오기 - 질문내용 ###
    tag_div = soup.find('div', attrs={'class': 'box_type1 view_question'})  # 해당 위치의 div 탐색
    qContents = tag_div.find('div', attrs={'class': 'inner'}).p.text    # 탐색된 div 내용중 p 안의 내용 저장
    
    
    count_question += 1     # 확인 - 질문 갯수 카운트 증가
    print(contentsAddr, '\n', qDate, '\n', qTitle, '\n', qContents, '\n')  # 확인 - 주소,날짜,제목,내용    
    
    ### 답변 내용 탐색 및 저장 ###
    tag_search  = soup.find('div', attrs={'view_answer'})  # 컨텐츠 목록내용 가져오기 - 답변 내용 전체 가져오기
    
    check_answerCount=1     # 해당 질문에 대한 답변 카운트
    for news in tag_search.find_all('div', attrs={'desc'}):
        check_null = news.text
        if check_null != '\n':
            # print('Fuck you!! \n')
            print('Answer_', check_answerCount,': ', news.text,'\n----------------------------\n\n') # 확인 - 답변 갯수
            check_answerCount += 1      # 확인 - 답변 갯수 증가
   
print('질문 갯수: ', count_question, '\n') # 확인 - 질문갯수
############################################################################
        
