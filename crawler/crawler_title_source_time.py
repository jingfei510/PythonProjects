#2018-09-28 07:49 新浪陕西 陕西省采取15条措施监管疫苗 严禁接种门诊私购

def openfile(file):
    f=open(r'F:\PythonText\crawler\doc\crawler_title_source.text','w')
    f.write(file)
    f.close()
#使用错误
     
import requests
from bs4 import BeautifulSoup

newurl="http://sx.sina.com.cn/news/b/2018-09-28/detail-ihkmwytp5948972.shtml"
res=requests.get(newurl)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
for news in soup.select('.article-header.clearfix'):
    #print(news)
    new=(news.select('h1')[0].text.strip())
source= soup.select('#art_source')[0].text.strip()
time= soup.select('.source-time span')[0].text.strip()
title_top=(time,source,new)


texto='\n'.join(['       '+i.text.strip() for i in soup.select('.article-body.main-body p')])
alltext=time+source+new+texto
print(alltext)#打印表头和正文
