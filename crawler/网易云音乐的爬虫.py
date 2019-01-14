import requests
from bs4 import BeautifulSoup
import  re
url = "https://music.163.com/radio/my/#/plist"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
           'Cookie': '_ntes_nnid = 8a9e744d2a359ead46f2341b30e050f4, 1540100955503;_ntes_nuid = 8a9e744d2a359ead46f2341b30e050f4;__f_ = 1540100956242;mail_psc_fingerprint = 45be3b48424f9531e3ae6fab9f3e335e;_iuqxldmzr_ = 32;WM_TID = lQqT % 2Fl9Sbm1BQFVFEUZ9PaEgDm26fSGo;__remember_me = true;P_INFO = jingfei_510 @ 163.com | 1543237840 | 0 | other | 00 & 99 | sxi & 1540890219 & other  #sxi&610100#10#0#0|&0||jingfei_510@163.com; NNSSPID=95e85b0734af4472affb91d46a049512; JSESSIONID-WYYY=bIqkYO6iikD2k5S25BvzvjnM6YRYd6qkjv7wMQPKg8%2F4lT2sjABcdUubyHjKQgcHEyMSjPwijzQfeIUmnVkFQnh9pi%5C%2FHQrPicG%2FyirjC9CwWP1g%5CGt%2FK4TCiuF1yr0RgQts8YQ4MIMGTgD5VDBQ%5CsmJKDUz3qU%2Fjo5iTjSEXhVsF2wB%3A1543315618073; __utma=94650624.185360301.1542978940.1542978940.1543313818.2; __utmc=94650624; __utmz=94650624.1543313818.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=sUBmvZeCSvTFE6%2BbVje7PTng8PyyI7fbr3VbGa%2BNS0U5vqhnbuodqXi4HCFuGgy7R7nErl8MmqqMUMgv9I1qU3ntGZlEg0YxsvAbuZ9J6xsTLkSh2aInbrwSFUi5YDkVa0g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea6ce538eb2f886e64a96a88ab3c85e969a8eaff36eaebcb89bce5f82968a83d72af0fea7c3b92ab18b8e8ef552a79d9d97d74e87eae583d562a7e9a0b5ed6dfc90b79acc3da6bebed4d56a85bfe5afd23c97ebba92eb66a2aba185f454abec88a4c57f85b9b7d8d13dae9bbe8dbb47afafbfaed847a5aaf7aab47b97eda295c652b09ba9d1dc74b1aa8f83f852fb96fa99f26090b59d89b16b8bb2ae93f659868ba7d6dc50a98aafd1e637e2a3; MUSIC_U=5ef4947d6d52803b8d183b424cb617567a829e341610105ec185e846082bdc36681056601de131dfcb298435d8d68010a70b41177f9edcea; __csrf=c4c79b3b627430e8217d8166b61e5116; __utmb=94650624.3.10.1543313818'}
html = requests.get(url,headers=headers)
soup = BeautifulSoup(html.content , 'lxml')
x = re.findall("<li> \w+ </li>", soup)
#print(soup)
# x = soup.select('div.m-programs')
print(x)

