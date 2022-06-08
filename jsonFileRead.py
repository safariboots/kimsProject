from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json

file = open('./qnaSample.json','r',encoding='UTF-8')
with open("./qnaSample.json",'r', encoding='UTF8') as f:
  data = json.load(f,strict=False)

print(data)