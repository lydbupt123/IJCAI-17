import codecs
import datetime
city_weather={}
for line in codecs.open('weather_all.csv','r',encoding='utf-8'):
    line=line.replace('\n','')
    line=line.replace('\r','')
    array=line.split(',')
    if city_weather.get(array[0])==None:
        city_weather[array[0]]={}
    date=datetime.datetime.strptime(array[1],'%Y-%m-%d').date()
    city_weather[array[0]][date]=[array[2],array[3],array[4]]
wr=open('full.csv','a')
for line in open('new_data.csv'):
    line=line.replace('\n','')
    #print(line)
    array=line.split(',')
    if array[0]=='shop_id':
        wr.write('shop_id,city_name,location_id,per_pay,score,comment_cnt,shop_level,date,air,h_tem,l_tem,weather,cate_1_name,cate_2_name,cate_3_name,cus_flow\n')
        continue
    detail=city_weather[array[1]]
    date=datetime.datetime.strptime(array[7],'%Y-%m-%d').date()
    wlist=[]
    try:
        wlist=detail[date]
    except:
        continue
    wr.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7],array[8],wlist[0],wlist[1],wlist[2],array[9],array[10],array[11],array[12]))
wr.close()

    
        
