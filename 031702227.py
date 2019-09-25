#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import json
def delete_substr(in_str, in_substr): #从字符串中删除子串函数
    if re.search(in_substr,in_str)!=None:
        start_loc = in_str.find(in_substr)
        len_substr = len(in_substr)
        res_str = in_str[:start_loc] + in_str[start_loc + len_substr:]
    else:
        res_str=in_str
    return res_str

flag=[]#标志
for i in range(0,10):
    flag.append(0)
list = [province, city, xian, zhen, lu, hao, fang]=['']*7
list1=['北京','天津','上海','重庆','河北','河南','云南','辽宁','黑龙江','湖南','安徽','山东','新疆维吾尔自治区','江苏','浙江','江西','湖北','广西壮族自治区','甘肃','山西','内蒙古自治区','陕西','吉林','福建','贵州','广东','青海','西藏自治区','四川','宁夏回族自治区','海南']
list2=['石家庄市', '唐山市', '秦皇岛市', '邯郸市', '邢台市', '保定市', '张家口市', '承德市', '沧州市', '廊坊市', '衡水市', '太原市', '大同市', '阳泉市', '长治市', '晋城市', '朔州市', '晋中市', '运城市', '忻州市', '临汾市', '吕梁市', '呼和浩特市', '包头市', '乌海市', '赤峰市', '通辽市', '鄂尔多斯市', '呼伦贝尔市', '巴彦淖尔市', '乌兰察布市', '兴安盟', '锡林郭勒盟', '阿拉善盟', '沈阳市', '大连市', '鞍山市', '抚顺市', '本溪市', '丹东市', '锦州市', '营口市', '阜新市', '辽阳市', '盘锦市', '铁岭市', '朝阳市', '葫芦岛市', '长春市', '吉林市', '四平市', '辽源市', '通化市', '白山市', '松原市', '白城市', '延边朝鲜族自治州', '哈尔滨市', '齐齐哈尔市', '鸡西市', '鹤岗市', '双鸭山市', '大庆市', '伊春市', '佳木斯市', '七台河市', '牡丹江市', '黑河市', '绥化市', '大兴安岭地区', '南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市', '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市', '杭州市', '宁波市', '温州市', '嘉兴市', '湖州市', '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市', '合肥市', '芜湖市', '蚌埠市', '淮南市', '马鞍山市', '淮北市', '铜陵市', '安庆市', '黄山市', '滁州市', '阜阳市', '宿州市', '六安市', '亳州市', '池州市', '宣城市', '福州市', '厦门市', '莆田市', '三明市', '泉州市', '漳州市', '南平市', '龙岩市', '宁德市', '南昌市', '景德镇市', '萍乡市', '九江市', '新余市', '鹰潭市', '赣州市', '吉安市', '宜春市', '抚州市', '上饶市', '济南市', '青岛市', '淄博市', '枣庄市', '东营市', '烟台市', '潍坊市', '济宁市', '泰安市', '威海市', '日照市', '临沂市', '德州市', '聊城市', '滨州市', '菏泽市', '郑州市', '开封市', '洛阳市', '平顶山市', '安阳市', '鹤壁市', '新乡市', '焦作市', '濮阳市', '许昌市', '漯河市', '三门峡市', '南阳市', '商丘市', '信阳市', '周口市', '驻马店市', '武汉市', '黄石市', '十堰市', '宜昌市', '襄阳市', '鄂州市', '荆门市', '孝感市', '荆州市', '黄冈市', '咸宁市', '随州市', '恩施土家族苗族自治州', '长沙市', '株洲市', '湘潭市', '衡阳市', '邵阳市', '岳阳市', '常德市', '张家界市', '益阳市', '郴州市', '永州市', '怀化市', '娄底市', '湘西土家族苗族自治州', '广州市', '韶关市', '深圳市', '珠海市', '汕头市', '佛山市', '江门市', '湛江市', '茂名市', '肇庆市', '惠州市', '梅州市', '汕尾市', '河源市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市', '南宁市', '柳州市', '桂林市', '梧州市', '北海市', '防城港市', '钦州市', '贵港市', '玉林市', '百色市', '贺州市', '河池市', '来宾市', '崇左市', '海口市', '三亚市', '三沙市', '儋州市', '成都市', '自贡市', '攀枝花市', '泸州市', '德阳市', '绵阳市', '广元市', '遂宁市', '内江市', '乐山市', '南充市', '眉山市', '宜宾市', '广安市', '达州市', '雅安市', '巴中市', '资阳市', '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州', '贵阳市', '六盘水市', '遵义市', '安顺市', '毕节市', '铜仁市', '黔西南布依族苗族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州', '昆明市', '曲靖市', '玉溪市', '保山市', '昭通市', '丽江市', '普洱市', '临沧市', '楚雄彝族自治州', '红河哈尼族彝族自治州', '文山壮族苗族自治州', '西双版纳傣族自治州', '大理白族自治州', '德宏傣族景颇族自治州', '怒江傈僳族自治州', '迪庆藏族自治州', '拉萨市', '日喀则市', '昌都市', '林芝市', '山南市', '那曲市', '阿里地区', '西安市', '铜川市', '宝鸡市', '咸阳市', '渭南市', '延安市', '汉中市', '榆林市', '安康市', '商洛市', '兰州市', '嘉峪关市', '金昌市', '白银市', '天水市', '武威市', '张掖市', '平凉市', '酒泉市', '庆阳市', '定西市', '陇南市', '临夏回族自治州', '甘南藏族自治州', '西宁市', '海东市', '海北藏族自治州', '黄南藏族自治州', '海南藏族自治州', '果洛藏族自治州', '玉树藏族自治州', '海西蒙古族藏族自治州', '银川市', '石嘴山市', '吴忠市', '固原市', '中卫市', '乌鲁木齐市', '克拉玛依市', '吐鲁番市', '哈密市', '昌吉回族自治州', '博尔塔拉蒙古自治州', '巴音郭楞蒙古自治州', '阿克苏地区', '克孜勒苏柯尔克孜自治州', '喀什地区', '和田地区', '伊犁哈萨克自治州', '塔城地区', '阿勒泰地区']
str0=input('')
p=re.compile('(.+?)!')
num=p.findall(str0)[0]
num=int(num)

