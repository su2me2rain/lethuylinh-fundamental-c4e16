from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
# 1. Download webpage
html_content =urlopen(url).read()

#2. Extract ROI (Region of Interest)
soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div', style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")

# 3.Extract info
tr_list = div.find_all('tr',['r_item', 'r_item_a'])
datas=[]

for tr in tr_list:
    data = OrderedDict({
        'Items':'',
        'Quý 4-2016':'',
        'Quý 1-2017':'',
        'Quý 2-2017':'',
        'Quý 3-2017':'',
        })
    td_list = tr.find_all('td','b_r_c')
    i = 0
    for key in data:
        while i < len(td_list)-1:
            data[key] = td_list[i].string
            break
        i += 1
    datas.append(data)
pyexcel.save_as(records = datas, dest_file_name= 'cafef.xls')
