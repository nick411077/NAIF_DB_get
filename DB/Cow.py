import requests
from bs4 import BeautifulSoup
from .Mongo import mongoOut


def Cow():
    response = requests.get("https://www.naif.org.tw/infoBeefCattleDaily.aspx?frontTitleMenuID=37&frontMenuID=158")
    soup = BeautifulSoup(response.text, "html.parser")
    key = []
    key.append('週數')
    key.append('日期')
    for i in range(1, 5):
        key.append(soup.find('div', class_="ScrollForm").find_all('th')[i].text)
    value = ["", "", "", "", "", ""]
    for i in range(1, 3):
        value[0] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('th')[0].text
        value[1] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('th')[1].text
        for x in range(0, 4):
            value[x + 2] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('td')[x].text
        mongoOut(key,value,"牛肉交易",0)
