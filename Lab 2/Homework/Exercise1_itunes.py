from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://www.apple.com/itunes/charts/songs/'

# 1. Download webpage
html_content =urlopen(url).read().decode('utf-8')

# #2. Extract ROI
soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section', 'section chart-grid')

#3.Extract info
li_list = section.find_all('li')
datas=[]

for li in li_list:
    names = li.h3.a
    artists = li.h4.a
    datas.append({
        "names": names.string,
        "artists" : artists.string
        })
pyexcel.save_as(records = datas, dest_file_name ="itunes.xls")

#4.Download
from youtube_dl import YoutubeDL

# Search and then download the first video
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
for k in datas:
    song = k['names'] + ' '+ k['artists']
    dl.download(song)
