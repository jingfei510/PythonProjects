import requests
from bs4 import BeautifulSoup
#headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
url = 'https://blog.csdn.net/qq_43371004'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
name = soup.select('#mainBox > main > div.article-list > div > h4 > a')
requests_num = soup.select('#mainBox > main > div.article-list > div > div.info-box.d-flex.align-content-center > p > span')
data = soup.select('#mainBox > main > div.article-list > div > div.info-box.d-flex.align-content-center > p > span')
print(data)
print(requests_num)
print(name)
for i, y in zip(name, requests_num):
    data = {
        'name': i.get_text(),
        '访问': y.get_text()

    }
    print(data)