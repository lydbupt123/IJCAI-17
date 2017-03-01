import codecs
import datetime


#读取空气指数信息
air={}
city=[]
for line in open('air.csv'):
    line=line.replace('\n','')
    array=line.split(',')
    if array[0]=='Date':
        for i in range(1,len(array)):
            air[int(array[i])]={}
            city.append(int(array[i]))
        print(len(city))
        continue
    for i in range(122):
        date=datetime.datetime.strptime(array[0],'%Y/%m/%d').date()
        air[city[i]][date]=int(array[i+1])
wr=open('new_shop_flow.csv','a')
for line in open('shop_flow.csv'):
    line=line.replace('\n','')
    array=line.split(',')
    if array[0]=='shop_id':
        wr.write('shop_id,city,date,air,cus_flow\n')
        continue
    date=datetime.datetime.strptime(array[2],'%Y-%m-%d').date()
    air_=''
    try:
        air_=air[int(array[1])][date]
        #print(air_)
    except:
        air_=''
    wr.write('%s,%s,%s,%s,%s\n'%(array[0],array[1],array[2],air_,array[3]))
wr.close()
        
