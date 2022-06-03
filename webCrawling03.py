from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json
import time
import random

url = "https://www.hidoc.co.kr/"
boardUrl = 'https://www.hidoc.co.kr/healthqna/list?page='   # 게시물 리스트
contentsUrl = 'https://www.hidoc.co.kr/healthqna/'   # 실제 내용이 있는 주소
# no = 1  # 게시물 번호
file = open("./qnaHidoc.json", "w", encoding='UTF-8')   # json 생성

#### 자꾸 끊어지니 게시물 100페이지 씩 크롤링, 100x7 게시물을 한파일에 저장 #####
# crawlingUrl=boardUrl+str(no)    # 실제가져올 게시물 페이지 url, 처음 시작과 끝 url간격 설정(100), 파일 페이지 시작 설정
startNo = 6701         # 게시물 번호 시작 1, 101..
endNo = 6801         # 게시물 번호 끝 101, 201,..
fileNo = 67            # jsonFile번호 시작 0, 1..
#############################################################################

for i in range(0,300):      # 게시물 크롤링 횟수 시작 0 , 게시판 번호 약 36500
    tempList_nUrl=[]    # 게시판 각 페이지의 url목록 배열생성    
    
    fileName = 'qnahidoc' + str(fileNo) + '.json'
    file = open(fileName, "w", encoding='UTF-8')   # json 생성

        
    for page in range(startNo,endNo):             #페이지 갯수 설정 시작~끝-1
        crawlingUrl=boardUrl+str(page)    # 실제가져올 게시물 페이지 url
        request = requests.get(crawlingUrl, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
        soup = BeautifulSoup(request.content, features="html.parser")   # html 파싱
        request.close()
        
        print('처리중', page,'가져옴\n')    # 확인 - 게시물페이지 처리 확인
        
        #### 상태체크 ####
        # if request.status_code!=200:
        #     print('이런 큰일이다')
        # print(request.status_code)
        ##################
        
        #### 100페이지 마다 쉬어줘 ######
        # if page%10 == 0:
        #     time.sleep( random.uniform(1,2) )   # 랜덤한 시간으로  쉬어줘
        #     print('지금', page,'여\n')
        ################################
        
        find_str = soup.find('div', attrs={'container_inner clear_g'})    # 가져올 div 전체 내용 부분 탐색
        
        for info in find_str.find_all('div', attrs={'class':'box_type1 qna_main'}): # div 부분 핵심 내용 탐색
            #temp_dict = {}
            nUrl = contentsUrl + str(info.find("div", attrs={'class':'cont'}).a['href']).strip()    # 공백문자처리후 url가져오기
            tempList_nUrl.append(nUrl)  # 주소 목록 배열에 url추가

        
        
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
    count_question = 0           # 확인 - 질문 갯수 확인
    for contentsAddr in tempList_nUrl:    # 컨텐츠 페이지 주소 (coontentsAddr) # ID로 활용 
        temp_dict = {}  # 임시 딕셔너리 생성
        print(count_question, '....컨텐츠 페이지 처리중\n')
        
        
        request = requests.get(contentsAddr, headers={"User-Agent": "Mozilla/5.0"}) # 게시물 페이지 내용 가져오기
        soup = BeautifulSoup(request.text, features="html.parser")   # html 파싱
        request.close()
        
        qTitle = soup.find('strong', attrs={'class': 'tit'}).text # 컨텐츠 목록내용 가져오기 - 질문 제목
        qDate = soup.find('span', attrs={'class': 'txt_time'}).text # 컨텐츠 목록내용 가져오기 - 질문 날짜
        
        ### 컨텐츠 목록내용 가져오기 - 질문내용 ###
        tag_div = soup.find('div', attrs={'class': 'box_type1 view_question'})  # 해당 위치의 div 탐색
        qContents = tag_div.find('div', attrs={'class': 'inner'}).p.text    # 탐색된 div 내용중 p 안의 내용 저장
        # print(contentsAddr, '\n', qDate, '\n', qTitle, '\n', qContents, '\n')  # 확인 - 주소,날짜,제목,내용    
    
            
        ### 답변 내용 탐색 및 저장 ###
        tag_search  = soup.find('div', attrs={'view_answer'})  # 컨텐츠 목록내용 가져오기 - 답변 내용 전체 가져오기
        
        check_answerCount=1     # 답변번호 카운트
        answerList=[]       # 답변목록 배열 생성
        for news in tag_search.find_all('div', attrs={'desc'}):
            check_null = news.text      # 답변내용 임시 저장공간 생성
            if check_null != '\n':      # 내용이 있는지 확인
                # print('Thank you!! \n')    # 확인 - 개행문자 유무 확인
                # print('Answer_', check_answerCount,': ', news.text,'\n----------------------------\n\n') # 확인 - 답변 갯수
                answerDoc = 'Answer'+ str(check_answerCount) + "-" + news.text  # 답변 정형화
                answerList.append(answerDoc)    # 답변 목록에 추가
                check_answerCount += 1      # 답변 번호 증가

        temp_dict[str(count_question)] = {'title': qTitle, 'Url': contentsAddr, 'date': qDate, 'question': qContents, 'answer': answerList} # json 형태로 임시 저장
        # print(temp_dict)        # temp_dict 내용 확인
        contentsTojson = dict(contentsTojson, **temp_dict)  # json 목록 생성 
        count_question += 1     # 확인 - 질문 갯수 카운트 증가 
        
    
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
