import requests
from bs4 import BeautifulSoup
from .Mongo import mongoOut


def GrassFeed():
    response = requests.get("https://www.naif.org.tw/infoGrassFeedDaily.aspx?frontTitleMenuID=37&frontMenuID=161")
    soup = BeautifulSoup(response.text, "html.parser")
    key = []
    key.append(soup.find('div', class_="ScrollForm").find('th').text)
    for i in range(0, 9):
        key.append(soup.find('div', class_="ScrollForm").find_all('tr')[1].find_all('th')[i].text)

    value = ["", "", "", "", "", "", "", "", "", ""]
    for i in range(2, 4):
        value[0] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find('th').text
        for x in range(0, 9):
            value[x] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('td')[x].text
        mongoOut(key, value, "草交易", 0)
