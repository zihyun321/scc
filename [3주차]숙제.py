import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
genieChart = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

count = 0
for genie in genieChart:
    count+= 1
    title = genie.select_one('td.info > a.title')
    rank = genie.select_one('td.number')
    singer = genie.select_one('td.info > a.artist.ellipsis')
    print(count, title.text.strip(), singer.text)
   
