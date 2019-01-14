

import requests
from bs4 import BeautifulSoup
URL = 'https://www.csdn.net/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
           'Cookie': 'ADHOC_MEMBERSHIP_CLIENT_ID1.0 = 850d4feb - 21e9 - d2e9 - ab71 - e2a060bb394f;smidV2 = 201810202253276fa25a97a3c4aad48c5a8349b4460c2300c08fb583fbae510;\Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac = 1788 * 1 * PC_VC;ARK_ID = JScf979b8faa62c66f8123d000211cd0afcf97;uuid_tt_dd = 10_28867322940 - 1540390300850 - 687862;UN = qq_43371004;           _ga = GA1.2.1122955675           .1540532037;_gid = GA1.2.1095391965.1541319272;dc_session_id = 10_1541332937433.317673;Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac = 1541297457, 1541311127, 1541322714, 1541332937;TY_SESSION_ID = 8ce33abf - 0550 - 40df - bdb9 - f07ae4c26c51;Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac = 1541342592'}
wb_data = requests.get(URL, headers=headers)
soup = BeautifulSoup(wb_data.content, 'lxml')
#print(soup)

namelist = soup.select('div.title > h2 > a')
print(namelist[0].text.strip())
#.text作用是得到文本，.strip()作用是去掉字符串两边的空格及换行