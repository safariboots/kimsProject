import requests
from bs4 import BeautifulSoup
import json
import csv

def mnet_Crawling(html): 
    temp_list = []
    temp_dict = {}
    
    page = 0
    find_str = html.find('div', attrs={'container_inner clear_g'})    # 가져올 div 전체 내용 부분 탐색

    for info in find_str.find_all('div', attrs={'class':'box_type1 qna_main'}): # div 부분 핵심 내용 탐색
        title = info.find("strong").text    # 제목가져오기
        nUrl = url + str(info.find("div", attrs={'class':'cont'}).a['href']).strip()    # 공백문자처리후 url가져오기
        contents = info.find('p', attrs={'class': 'desc'}).text     # 내용가져오기

        #temp_dict= {'title': title, 'nUrl': nUrl, 'contents': contents}    # json형태로 저장하기
        
        temp_list.append([title, nUrl, contents])
        temp_dict[str(page)] = {'title': title, 'nUrl': nUrl, 'contents': contents}
        page += 1
    
    return temp_list, temp_dict


def toCSV(mnet_list):
    with open('mnet_chart.csv', 'w', encoding='utf-8', newline='') as file :
        csvfile = csv.writer(file)
        for row in mnet_list:
            csvfile.writerow(row)
            

def toJson(mnet_dict):
    with open('mnet_chart.json', 'w', encoding='utf-8') as file :
        json.dump(mnet_dict, file, ensure_ascii=False, indent='\t')




mnet_list = []
mnet_dict = {}

url = "https://www.hidoc.co.kr/healthqna/"
boardUrl = 'https://www.hidoc.co.kr/healthqna/list?page='   # 게시물 리스트
no = 1  # 게시물 번호
crawlingUrl=boardUrl+str(no)    # 실제가져올 게시물 페이지 url

# print(crawlingUrl)
request = requests.get(crawlingUrl, headers={"User-Agent": "Mozilla/5.0"}) # 게시물페이지 가져오기
#print(request)

html = BeautifulSoup(request.content, features="html.parser")   # html 파싱
request.close()




mnet_temp = mnet_Crawling(html)
mnet_list += mnet_temp[0]
mnet_dict = dict(mnet_dict, **mnet_temp[1])



# 리스트 출력
for item in mnet_list :
    print(item)
    
# 사전형 출력
for item in mnet_dict :
    print(item, mnet_dict[item]['title'], mnet_dict[item]['nUrl'], mnet_dict[item]['contents'])




# CSV파일 생성
toCSV(mnet_list)
# Json파일 생성
toJson(mnet_dict)



    
    
	