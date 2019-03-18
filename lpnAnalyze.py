# -*- coding: utf-8 -*-
import urllib.request,urllib.parse
import base64

class API_lpn(object):
    def __init__(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        self.host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=oPCATAa46bL4MIvtkkqLLskU&client_secret=TSCb3Nkro5CC7f0mGBjIkimFe2BkxFmv'
        self.request = urllib.request.Request(self.host)
        self.request.add_header('Content-Type', 'application/json; charset=UTF-8')


    def connect(self):
        self.response = urllib.request.urlopen(self.request)
        self.content = self.response.read()
        if (self.content):
            print(type(self.content))
        self.content_str= str(self.content, encoding="utf-8")
        self.content_dir = eval(self.content_str)
        #eval函数把字符串转为字典
        self.access_token = self.content_dir['access_token']

        self.url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate?access_token=' + access_token
        # 二进制方式打开图文件
        self.f = open(r'C:\Users\Vincent Collins\Desktop\car.jpg', 'rb')
        # 参数image：图像base64编码
        self.img = base64.b64encode(self.f.read())
        self.params = {"image": self.img, "multi_detect": True}
        #multi_detect是可选的
        self.params = urllib.parse.urlencode(self.params).encode('utf-8')
        #encode是把str转换为bytes
        self.request2 = urllib.request.Request(self.url, self.params)
        self.request2.add_header('Content-Type', 'application/x-www-form-urlencoded')
        self.response2 = urllib.request.urlopen(self.request2)
        self.content2 = self.response2.read()
        if (self.content2):
            print(self.content2)

