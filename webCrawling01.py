import requests
from bs4 import BeautifulSoup
import json


# response = requests.get("http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=035720")
# print(response.text)



url = "https://newstapa.org"

request = requests.get('https://newstapa.org/recent')

soup = BeautifulSoup(request.content, features="html.parser")
request.close()

# print(soup)

print('########################################')
# find_str = soup.find('div', attrs={'class':'col-lg-3 col-md-6 columns'})
find_str = soup.find('div', attrs={'list_section-slider-row-block'})
# print(find_str)

file = open("./saveJsonTest.json", "w", encoding='UTF-8')


for news in find_str.find_all('div', attrs={'class':'col-lg-3 col-md-6 columns'}):
    temp_dict = {}
    # print(news)
    # print(news.find("h6", attrs={'class': 'font-weight-blold'}).text)  # 기사제목
   
    title = news.find("h6").text
    nUrl = url + str(news.find("h6", attrs={'class':'font-weight-bold'}).a['href']).strip()
    newsDate = news.find("p", attrs={'class': 'float-right mt-2 date'}).text
    imgLink = news.find('figure', attrs={'class': 'article-image'}).img['src']
    # print(title + ' ok')
    # print(nUrl + ' ok')
    # print(newsDate + ' ok')
    # print(imgLink + ' end' + '\n')
    temp_dict = {'title': title, 'nUrl': nUrl, 'newsDate': newsDate, 'imgLink': imgLink}
    file.write(json.dumps(temp_dict,ensure_ascii=False))
    print(temp_dict)

file.close()




#     print(news.h6.text)   # 기사제목
#     print(url + str(news.find("h6", attrs={'class':'font-weight-bold'}).a['href']).strip()) # 기사 url
    
# # 기사 url
#    print(news.find("p", attrs={'class': 'float-right mt-2 date'}).text) # 기사날짜
#     # print(news.find('figure', attrs={'class': 'article-image'}).img['src']) # 이미지 url
#     print(news.figure.img['src']+"-ok")
