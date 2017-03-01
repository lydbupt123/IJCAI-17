import codecs
city=['黄冈', '三亚', '汉中', '宝鸡', '泉州', '石家庄', '东营', '莆田', '盐城',\
       '衢州', '扬州', '清远', '哈尔滨', '营口', '郑州', '镇江', '乐山', '福州',\
       '珠海', '嘉兴', '襄阳', '荆门', '泰州', '辽阳', '廊坊', '南平', '南宁',\
       '台州', '濮阳', '北京', '杭州', '聊城', '淮安', '铜陵', '常州', '芜湖', \
       '咸阳', '昆明', '锦州', '绵阳', '长沙', '邯郸', '黄石', '株洲', '自贡', \
       '绍兴', '抚顺', '淮北', '葫芦岛', '龙岩', '贵阳', '湖州', '思茅', '阳江',\
       '丽水', '阜阳', '荆州', '沈阳', '中山', '肇庆', '安康', '柳州', '徐州', \
       '石河子', '十堰', '上海', '烟台', '太原', '武汉', '湛江', '宁波', '德阳', \
       '江门', '上饶', '六安', '长治', '梧州', '蚌埠', '孝感', '成都', '济南', '南通'\
       , '达州', '金华', '深圳', '天门', '宿迁', '青岛', '东莞', '西安', '咸宁', '日照'\
       , '南京', '汕尾', '重庆', '大连', '苏州', '天津', '威海', '保定', '宜昌', '厦门'\
       , '南昌', '漳州', '黄山', '三明', '宁德', '合肥', '惠州', '张家口', '济宁', \
       '温州', '潍坊', '信阳', '邢台', '玉林', '广州', '舟山', '洛阳', '无锡', '通辽',\
       '佛山']
citys={}
for i,c in enumerate(city):
    citys[c]=i+1

cus={}
for line in open('new_shop_flow.csv'):
    line=line.replace('\n','')
    #print(line)
    array=line.split(',')
    if array[0]=='shop_id':
        continue
    if cus.get(array[0])==None:
        cus[array[0]]={}
    cus[array[0]][array[2]]=[array[-2],array[-1]]
    
wr=open('new_data.csv','a')
wr.write('shop_id,city_name,location_id,per_pay,score,comment_cnt,shop_level,date,air,cate_1_name,cate_2_name,cate_3_name,cus_flow\n')
for line in open('data_shop_info.csv'):
    line=line.replace('\n','')
    #print(line)
    array=line.split(',')
    if array[0]=='shop_id':
        continue
    detail=cus[array[0]]
    for key in detail.keys():
        wr.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(array[0],array[1],array[2],array[3],array[4],array[5],array[6],key,detail[key][0],array[7],array[8],array[9],detail[key][1]))
wr.close()
    
    
    
