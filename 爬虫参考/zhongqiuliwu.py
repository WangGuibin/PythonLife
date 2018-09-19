# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
html = requests.get('https://search.jd.com/Search?keyword=%E4%B8%AD%E7%A7%8B%E7%A4%BC%E7%89%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%B8%AD%E7%A7%8B%E7%A4%BC%E7%89%A9&psort=3&click=0',headers=headers).text

bs = BeautifulSoup(html,'lxml')
lists = bs.find_all('em')
texts = []
for em in lists:
        text = em.get_text()
        print(text)
         # texts.append(text)

