#2018年09月28日 09:57 习近平一锤定音 关于民企的无谓争论可休矣
import requests
from bs4 import BeautifulSoup
def openfile(file):
    f=open(r'F:\PythonText\crawler\doc\doc1.text','w')
    f.write(file)
    f.close()
newurl="https://news.sina.com.cn/gov/xlxw/2018-09-28/doc-ifxeuwwr9032306.shtml"
res=requests.get(newurl)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
title = soup.select('.main-title')[0].text
time=soup.select('.date')[0].contents[0]
files='时间：\n'+time+'\n内容：\n'+title
print(files)
openfile(files)
document=soup.select('.num')
print(document)

