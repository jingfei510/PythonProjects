import requests
from bs4 import BeautifulSoup
import os
url = 'https://baike.baidu.com/item/阿尔伯特·爱因斯坦/127535?fromtitle=%E7%88%B1%E5%9B%A0%E6%96%AF%E5%9D%A6&fromid=122624'
#url='http://baike.baidu.com/subview/6593456/6713831.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
wb_data = requests.get(url, headers=headers)
#print(wb_data)
soup = BeautifulSoup(wb_data.content, 'lxml')
#print(soup)
def Saving(url,name):
    #root = r"C:\Users\JF\Desktop\pictures\\"
    root = r'C:\pictures\\'
    path = root + name + '.jpg'
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
def GetPicture():
    PictureList = soup.select('div.summary-pic > a > img')
    Picture =PictureList[0].get('src')
    NameList = soup.select('dd.lemmaWgt-lemmaTitle-title > h1')
    Name = NameList[0].text
    LinkList = soup.select('a.link-inner')
    #print(Name)
    #print(Picture)
    Saving(Picture, Name)
GetPicture()
