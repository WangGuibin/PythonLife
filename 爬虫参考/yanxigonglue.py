from bs4 import BeautifulSoup
import pymongo
import re
from selenium import webdriver
import time

import jieba
from  pyecharts import WordCloud
from collections import Counter



# 爬取延禧攻略 500条短评 用于分析这部电视剧
mg = pymongo.MongoClient('localhost',27017)
client = mg['yxgl']
commentsDB = client['comments']

def getInfo():
        url = 'https://movie.douban.com/subject/26999852/comments?status=P'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        wb = webdriver.Chrome()
        wb.get(url)
        html = wb.page_source
        # print(html)
        parseHTML(html)
        page = 20
        while True:
                wb.implicitly_wait(10)
                button = wb.find_element_by_class_name('next')
                button.click()
                time.sleep(2)
                page += 20
                print('\n'+'已爬取评论数据:  '+str(page)+'  条',end='\n')
                parseHTML(wb.page_source)
                if page == 500:
                         break


def parseHTML(html):
        bs = BeautifulSoup(html,"lxml")
        comments = bs.find_all('div',attrs={"class":"comment-item"})
        for div in comments:
                info_span = div.h3.find_all('span',attrs={'class':"comment-info"})
                nickname = info_span[0].a.get_text(strip=True)
                headimg = div.a.img.get('src')
                userlink = div.a.get('href')
                content = div.p.span.get_text(strip=True)
                scoretext =  info_span[0].span.next_sibling.next_sibling['class'][0]
                score = getScore(scoretext)
                time = info_span[0].select('span.comment-time')[0]['title']
                data = {
                    'nickname': nickname,
                    'headimage': headimg,
                    'userlink' : userlink,
                    'content': content,
                    'score': score,
                    'time': time,
                }
                # 插入数据库
                commentsDB.insert_one(data)

# 处理评分
def getScore(scoretext):
        score = re.findall(r'\d',scoretext)
        if len(score):
            return str(float(score[0]))
        else:
            return '0.0'

if __name__ == '__main__':
     # getInfo()
     for item in commentsDB.find():
         wordlist_after_jieba = jieba.cut(item['content'], cut_all=True)
         wl_space_split = " ".join(wordlist_after_jieba)
         wordlist = wl_space_split.split(" ", 10000)
         counts = Counter(wordlist)
         times = counts.most_common(100)
         array = []
         values = []
         for list in times:
             array.append(list[0])
             values.append(list[1])

         wordcloud = WordCloud(width=1080, height=1080)
         wordcloud.add("", array, values, word_size_range=[30, 200])
         wordcloud.render("doubancomments.html")



