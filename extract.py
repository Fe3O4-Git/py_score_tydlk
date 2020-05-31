import csv
from bs4 import BeautifulSoup

data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
writer = csv.writer(open("data.csv",mode='w'))
writer.writerow(["考号","文理","班级","姓名",
                 "总分","班名","校名","联名",
                 "语文","数学","英语","物理","化学","生物","政治","历史","地理"])

def score(a,b):
    table = soup.find("table",class_="table_1").find_all("tr")[a].find_all("td")
    if b < 2:
        r = table[b].span.text
    else:
        r = table[b].text
    return r

for room in range(1,21,1):
    if room < 10:
        str_room = "0" + str(room)
    else:
        str_room = str(room)
    for seat in range(1,37,1):
        if seat < 10:
            str_seat = "0" + str(seat)
        else:
            str_seat = str(seat)
        soup = BeautifulSoup(open("./raw/"+str_room+"-"+str_seat+".html"),features="html5lib")
        if str(type(soup.find("span",class_="ml10")))=="<class 'bs4.element.Tag'>":
            break
        info = soup.find("div",class_="info").find_all("span")
        data[0] = info[1].text.lstrip("考号：")
        data[3] = info[0].text
        data[2] = soup.find("select",id="classSelect").find("option",selected=True).text
        data[4] = score(1,1)
        data[5] = score(1,2)
        data[6] = score(1,3)
        data[7] = score(1,4)
        data[8] = score(2,1)
        data[9] = score(3,1)
        data[10]= score(4,1)
        if score(5,0)=="物理":
            data[1] = "理"
            data[11] = score(5,1)
            data[12] = score(6,1)
            data[13] = score(7,1)
            data[14] = -1
            data[15] = -1
            data[16] = -1
        else:
            data[1] = "文"
            data[11] = -1
            data[12] = -1
            data[13] = -1
            data[14] = score(5,1)
            data[15] = score(6,1)
            data[16] = score(7,1)
        writer.writerow(data)
    seat = 1
