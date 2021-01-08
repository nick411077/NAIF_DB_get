import pymongo

myclient = pymongo.MongoClient("mongodb+srv://nick411077:nick10279@nickcandiscordbot-iqnfx.gcp.mongodb.net/test?retryWrites=true&w=majority")#位置
mydb = myclient["txt"]#名稱

def mongoOut(KEY,VALUE,NAME,method):#將資料檢查在放入資料庫
    mycol = mydb[NAME]
    Data = {}
    YN = True

    for aa in range(len(VALUE)):
        Data[KEY[aa]]=VALUE[aa]
         
    print(Data)  
    BD = mycol.find()
    for bd in BD:
        if method == 1:
            if bd.get("日期") == Data["日期"] and bd.get("價量項目") == Data["價量項目"]:
                YN=False
        else:
            if bd.get("日期") == Data["日期"]:
                YN=False
    if YN:
        xxx=mycol.insert_one(Data)
    print("-----------------")


def mongoOutG(DATA):
    mycol = mydb["飼料進口"] ##資料排列有困難，資料凌亂。
    YN = [True]*len(DATA)
         
    print(DATA)  
    BD = mycol.find()
    for bd in BD:
        for i in range(len(DATA)):
            if bd.get("日期") == DATA[i].get("日期") and bd.get("資料來源") == DATA[i].get("資料來源") and bd.get("類別") == DATA[i].get("類別") and bd.get("地區") == DATA[i].get("地區"):
                YN[i]=False
    for i in range(len(DATA)): 
        if YN[i]:
            xxx=mycol.insert_one(DATA[i])
    print("-----------------")


def Add():#重資料庫取資料在加總
    mycol = mydb["毛豬交易"]
    BD =mycol.find()
    JZ ={}
    for i in BD:
        try:
            if i.get('交易頭數')==' ':
                JZ[i.get('價量項目')]+=0
            else:
                JZ[i.get('價量項目')]+=int(i.get('交易頭數'))
        except:
            if i.get('交易頭數')==' ':
                JZ[i.get('價量項目')]=0
            else:
                JZ[i.get('價量項目')]=int(i.get('交易頭數'))
    print(JZ)
