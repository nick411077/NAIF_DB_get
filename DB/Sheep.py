import requests
from bs4 import BeautifulSoup
from .Mongo import mongoOut


def Sheep():
    response = requests.get("https://www.naif.org.tw/infoSheepDaily.aspx?frontTitleMenuID=37&frontMenuID=159")
    soup = BeautifulSoup(response.text, "html.parser")
    key=[]
    value =["","","",""]
    key.append(soup.find('div', class_="ScrollForm").find('th').text)
    value[0]=soup.find('div', class_="ScrollForm").find_all('th')[1].text
    for i in range(0,3):
        key.append(soup.find('div', class_="ScrollForm").find_all('tr')[1].find_all('th')[i].text)
    for i in range(2,4):
        value[1] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find('th').text
        value[2] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find('td').text
        value[3] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('td')[1].text

        mongoOut(key, value, "羊交易", 0)
