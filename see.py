import datetime
import codecs
wr=open('shop_flow_new.csv','a')
wr.write('shop_id,date,cus_flow\n')
shop={}
for line in codecs.open('shop_flow.csv','r',encoding="utf-8"):
    line=line.replace('\n','')
    array=line.split(',')
    if array[0]=='shop_id':
        continue
    array[0]=int(array[0])
    array[1]=datetime.datetime.strptime(array[1],'%Y-%m-%d')
    array[1]=array[1].date()
    array[2]=int(array[2])
    if shop.get(array[0])==None:
        shop[array[0]]={}
    shop[array[0]][array[1]]=array[2]
for key in shop.keys():
    shop[key]=sorted(shop[key].items(),key=lambda x:x[0])
shop=sorted(shop.items(),key=lambda x:x[0])
#shop=sorted(shop.items(),key=lambda x:x[0])
for i in range(len(shop)):
    #print(shop[i][0])
    for j in range(len(shop[i][1])):
        wr.write(str(shop[i][0])+','+str(shop[i][1][j][0])+','+str(shop[i][1][j][1])+'\n')
        #print(shop[i][1][j][0])
        #print(shop[i][1][j][1])
wr.close()

        

