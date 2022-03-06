# coding:utf-8

import json 
from wsgiref.simple_server import make_server
 
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'application/json')])
    # environ是当前请求的所有数据，包括Header和URL，body

    request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0))) 
    request_body = json.loads(request_body)
    
    # 这里拿到body的参数进行CRUD
    # name = request_body["name"] 
    # no = request_body["no"]

    # 回调组装数据 
    # dic = {'name': name, 'no': no}
    # return [json.dumps(dic)]
    # 原路返回 body数据 
    return [json.dumps(request_body)]
 
if __name__ == "__main__":
    port = 8080
    httpd = make_server("0.0.0.0", port, application)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()