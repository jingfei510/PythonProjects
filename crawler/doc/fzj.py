import requests
import pandas
from bs4 import BeautifulSoup

def openfile(file):
    f=open(r'F:\PythonText\crawler\doc\fzj.csv','a')
    f.write(file)
    f.close()

def detail_page(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html , 'lxml')
    jod_name = soup.select('.new_job_name')[0].string
    #获得该网站中class属性为new_job_name的内容，其中的[0]是得到第一个
    job_position=soup.select('.job_position')[0].string 
    com_position=soup.select('.com_position')[0].string
    job_detail=soup.select('.job_detail')[1].string
    x=('公司项目:{} 地点:{} 公司地址：{}'.format(jod_name,job_position,com_position))
    #df = pandas.DataFrame(x)
    #print(df.head(10))
    openfile(x)
for page in range (2,10):
    req = requests.get('https://www.shixiseng.com/interns/c-None_?k=IT%E4%BA%92%E8%81%94%E7%BD%91&p={}'.format(page)) 
    html=req.text
    soup = BeautifulSoup(html,'lxml')
    for job in soup.select('a.name'):
        url = job.get('href')
        detail_page('https://www.shixiseng.com'+ url)
        #转入到该网址


