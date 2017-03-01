import datetime
holiday_list=['2015-9-3','2015-9-4','2015-9-5','2015-9-26','2015-9-27','2015-10-1','2015-10-2','2015-10-3','2015-10-4','2015-10-5','2015-10-6','2015-10-7','2016-1-1','2016-1-2','2016-1-3',\
              '2016-2-7','2016-2-8','2016-2-9','2016-2-10','2016-2-11','2016-2-12','2016-2-13','2016-2-14','2016-2-22','2016-4-2','2016-4-3','2016-4-4','2016-4-30','2016-5-1','2016-5-2'\
              ,'2016-6-9','2016-6-10','2016-6-11','2016-9-15','2016-9-16','2016-9-17','2016-10-1','2016-10-2','2016-10-3','2016-10-4','2016-10-5','2016-10-6','2016-10-7']
index=0
for i in holiday_list:
    holiday_list[index]=datetime.datetime.strptime(i,'%Y-%m-%d').date()
    index+=1
wr=open('full_new.csv','a')
for line in open('full.csv'):
    line=line.replace('\n','')
    #print(line)
    array=line.split(',')
    if array[0]=='shop_id':
        wr.write('shop_id,city_name,location_id,per_pay,score,comment_cnt,shop_level,year,month,day,weekend,holiday,air,h_tem,l_tem,weather,cate_1_name,cate_2_name,cate_3_name,cus_flow\n')
        continue
    date=datetime.datetime.strptime(array[7],'%Y-%m-%d').date()
    isHoliday=0
    try:
        if holiday_list.index(date)>=0:
            isHoliday=1
    except:
        isHoliday=0
    wr.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(array[0],array[1],array[2],array[3],array[4],array[5],array[6],date.year,date.month,date.day,date.weekday(),isHoliday,array[8],array[9],array[10],array[11],array[12],array[13],array[14],array[15]))
wr.close()
