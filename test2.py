from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json


# response = requests.get("http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=035720")
# print(response.text)



url = "https://www.hidoc.co.kr/healthqna/view/C0000703070"

request = requests.get(url,headers={"User-Agent": "Mozilla/5.0"})

soup = BeautifulSoup(request.content, features="html.parser")
request.close()
print(soup.find('strong', attrs={'class': 'tit'}).text)






# find_str = soup.find('div', attrs={'list_section-slider-row-block'})



# for news in find_str.find_all('div', attrs={'class':'view_answer'}):
    # temp_dict = {}
    # print(news.find("strong", attrs={'class': 'tit'}).text)

    # print(news)
    # print(news.find("h6", attrs={'class': 'font-weight-blold'}).text)  # 기사제목
   
    # title = news.find("h6").text
    # nUrl = url + str(news.find("h6", attrs={'class':'font-weight-bold'}).a['href']).strip()
    # newsDate = news.find("p", attrs={'class': 'float-right mt-2 date'}).text
    # imgLink = news.find('figure', attrs={'class': 'article-image'}).img['src']
    # print(title + ' ok')
    # print(nUrl + ' ok')
    # print(newsDate + ' ok')
    # print(imgLink + ' end' + '\n')
    # temp_dict = {'title': title, 'nUrl': nUrl, 'newsDate': newsDate, 'imgLink': imgLink}
    # file.write(json.dumps(temp_dict,ensure_ascii=False))
    # print(temp_dict)

# file.close()




#     print(news.h6.text)   # 기사제목
#     print(url + str(news.find("h6", attrs={'class':'font-weight-bold'}).a['href']).strip()) # 기사 url
    
# # 기사 url
#    print(news.find("p", attrs={'class': 'float-right mt-2 date'}).text) # 기사날짜
#     # print(news.find('figure', attrs={'class': 'article-image'}).img['src']) # 이미지 url
#     print(news.figure.img['src']+"-ok")
