# !/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request, json
from urllib.parse import urlencode

#available cities:beijign, guiyang, hangzhou, lanzhou, tianjin, chengdu, nanchang, changchun, haerbin, chongqing
#type意义：1  今天 2 明天 3 后天(1~7)
class API_illegality(object):
    def __init__(self):
        self.Params = {"key": "4c5e32ce5726136069ece29f59b989da", "city": "beijing", "type": "1"}
        self.params = urlencode(self.Params)
        self.url = 'http://v.juhe.cn/xianxing/index?%s' % self.params


    def query(self):

        self.wp = urllib.request.urlopen(self.url)
        self.content = self.wp.read()
        self.res = self.json.loads(self.content)
        if self.res:
            self.error_code = self.res['error_code']
            if self.error_code == 0:
                self.queryResult=self.res['result']
            else:
                self.queryResult =False
        else:
            self.queryResult =False

        if self.queryResult:
            if self.queryResult['isxianxing'] == 1:
                self.weihaos = self.queryResult['xxweihao']
            else:
                self.weihaos = ''
            print("城市：%s,日期：%s,%s" % (self.queryResult['city'], self.queryResult['date'], self.queryResult['week']))
            print("是否限行：%s,限行尾号:%s" % (self.queryResult['isxianxing'], self.weihaos))
            # print queryResult
            # print queryResult['date']
        else:
            print("查询失败")

    



if __name__ == "__main__":
    main()
