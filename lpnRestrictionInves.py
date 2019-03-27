# !/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request, json
from urllib.parse import urlencode

#这个类封装了“查询尾号”API所需的所有内容
class API_illegality(object):
    def __init__(self):
        #读取文件中的密钥信息
        with open("./key_data.json",'r')as load_f:
            self.result=json.load(load_f)
        self.Params = {"key": self.result['key'], "city": "beijing", "type": "1"}

    #测试函数，直接读取保存好的json文件
    #type(取值范围：1~7)意义：1 今天  2 明天  3 后天...
    def query2(self, city, type):
        with open("./data_R.json",'r')as load_f:
            self.res=json.load(load_f)
        self.queryResult=self.res["result"]
        #print(self.queryResult)

    #正式函数，联网调用api
    #query（城市，相对星期数），用来访问API以获取该城市某一天的限号情况
    def query(self, city, type):
        self.Params["city"]=city
        self.Params["type"]=type
        self.params = urlencode(self.Params)
        self.url = 'http://v.juhe.cn/xianxing/index?%s' % self.params

        self.wp = urllib.request.urlopen(self.url)
        self.content = self.wp.read()
        self.res = json.loads(self.content)

        #测试代码，用户生成本地json文件，节约API访问限数
        '''jsonData = json.dumps(self.res)
        fileObject = open('data_R.json', 'w')
        fileObject.write(jsonData)
        fileObject.close()
        '''

        #分析json中的关键信息是否合法，无论是否合法，都把信息存到queryResult变量中
        if self.res:
            self.error_code = self.res['error_code']
            if self.error_code == 0:
                self.queryResult=self.res['result']
            else:
                self.queryResult =False
        else:
            self.queryResult =False
        # 若queryResult正确地存储了信息，就把限行尾号存到weihaos变量中
        if self.queryResult:
            if self.queryResult['isxianxing'] == 1:
                self.weihaos = self.queryResult['xxweihao']
            else:
                self.weihaos = ''
        else:
            print("查询失败")
