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
    citys[c]=i
#print(citys)
wr1=open('超市便利店.csv','a')
wr2=open('美食.csv','a')
wr3=open('休闲娱乐.csv','a')
wr4=open('美发美容美甲.csv','a')
wr5=open('购物.csv','a')
wr6=open('医疗健康.csv','a')

with codecs.open('shop_info.txt','r',encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        array=line.split(',')
        line_new=''
        if array[7]=='超市便利店':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i])
            wr1.write(line_new)
        elif array[7]== '美食':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i])
            wr2.write(line_new)
        elif array[7]=='休闲娱乐':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i])
            wr3.write(line_new)
        elif array[7]=='美发/美容/美甲':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i])
            wr4.write(line_new)
        elif array[7]=='购物':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i])
            wr5.write(line_new)
        else:
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i])
            wr6.write(line_new)
        
    wr1.close()
    wr2.close()
    wr3.close()
    wr4.close()
    wr5.close()
    wr6.close()


        
        
        
