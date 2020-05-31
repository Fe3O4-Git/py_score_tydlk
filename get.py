import os,requests,time
if not os.path.exists("raw"):
    os.makedirs("raw")
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
        try:
            file = open("./raw/"+str_room+"-"+str_seat+".html",mode='r')
            print("Already here: "+str_room+"-"+str_seat)
            file.close
        except:
            file = open("./raw/"+str_room+"-"+str_seat+".html",mode='w')
            for i in range(0,99,1):
                try:
                    page = requests.get("http://score.tydlk.cn/search/msingle?clkid=167&xuehao=115019"+str_room+str_seat)
                    break
                except:
                    print("Failed to get,retrying: "+str_room+"-"+str_seat)
                    time.sleep(1)
            file.write (page.text)
            file.close
    seat = 1
