import re
import requests
from lxml import etree
from onexima import Xima


def get_id():
    """获取排行榜每一本书的信息"""
    main_url = "https://www.ximalaya.com/shangye/top/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    r = requests.get(main_url, headers=headers)
    # 获取到当前页面的xml数据
    html = etree.HTML(r.content.decode())
    # 得到每一本书的位置的信息
    div_list = html.xpath("//div[contains(@class,'e-2997888007 rrc-album-item')]")
    all_lsit = []  # 待会把每一本书的音频以字典形式放进列表当中
    for div in div_list:
        author = {}  # 创建一个列表, 我们要获取书的id和书的名字, 并且一一对应
        r = div.xpath("./a/@href")[0]  # 获取到当前书的id所在信息, 数据为: /renwen/4859823/
        print(r)
        # 所以得通过正则把正确的id取出来, id是为了传入正确的id, 得到正确的json数据
        author['id'] = re.search(r'\/.*?\/(.*)\/', r).group(1)
        author['book_name'] = div.xpath("./a/div[3]/div[1]/span/text()")[0]
        # 向列表中传入每一个音频的信息
        all_lsit.append(author)
    print(all_lsit)
    return all_lsit


# 调用函数得到所有每一本书的信息, 是一个列表类型
all_lsit = get_id()
for i in all_lsit:
    # 遍历列表, 把每本书对应的id和对应的书名传到类里面去
    x = Xima(i['id'], i['book_name'])
    x.run()