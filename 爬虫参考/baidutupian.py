# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 导入URLLIB库的编码方法
from urllib.parse import urlencode
# 请求库
import requests
# 用于处理Json格式的文件
import json


# 函数作用,拼接完整的URL
def page_url_cont():
    # 可以传入2个变量,一个用于搜索关键字,一个用于翻页
    # queryWord   word    对应关键字
    # pn 对应翻页
    data = {'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': '美女',
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid':'',
            'st': '-1',
            'z': '',
            'ic': 0,
            'word': '美女',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': 0,
            'rn': 30,
            'gsm': 96
            }
    # 拼接url
    url = 'http://image.baidu.com/search/index?' + urlencode(data)

    # 返回拼接好的url
    return url


# 获取图片链接返回一个列表
def get_images_url(response):
    # 用jsondata保存 用json.loads的方法处理返回回来的类似字典的格式
    jsondata = json.loads(response.text)
    # 创建一个空的列表,用于处理提取出来的Url
    image_url = []
    # 检查字典里是否包含data这个关键字
    if 'data' in jsondata.keys():
        # 从字典里面提取出data这个键的值
        for items in jsondata.get('data'):
            # 从items这个自动中提取thumbURL的值,返回一个url
            url = items.get('thumbURL')
            # 空列表添加提取出来的url
            image_url.append(url)
    # 添加完成后统一返回
    return image_url

# 下载用的函数
def downimage(image_url):
    # 从我们传入的url列表重依次取出url
    for url in image_url:
        # 异常处理
        try:
            # 请求我们图片地址得到返回
            response = requests.get(url)
            # 判断响应码
            if response.status_code == 200:
                # 用切片的方法给图片命名
                name = url.split(',')[-1].split('&')[0]
                # 以字节的方式读取读取数据
                image = response.content
                # 创建一个空白的文件,以二进制的方式写入数据
                # 给创建出来的这个文件取个别名叫f
                with open('./images/%s.jpg' % name, 'wb') as f:
                    # 写入我们的2进制数据
                    f.write(image)
        except:
            print('当前请求出错')


def main():
    url = page_url_cont()
    # 获得的响应 被赋值  GEI请求赋值
    response = requests.get(url)
    # 用json格式读取返回的文本数据
    # print(jsondata.keys())
    image_url = get_images_url(response)
    # print(image_url)
    # 传入我们的下载器
    downimage(image_url)


if __name__ == '__main__':
    main()