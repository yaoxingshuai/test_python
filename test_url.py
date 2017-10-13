#!/usr/bin/env python
# coding=utf-8
# 测试我的聚合数据   python2
import urllib2
import json
url='https://v.juhe.cn/historyWeather/weather?city_id=93&weather_date=2017-10-13&key=489ac8c77dbfebe6f865a4b3193957de'
req=urllib2.Request(url)

ret=urllib2.urlopen(req)
ret_data_json=ret.read()

ret_data=json.loads(ret_data_json)
for key,val in ret_data['result'].items():
    print u'key={}, val={}'.format(key, val)  # ps: 必须要 u''
    print key, val
print '-----end-----'
