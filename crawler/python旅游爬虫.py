import requests
from bs4 import BeautifulSoup
url = requests.get('https://go.hao123.com')
soup = BeautifulSoup(url.content, "lxml")
images = soup.select('body > div.content-outer-wrapper > div > div > div > div > div > div > div > a > img')
prices  = soup.select('body > div.content-outer-wrapper > div > div > div.tejia-menpiao > div.container > div > div > div.price > a > div.new')
names = soup.select('body > div.content-outer-wrapper > div > div > div.tejia-menpiao > div.container > div > div > div.pic > a > div')

'''
#循环遍历列表提取文本
for i in names:
    print(i.get_text())
'''

data = {}
for name, price, image in zip(names, prices, images):
    data = {
        'name': name.get_text(),
        'price': price.get_text(),
        'img': image.get('src')
    }
    #print(name, price, image, sep='\n')
    print(data)     #遍历列表字典存储