#tele匹配
p1=re.compile('\d+')
pp1=p1.findall(str0)
#print(pp1)
len0=len(pp1)
for i in range(0,len0):
    if int(pp1[i])>10000000000:
        tele=str(pp1[i])
#print(tele)
str0=delete_substr(str0,tele)#从字符串中删除子串

#name匹配
p2=re.compile('!(.+?),')
pp2=p2.findall(str0)[0]
name=pp2
#print(name)
p3=re.compile(',(.+?)\.')
str0=p3.findall(str0)[0]#去除前缀
str1=str0
#省份匹配
for i in range(0,len(list1)):
    if re.search(list1[i],str0)!=None:
        if i>3:   #对是否为直辖市的判断
            province=list1[i]+'省'
            flag[1]=1
        else:
            province=list1[i]
            city=list1[i]+'市'
            flag[1]=1
            flag[2]=1
        break
#print(province)
str0=delete_substr(str0,list1[i])#从字符串中删除子串
p = re.compile('(.+?)')
arr=p.findall(str0)
for i in range(0,5):
    if re.search('省',arr[i])!=None:
        str0=delete_substr(str0,'省')#从字符串中删除子串

#市级匹配
#对list2进行处理
list3=list2.copy()
len0=len(list2)
for i in range(0,len0):
    if re.search('市',list2[i])!=None:
        list2[i]=delete_substr(list2[i], '市')
for i in range(0,len0):
    if re.search(list2[i],str0)!=None:
        city = list3[i]
        flag[2] = 1
        break
#print(city)
str0=delete_substr(str0,list2[i])#从字符串中删除子串
arr=p.findall(str0)
for i in range(0,5):
    if re.search('市',arr[i])!=None:
        str0=delete_substr(str0,'市')#从字符串中删除子串
#将str0转换成数组
p = re.compile('(.+?)')
arr=p.findall(str0)
t=0
xian=''
for i in range(0,5):
    if re.search('市|县|区',arr[i])!=None:
        t=1
        flag[3] = 1
        break
if t==1 and flag[3]==1:
    for j in range(0,i+1):
        xian=xian+arr[j]
    #print(xian)
    str0=delete_substr(str0,xian)#从字符串中删除子串


