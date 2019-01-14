import requests
from bs4 import BeautifulSoup
URL1 = 'http://bj.xiaozhu.com/fangzi/37609773603.html'
URL = 'http://bj.xiaozhu.com/fangzi/40280014403.html'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
wb_data = requests.get(URL, headers=headers)
soup = BeautifulSoup(wb_data.content, 'lxml')
#print(soup)
HouseName = soup.select('div > div > div > h4 > em')
HouseAdress = soup.select('div.wrap > div > div > p > span')
HousePrice = soup.select('#pricePart > div.day_l > span')
HousePicture = soup.select('#curBigImage')
WannerPicture = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
WannerName = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
WannerSex = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
if WannerSex[0]['class'][0] == 'member_ico':
    WannerSex = '男'
elif WannerSex[0]['class'][0] == 'member_ico1':
    WannerSex = '女'
else:
    WannerSex = '性别不明'
'''body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span   
删掉前面的body >  如果爬出来的数据是空值，空列表，索引超过范围等这种错误，则需要删除前面的一些，或者删除每个点后面的东西
例如上面这条最终
可以是div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span
也可以是div.wrap > div > div > p > span'''

'''以下用了两种字符串输出方式：拼接“+”，和字符串输出“%s”
用了3种爬虫输出文本方式，get_text(),text和string'''
print('名称：%s' %HouseName[0].string)
print('地址：%s' %HouseAdress[0].get_text().strip())
print('价格：'+HousePrice[0].text)
print('房子图片：'+HousePicture[0]['src'])
print('主人照片：'+WannerPicture[0]['src'])
print('主人姓名：'+WannerName[0].text)
print('主人性别：'+WannerSex)
cates = soup.find_all('div','pho_info')
print(cates)