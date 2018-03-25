from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://dantri.com.vn'
# 1. Download webpage
#1.1 Open connection
#conn = urlopen(url)
#1.2 Read
#data = conn.read()
#1.3 Decode
#html_content = data.decode('utf8')
html_content =urlopen(url).read()

#save html_content to file
#html_file = open("dantri.html", "wb")
#html_file.write(html_content)
#html_file.close()

#2. Extract ROI (Region of Interest)
soup = BeautifulSoup(html_content, 'html.parser') #xml, xhtml,html, htm
#ul = soup.find('ul', class='ul1 ulnew')
ul = soup.find('ul', 'ul1 ulnew')

#3.Extract info
li_list = ul.find_all('li') #[]
datas=[]

for li in li_list:
    a = li.h4.a
    #print(a.string)
    # print(url + a["href"])
    # print('*' * 30)
    datas.append({
    "title": a.string,
    "link" : url + a["href"]})
pyexcel.save_as(records = datas, dest_file_name ="dan_tri.xls")`
