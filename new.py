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
    citys[c]=str(i+1)
#print(citys)
food_list=['东北菜', '闽菜', '粤菜', '砂锅/煲类/炖菜', '米粉/米线', '其它烘焙糕点', '中式烧烤', '饮品/甜点', '西北菜', '其它休闲食品', '其它快餐', '中式快餐', '日韩料理', '咖啡', '西式快餐', '其他餐饮美食', '奶茶', '香锅/烤鱼', '川味/重庆火锅', '自助餐', '熟食', '粥', '麻辣烫/串串香', '其它小吃', '冰激凌', '美食特产', '其它地方菜', '江浙菜', '面包', '川菜', '海鲜', '其它烧烤', '湖北菜', '上海本帮菜', '西餐', '其它火锅', '面点', '台湾菜', '湘菜', '咖啡厅', '蛋糕', '生鲜水果', '零食']
food_dict={}
for i,f in enumerate(food_list):
    food_dict[f]=str(i+1)
wr1=open('超市便利店.csv','a')
wr2=open('美食.csv','a')
wr2.write('shop_id,city_id,location_id,per_pay,score,comment_cnt,shop_level,type\n')
wr3=open('休闲娱乐.csv','a')
wr4=open('美发美容美甲.csv','a')
wr5=open('购物.csv','a')
wr6=open('医疗健康.csv','a')

with codecs.open('shop_info.txt','r',encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line=line.replace('\n','')
        array=line.split(',')
        line_new=''
        array[1]=citys[array[1]]
        if array[7]=='超市便利店':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i]+'\n')
            wr1.write(line_new)
        elif array[7]== '美食':
            array[-1]=food_dict[array[-1]]
            for i in range(8):
                if i !=7:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[-1]+'\n')
            wr2.write(line_new)
        elif array[7]=='休闲娱乐':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i]+'\n')
            wr3.write(line_new)
        elif array[7]=='美发/美容/美甲':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i]+'\n')
            wr4.write(line_new)
        elif array[7]=='购物':
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i]+'\n')
            wr5.write(line_new)
        else:
            for i in range(10):
                if i!=9:
                    line_new+=(array[i]+',')
                else:
                    line_new+=(array[i]+'\n')
            wr6.write(line_new)
        
    wr1.close()
    wr2.close()
    wr3.close()
    wr4.close()
    wr5.close()
    wr6.close()


        
        
        
