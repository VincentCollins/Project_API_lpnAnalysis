# -*- coding: utf-8 -*-
import urllib.request,urllib.parse, base64
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=oPCATAa46bL4MIvtkkqLLskU&client_secret=TSCb3Nkro5CC7f0mGBjIkimFe2BkxFmv'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()

if (content):
    print(type(content))
content_str= str(content, encoding="utf-8")
content_dir = eval(content_str)
#eval函数把字符串转为字典
access_token = content_dir['access_token']

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'C:\Users\Vincent Collins\Desktop\car.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img, "multi_detect": True}
#multi_detect是可选的
params = urllib.parse.urlencode(params).encode('utf-8')
#encode是把str转换为bytes
request2 = urllib.request.Request(url, params)
request2.add_header('Content-Type', 'application/x-www-form-urlencoded')
response2 = urllib.request.urlopen(request2)
content2 = response2.read()
if (content2):
    print(content2)

