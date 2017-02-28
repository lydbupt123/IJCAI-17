import codecs
import datetime
import time

wr=open('shop_flow.csv','a')
wr.write('shop_id,date,cus_flow\n')
info={}
for line in codecs.open('user_pay.txt','r',encoding="utf-8"):
    line=line.replace('\n','')
    #print(line)
    array=line.split(',')
    if array[0]=='' or array[1] == '' or array[2]=='':
        continue
    shop_id=array[1]
    #print(type(shop_id))
    timeStamp=datetime.datetime.strptime(array[2],'%Y-%m-%d %H:%M:%S')
    date=str(timeStamp.date())
    #print(type(date))
    if info.get(shop_id)==None:
        info[shop_id]={}
    if info[shop_id].get(date)==None:
        info[shop_id][date]=1
    else:
        info[shop_id][date]+=1
for shop in info.keys():
    for date in info[shop].keys():
        wr.write(shop+','+date+','+str(info[shop][date])+'\n')
wr.close()
    
