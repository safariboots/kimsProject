from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json
import time
import random

boardUrl = 'https://www.hidoc.co.kr/healthstory/news?page='   # 게시물 리스트
contentsUrl = 'https://www.hidoc.co.kr'   # 실제 내용이 있는 주소

# file = open("./qnaHidoc.json", "w", encoding='UTF-8')   # json 생성

#### 자꾸 끊어지니 게시물 100페이지 씩 크롤링, 100x7 게시물을 한파일에 저장 #####
# crawlingUrl=boardUrl+str(no)    # 실제가져올 게시물 페이지 url, 처음 시작과 끝 url간격 설정(100), 파일 페이지 시작 설정
startNo = 2701         # 게시물 번호 시작 1, 101..
endNo = 2720         # 게시물 번호 끝 101, 201,..
fileNo = 27            # jsonFile번호 시작 0, 1..
#############################################################################

for i in range(0,1):      # 게시물 크롤링 횟수 시작 0 , 게시판 번호 약 36738 x 7 = 약 25만 페이지
    tempList_nUrl=[]    # 게시판 각 페이지의 url목록 배열생성    
    
    fileName = 'hidocNews' + str(fileNo) + '.json'
    file = open(fileName, "w", encoding='UTF-8')   # json 생성

        
    for page in range(startNo,endNo):             #페이지 갯수 설정 시작~끝-1
        crawlingUrl=boardUrl+str(page)    # 실제가져올 게시물 페이지 url
        request = requests.get(crawlingUrl, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
        soup = BeautifulSoup(request.content, features="html.parser")   # html 파싱
        request.close()
        
        print('처리중', page,'가져옴\n')    # 확인 - 게시물페이지 처리 확인
        
        
        find_str = soup.find('ul', attrs={'news_list'})    # 가져올 ul 내용 부분 탐색
        
        for info in find_str.find_all('li', attrs={'class':'news_item'}): # li 부분 핵심 내용 탐색            
            nUrl = contentsUrl + str(info.find('div', attrs={'class':'news_info'}).a['href']).strip()    # 공백문자처리후 url가져오기
            print(nUrl)
            tempList_nUrl.append(nUrl)  # 주소 목록 배열에 url추가

        
    # print(tempList_nUrl) # 수집된 주소값 목록 확인    
    # ### 중복 주소목록 제거 #######
    # result = []     # 중복 제거된 값들이 들어갈 리스트
    # c_count=0
    # for value in tempList_nUrl:
    #     if value not in result:
    #         result.append(value)
    #         c_count += 1
    # print(result, '\n', '===============',c_count,'==========================') # 확인 - 중복제거 결과
    # print(tempList_nUrl)   # 확인 - 게시판 페이지별 url목록 배열 출력 
    # #############################


    contentsTojson = {}  # json 딕셔너리 생성


    ####################### 질문, 답변 게시물 컨텐츠 크롤링 ##########################
    count_newsContents = 0            # 확인 - 질문 갯수 확인
    for contentsAddr in tempList_nUrl:    # 컨텐츠 페이지 주소 (coontentsAddr) # ID로 활용 
        temp_dict = {}  # 임시 딕셔너리 생성
        print(count_newsContents, '....컨텐츠 페이지 처리중\n')     # 멈춤효과가 좀 더 있음(for문에서 한번씩 쉬어주는효과?)
        
        
        request = requests.get(contentsAddr, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
        soup = BeautifulSoup(request.text, features="html.parser")   # html 파싱
        request.close()
        
        print(contentsAddr, '\n')   # 확인 - 현재 해당 주소 확인
        
        try:
            nTitle = soup.find('h3', attrs={'class': 'article_tit'}).text # 컨텐츠 목록내용 가져오기 - 질문 제목
            nDate = soup.find('span', attrs={'class': 'date'}).text # 컨텐츠 목록내용 가져오기 - 질문 날짜
            # print(nTitle, nDate)
    
                
            ### 뉴스내용 탐색 및 저장 ###
            tag_search  = soup.find('div', attrs={'class': 'article_body'})  # 컨텐츠 목록내용 가져오기
            # print(tag_search)
            
            check_answerCount=1     # 답변번호 카운트
            newsContentsList=[]       # 답변목록 배열 생성
            for news in tag_search.find_all('p'):
                check_null = news.text      # 답변내용 임시 저장공간 생성
                if check_null != '\n':      # 내용이 있는지 확인
                    # print('Thank you!! \n')    # 확인 - 개행문자 유무 확인
                    # print('Answer_', check_answerCount,': ', news.text,'\n----------------------------\n\n') # 확인 - 뉴스 갯수
                    tempContents = news.text  # 답변 정형화
                    newsContentsList.append(tempContents)    # 답변 목록에 추가
                    # check_answerCount += 1      # 답변 번호 증가


            temp_dict[str(count_newsContents)] = {'title': nTitle, 'Url': contentsAddr, 'date': nDate, 'answer': newsContentsList} # json 형태로 임시 저장
            # print(temp_dict)        # temp_dict 내용 확인
            contentsTojson = dict(contentsTojson, **temp_dict)  # json 목록 생성
            count_newsContents += 1     # 확인 - 질문 갯수 카운트 증가
        except :
            errUrl = nUrl
            print(errUrl, '페이지에러발생 \n')
        
    
    file.write(json.dumps(contentsTojson,ensure_ascii=False,indent='\t'))    # json파일 만들기
    file.close()    # 파일 닫기
    
    print('좀 쉴께요 \n')   # 확인 - 쉬는지 확인
    time.sleep( random.uniform(5,10) )   # 랜덤한 시간으로  쉬어줘.. 최소 10초-20초 정도가 안걸림
    
    # time.sleep(20)      # 20초 휴식
    # print('질문 갯수: ', count_question, '\n') # 확인 - 질문갯수
    ############################################################################
    fileNo += 1             # jsonFile번호 증가
    startNo = startNo + 100       # 게시물 번호 시작 1, 101, 201, 301, 401,....
    endNo = endNo + 100           # 게시물 번호 끝   101, 201, 301, 401,...
    
    print('지금', i,'번째\n')
    if i%10==0:
        print('그만 부려먹어라.. 좀 쉬어야함..\n')
        time.sleep( random.uniform(30,60))  # 1분이내 랜덤하게 쉬어가기
        
