import requests
from bs4 import BeautifulSoup
with open(r'C:\Users\JF\Desktop\demo.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
    trs = soup.find_all('tr')
    #print(trs)
    #print('*'*50)
    for tr in trs:
        print(tr.text)
        ui = []
        for td in tr:
            ui.append(td.string)
        print(ui)
    # print(soup)