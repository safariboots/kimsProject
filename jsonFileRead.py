from email.policy import strict
import requests
from bs4 import BeautifulSoup
import json


with open("./saveJsonTest.json",'r', encoding='UTF8') as f:
  data = json.load(f,strict=False)

print(data)