import requests
from bs4 import BeautifulSoup

def get_info(URL):
    #URL = 'https://bj.58.com/pingbandiannao/35923077687887x.shtml?psid=157596847202024134799949907&entinfo=35923077687887_p&slot=-1&iuType=p_1&PGTID=0d305a36-0000-19ea-0c77-0ae8025ace4f&ClickID=2'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
    try:
        wb_data = requests.get(URL,headers=headers)
        soup = BeautifulSoup(wb_data.content, 'lxml')
        #print(soup)
        NameList = soup.select('h1.detail-title__name')
        ProductName = NameList[0].text.strip()
        PriceList = soup.select('span.infocard__container__item__main__text--price')
        ProductPrice = PriceList[0].text.strip()

        AreaList = soup.select('div.infocard__container__item__main > a')
        ProductArea = AreaList[0].text.strip()+'-'+AreaList[1].text.strip()
        SellerNameList = soup.select('div.infocard__container__item__main > a')
        SellerName = SellerNameList[2].text
        CatalogueList = soup.select('div.nav > a')
        Catalogue = CatalogueList[-1].text

        data_dict = {
            '产品类别': Catalogue,
            '产品名称': ProductName,
            '产品价格': ProductPrice,
            '产品区域': ProductArea,
            '卖家姓名': SellerName
        }
        print(data_dict)
    except:
        print("内容已被修改")

def get_all_info():
    url = 'https://bj.58.com/pingbandiannao/?PGTID=0d409654-017a-3436-09be-f01fa1e2217f&ClickID=13'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    GetLink = soup.select('td.t > a')
    #print(GetLink)
    for i in GetLink:
        link = i.get('href')  #得到href链接
        if 'pingbandiannao' in link:
            get_info(link)

get_all_info()