p = re.compile('(.+?)')
arr=p.findall(str0)
#print(arr)
t=0
zhen=''
for i in range(0,5):
    if re.search('镇|乡',arr[i])!=None:
        t=1
        flag[4] = 1
        break
    if re.search('街', arr[i]) != None:
        if re.search('道', arr[i+1]) != None:
            t = 1
            i=i+1
            flag[4] = 1
            break
if t==1 and flag[4]==1:
    for j in range(0,i+1):
        zhen=zhen+arr[j]
    #print(zhen)
    str0=delete_substr(str0,zhen)#从字符串中删除子串

if num==1:
    lu=str0
    #print(cun)
else:
    p = re.compile('(.+?)')
    arr = p.findall(str0)
    # print(arr)
    t = 0
    lu = ''
    len0=len(arr)
    for i in range(0, len0):
        if re.search('路|街|巷', arr[i]) != None:
            t = 1
            flag[5] = 1
            break
        if re.search('大', arr[i]) != None:
            if re.search('道', arr[i + 1]) != None:
                t = 1
                i = i + 1
                flag[5]=1
                break
    if t == 1 and flag[5]==1:
        for j in range(0, i + 1):
            lu = lu + arr[j]
        #print(lu)
        str0 = delete_substr(str0, lu)  # 从字符串中删除子串

    p = re.compile('(.+?)')
    arr = p.findall(str0)
    # print(arr)
    t = 0
    hao = ''
    fang=''
    len0 = len(arr)
    for i in range(0, len0):
        if re.search('号', arr[i]) != None:
            if len0>i+1:
                if re.search('楼',arr[i+1])!=None:
                    t = 1
                    i=i+1
                    flag[7]=1
                    break
        if re.search('号', arr[i]) != None:
            t = 1
            flag[6]=1
            break
    if t == 1 and flag[6]==1:
        for j in range(0, i + 1):
            hao = hao + arr[j]
        #print(hao)
        str0 = delete_substr(str0, hao)  # 从字符串中删除子串
    if t==1 and flag[7]==1:
        for j in range(0, i + 1):
            fang = fang + arr[j]
        #print(fang)
        str0 = delete_substr(str0, fang)  # 从字符串中删除子串
    #判断是否有第七级地址
    len0=len(str0)
    if len0!=0:
        fang=str0
        flag[7]=1
        #print(fang)
if num==3:
    url = 'https://restapi.amap.com/v3/geocode/geo?address='+str1+'&output=XML&key=46b59533e5942f662c8201f2df21a7d9'
    res = requests.get(url).text
    #print(res)
    res=str(res)
    p=re.compile('<location>(.+?)</location>')
    location=p.findall(res)[0]
    #print(location)
    #地址反编码
    url = 'https://restapi.amap.com/v3/geocode/regeo?output=xml&location='+location+'&key=46b59533e5942f662c8201f2df21a7d9&radius=50&extensions=base'
    res = requests.get(url).text
    #print(res)
    p1=re.compile('<province>(.+?)</province>')
    province=p1.findall(res)[0]
    if province=='北京市'or province=='天津市'or province=='上海市'or province=='重庆市':
        city=province
        province=delete_substr(province,'市')#从字符串中删除子串
    else:
        p2 = re.compile('<city>(.+?)</city>')
        city = p2.findall(res)[0]
    p3 = re.compile('<district>(.+?)</district>')
    xian = p3.findall(res)[0]
    p3 = re.compile('<township>(.+?)</township>')
    zhen = p3.findall(res)[0]
    for i in range(1,5):
        flag[i] = 1



if num==1:
    list = ['0', province, city, xian, zhen, lu]
    for i in range(1, 6):
        if flag[i] == 0:
            list[i] = ''

    imformation = {
        "level": num,
        "姓名": name,
        "手机": tele,
        "地址": [
            province,
            city,
            xian,
            zhen,
            lu,
        ]
    }
else:
    list = ['0', province, city, xian, zhen, lu, hao, fang]
    for i in range(1, 8):
        if flag[i] == 0:
            list[i] = ''

    imformation={
        "level": num,
        "姓名": name,
        "手机": tele,
        "地址": [
            province,
            city,
            xian,
            zhen,
            lu,
            hao,
            fang
        ]
    }
data = json.dumps(imformation, ensure_ascii=False)
print(data)













