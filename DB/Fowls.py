import requests
from bs4 import BeautifulSoup
from .Mongo import mongoOut


def Fowls():
    response = requests.get("https://www.naif.org.tw/infoFowlsDaily.aspx?frontTitleMenuID=37&frontMenuID=157")
    soup = BeautifulSoup(response.text, "html.parser")
    key = []
    value = ["", "", "", "", "", "", "", "", "", "", "", ""]
    for i in range(0, 12):
        key.append(soup.find('div', class_="ScrollForm").find_all('th')[i].text)

    for i in range(1, 3):
        value[0] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find('th').text
        for x in range(1, 11):
            value[x] = soup.find('div', class_="ScrollForm").find_all('tr')[i].find_all('td')[x].text
        mongoOut(key, value, "家禽交易", 0)
