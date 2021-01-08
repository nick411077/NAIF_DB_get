import requests
from bs4 import BeautifulSoup
from .Mongo import mongoOut


def Pig():
    response = requests.get("https://www.naif.org.tw/infoPigSellDaily.aspx")
    soup = BeautifulSoup(response.text, "html.parser")
    key = []
    value = ["", "", "", "", ""]
    for i in range(0, 5):
        key.append(soup.find('div', class_="ScrollForm").find_all('th')[i].text)
    for i in range(1, 7):
        if i == 1 or i == 4:
            for x in range(0, 5):
                value[x] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('td')[x].text
        else:
            for x in range(0, 4):
                value[x + 1] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('td')[x].text
        mongoOut(key, value, "毛豬交易", 1)
