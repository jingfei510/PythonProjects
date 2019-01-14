import requests
from bs4 import BeautifulSoup
import pymysql

list_url = []#存储生成的从第一页到第5页的网页连接
list_info_experience = []#存储求职要求经验
list_info_education = []#存储求职要求学历
list_info_money = []#存储求职要求薪资区间
list_name = []#存储求职公司名称
db = pymysql.connect("localhost", "root", "admin", "Myinterview")
cursor = db.cursor()
def Create_Table(cursor):
    cursor.execute("drop table if exists employee;")  # 如果存在fin表时候先删除
    sql = '''create table employee
    	(
    		id int unsigned not null auto_increment primary key,
    		公司名称 char(100) not null,
    		工作经验 char(50) not null,
    		学历要求 char(50) not null,
    		薪资范围 char(50) null default "-"
    	);'''
    cursor.execute(sql)
def Mysql_Content(cursor,JobName, JobExperience, JobEducation, JobMoney):
    print(JobName, JobExperience, JobEducation, JobMoney)
    sql = 'INSERT INTO employee(公司名称,工作经验,学历要求,薪资范围) VALUES (\"' + JobName + '\",\"' + JobExperience + '\",\"' + JobEducation + '\",\"' + JobMoney + '\")'
    #print(sql)
    cursor.execute(sql)
    db.commit()



#网页有很多页，这里把每一页的连接存储在list_url中
def Make_Url():
    for i in range(1, 4):
        global URL
        URL = 'https://www.jobui.com/jobs?jobKw=python&cityKw=%E5%8C%97%E4%BA%AC&n={}'.format(i)
        list_url.append(URL)
        #print(list_url)

#获取给定URL页的html信息
def Get_Wb(URL):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    wb_data = requests.get(URL, headers=headers)
    global soup
    soup = BeautifulSoup(wb_data.content, 'lxml')
    #print(soup)

#获取每家公司的名称
def Get_Name():
    names = soup.select('#search-match > div.header-2014 > div.astruct.cfix > div.aleft > div.jk-box.jk-matter.j-jobInfo > ul > li > div > div > div.cfix > a')
    for i in names:
        list_name.append(i.get_text().strip())

#获取每家公司的经验要求，学历要求，薪资区间
def Get_Msg():
    for i in range(1, 16):
        xxx = 'div.header-2014 > div.astruct.cfix > div.aleft > div.jk-box.jk-matter.j-jobInfo > ul > li:nth-of-type({}) > div > div > div:nth-of-type(4)'.format(i)
        #print(xxx)
        msg = soup.select(xxx)
        #print(msg)
        for y in msg:
            info = y.get_text()
            info = info.split('|')#将经验要求，学历要求，薪资区间3个信息，以|分割开，存储为列表格式
            list_info_experience.append(info[0].strip())
            list_info_education.append(info[1].strip())
            list_info_money.append(info[2].strip())
#最后以字典形式输出
def DictOutput():
    for JobName, JobExperience, JobEducation, JobMoney in zip(list_name, list_info_experience, list_info_education, list_info_money):

        AllData = {'公司名称': JobName,
                   '工作经验': JobExperience,
                   '学历要求': JobEducation,
                   '薪资范围': JobMoney
        }
        print(AllData)
        Mysql_Content(cursor, JobName, JobExperience, JobEducation, JobMoney)
print('北京市招聘信息')
Make_Url()
#先输出3页
for i in range(0, 3):
    Get_Wb(list_url[i])
    #print(list_url[i])#所爬取的网页链接
    Get_Msg()
    Get_Name()
#Create_Table(cursor)
DictOutput()
db.close()


