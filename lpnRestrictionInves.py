'''{
	"reason":"查询成功",
	"result":[
		{
			"city":"beijing",
			"cityname":"北京"
		},
		{
			"city":"guiyang",
			"cityname":"贵阳"
		},
		{
			"city":"hangzhou",
			"cityname":"杭州"
		},
		{
			"city":"lanzhou",
			"cityname":"兰州"
		},
		{
			"city":"tianjin",
			"cityname":"天津"
		},
		{
			"city":"chengdu",
			"cityname":"成都"
		},
		{
			"city":"nanchang",
			"cityname":"南昌"
		},
		{
			"city":"changchun",
			"cityname":"长春"
		},
		{
			"city":"haerbin",
			"cityname":"哈尔滨"
		},
		{
			"city":"chongqing",
			"cityname":"重庆"
		}
	],
	"error_code":0
}'''
# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib.request, json
from urllib.parse import urlencode

def main():
    """
    参数配置：
    city:查询城市的代码，如beijing
    type:查询限号类型，1:今天 2:明天 3:后天
    key:申请的尾号限行API key
    """
    params = {"key": "4c5e32ce5726136069ece29f59b989da", "city": "beijing", "type": "1"}
    queryResult = query(params)
    # print queryResult
    if queryResult:
        if queryResult['isxianxing'] == 1:
            weihaos = queryResult['xxweihao']
        else:
            weihaos = ''
        print("城市：%s,日期：%s,%s" % (queryResult['city'], queryResult['date'], queryResult['week']))
        print("是否限行：%s,限行尾号:%s" % (queryResult['isxianxing'], weihaos))
        # print queryResult
        # print queryResult['date']
    else:
        print("查询失败")


def query(params):
    params = urlencode(params)
    url = 'http://v.juhe.cn/xianxing/index?%s' % params
    wp = urllib.request.urlopen(url)
    content = wp.read()
    res = json.loads(content)
    if res:
        error_code = res['error_code']
        if error_code == 0:
            return res['result']
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
