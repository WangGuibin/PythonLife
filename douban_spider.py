import scrapy
import re
import json
from bs4 import  BeautifulSoup
import time
import csv

class  DoubanDianYing(scrapy.Spider):
            name = 'douban'
            allow_domains = ['movie.douban.com']
            datalist = []
            def start_requests(self):

                    headers = {
                        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                    }


                    for page in range(0,251,25):
                        url = 'https://movie.douban.com/top250?start=%d&filter=' % page
                        yield scrapy.Request(url,headers=headers)

            def parse(self, response):

                with open('dataSource.json', 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    out = open('douban_csv.csv', 'a', newline='')
                    csv_writer = csv.writer(out, dialect='excel')
                    csv_writer.writerow(['影片名字','封面图片', '电影地址','演员以及类型','影片宣传语','热度','豆瓣评分'])
                    for dic  in  content:
                         csv_writer.writerow([dic['title'], dic['img'],  dic['link'], dic['actors'], dic['desc'], dic['hot'], dic['rating']])

                    # html = response.text
                    # bs = BeautifulSoup(html)
                    # 练习xpath
                    # titles = response.xpath('//div/a/span[1]/text()').extract()
                    # imgs = response.xpath('//div[@class="pic"]/a/img/@src').extract()
                    # links = response.xpath('//div[@class="hd"]/a/@href').extract()
                    # actors = response.xpath('//div[@class="bd"]/p/text()').extract()
                    # descs = response.xpath('//span[@class="inq"]/text()').extract()
                    # rating = response.xpath('//div[@class="star"]/span[@class="rating_num"]/text()').extract()
                    # hots = response.xpath('//div[@class="star"]/span[4]/text()').extract()
                    #
                    # if '6.0' in titles: #豆瓣派来的逗我们玩的 脏数据大概就是说的它!
                    #         titles.remove('6.0')
                    #
                    # for index in range(len(titles)):
                    #          dic = {}
                    #          dic['title'] = titles[index]
                    #          dic['img'] = imgs[index]
                    #          dic['actors'] = str(actors[index]).strip().replace("\n","")
                    #          dic['rating'] = rating[index]
                    #          dic['hot'] = hots[index]
                    #          dic['link'] = links[index]
                    #          dic['desc'] = descs[index]
                    #          self.datalist.append(dic)
                    # if len(self.datalist) == 250:
                    #     with open('dataSource.json', 'a+') as f:
                    #         json.dump(self.datalist, f, ensure_ascii=False, indent=4)




