import requests
from bs4 import BeautifulSoup
import os
URL = 'https://v.taobao.com/'
url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B1%A6%C2%ED%C3%D4%C4%E3%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
wb_data = requests.get(url, headers=headers)
#print(wb_data)
soup = BeautifulSoup(wb_data.content, 'lxml')
#print(soup)
def Saving(url):
    root = r"C:\Users\JF\Desktop\pictures\\"
    path = root +url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            print(url)
            r = requests.get(url)
            print(r)
            with open(path, 'wb') as f:

                f.write(r.content)
                #f = r.replace(r, "1.jpg")
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬去失败")

PictureList = soup.find_all('img')
print(PictureList)

pictureList = soup.select('.imglist clearfix pageNum1')

print(pictureList)
