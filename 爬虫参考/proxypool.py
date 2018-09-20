import requests
from bs4 import BeautifulSoup
import time

def getHtml(page):
        url = 'https://www.kuaidaili.com/free/inha/%d' % page
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        data = requests.get(url,headers=headers).text
        return  data

# <td data-title="IP">117.90.137.190</td>
# <td data-title="PORT">9000</td>
def dealWithIPOrPort(html):
        ipList = []
        bs = BeautifulSoup(html,features='lxml')
        ips = bs.find_all('td',attrs={'data-title':'IP'})
        ports = bs.find_all('td', attrs={'data-title': 'PORT'})
        for ip_td,port_td in list(zip(ips,ports)):
                ip_text = ip_td.get_text()
                port_text = port_td.get_text()
                ip = '{0}:{1}'.format(ip_text,port_text)
                ipList.append(ip)
        return ipList

def saveIpFiles(list):
        for ip in list:
             with open('ip.txt','a+',encoding='utf-8') as f:
                    f.write(ip + '\n')


def getAllData():
        for page in range(1,2472):
                 html = getHtml(page)
                 iplist = dealWithIPOrPort(html)
                 saveIpFiles(iplist)
                 print('第%d页数据已爬完\n' % page)
                 print(iplist)
                 time.sleep(1)




if __name__ == '__main__':
        getAllData()