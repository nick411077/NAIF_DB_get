import requests
from bs4 import BeautifulSoup
from .Mongo import mongoOutG


def Feed():
    response = requests.get("https://www.naif.org.tw/infoFeedDaily.aspx?frontTitleMenuID=37&frontMenuID=160")
    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    for i in range(0, 3):
        data.append(soup.find('div', class_="ScrollForm").find_all('th')[i].text)
    for i in range(0, 7):
        data.append(soup.find('div', class_="ScrollForm").find_all('tr')[1].find_all('th')[i].text)
    for i in range(0, 12):
        data.append(soup.find('div', class_="ScrollForm").find_all('tr')[2].find_all('th')[i].text)
    data.append(soup.find('div', class_="ScrollForm").find_all('tr')[4].find('th').text)
    for i in range(0, 12):
        data.append(soup.find('div', class_="ScrollForm").find_all('tr')[4].find_all('td')[i].text)
    data.append(soup.find('div', class_="ScrollForm").find_all('tr')[5].find('th').text)
    for i in range(0, 12):
        data.append(soup.find('div', class_="ScrollForm").find_all('tr')[5].find_all('td')[i].text)

    print(data)
    print("----------")
    DATA = []
    DATA2 = []
    for A in range(2):

        Data = {}
        Data["日期"] = data[1 + 7 + 2 + 12 + (A * 13)]
        for B in range(2):
            Data["資料來源"] = data[1 + (B * 1)]
            if B == 0:
                for C in range(4):
                    Data["類別"] = data[1 + 2 + C]
                    for D in range(6):
                        if C == 0 and D < 2 and D >= 0:
                            Data["價錢"] = data[23 + D + (A * 13)]
                            Data["地區"] = data[10 + D]
                            DATA.append(Data.copy())
                        elif C == 1 and D < 4 and D >= 2:
                            Data["價錢"] = data[23 + D + (A * 13)]
                            Data["地區"] = data[10 + D]
                            DATA.append(Data.copy())
                        elif C == 2 and D < 5 and D >= 4:
                            Data["價錢"] = data[23 + D + (A * 13)]
                            Data["地區"] = data[10 + D]
                            DATA.append(Data.copy())
                        elif C == 3 and D < 6 and D >= 5:
                            Data["價錢"] = data[23 + D + (A * 13)]
                            Data["地區"] = data[10 + D]
                            DATA.append(Data.copy())
            else:
                for C in range(3):
                    Data["類別"] = data[1 + 2 + 4 + C]
                    for D in range(6):
                        if C == 0 and D < 2 and D >= 0:
                            Data["價錢"] = data[23 + D + 6 + (A * 13)]
                            Data["地區"] = data[10 + D + 6]
                            DATA2.append(Data.copy())
                        elif C == 1 and D < 4 and D >= 2:
                            Data["價錢"] = data[23 + D + 6 + (A * 13)]
                            Data["地區"] = data[10 + D + 6]
                            DATA2.append(Data.copy())
                        elif C == 2 and D < 6 and D >= 4:
                            Data["價錢"] = data[23 + D + 6 + (A * 13)]
                            Data["地區"] = data[10 + D + 6]
                            DATA2.append(Data.copy())
    mongoOutG(DATA)
    mongoOutG(DATA2)
    print("----------")
