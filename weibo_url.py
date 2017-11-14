# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author GengYanpeng
@software:PyCharm Community Edition
@time:2017/10/29 09:33
"""
# import sys

# reload(sys)
# sys.setdefaultencoding('utf8')

dict1 = {'工业制造':'http://s.weibo.com/user/%25E5%25B7%25A5%25E4%25B8%259A%25E5%2588%25B6%25E9%2580%25A0&page=1',
'智造':'http://s.weibo.com/user/%25E6%2599%25BA%25E9%2580%25A0&page=1',
 '物联网':'http://s.weibo.com/user/%25E7%2589%25A9%25E8%2581%2594%25E7%25BD%2591&page=1',
 '机器人':'http://s.weibo.com/user/&tag=%25E6%259C%25BA%25E5%2599%25A8%25E4%25BA%25BA&page=1',
 '人工智能':'http://s.weibo.com/user/%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD&page=1',
 '机械制造':'http://s.weibo.com/user/&tag=%25E6%259C%25BA%25E6%25A2%25B0%25E5%2588%25B6%25E9%2580%25A0&page=1',
 '工业设计':'http://s.weibo.com/user/&tag=%25E5%25B7%25A5%25E4%25B8%259A%25E8%25AE%25BE%25E8%25AE%25A1&page=1',
 '智能设计':'http://s.weibo.com/user/&nickname=%25E6%2599%25BA%25E8%2583%25BD%25E8%25AE%25BE%25E8%25AE%25A1&page=1',
 '家居设计':'http://s.weibo.com/user/&nickname=%25E5%25AE%25B6%25E5%25B1%2585%25E8%25AE%25BE%25E8%25AE%25A1&page=1',
 '机械设计':'http://s.weibo.com/user/&nickname=%25E6%259C%25BA%25E6%25A2%25B0%25E8%25AE%25BE%25E8%25AE%25A1&page=1',
 '智能家居':'http://s.weibo.com/user/&tag=%25E6%2599%25BA%25E8%2583%25BD%25E5%25AE%25B6%25E5%25B1%2585&page=1',
 '数码':'http://s.weibo.com/user/&tag=%E6%95%B0%E7%A0%81&page=1',
 '汽车':'http://s.weibo.com/user/&nickname=%25E6%25B1%25BD%25E8%25BD%25A6&page=1',
 '家居':'http://s.weibo.com/user/&tag=%25E5%25AE%25B6%25E5%25B1%2585&page=1',
 '曝光':'http://s.weibo.com/user/&nickname=%E6%9B%9D%E5%85%89&page=1',
 '商业':'http://s.weibo.com/user/&nickname=%25E5%2595%2586%25E4%25B8%259A&auth=ord&page=1',
 '电商':'http://s.weibo.com/user/&tag=%25E7%2594%25B5%25E5%2595%2586&auth=ord&page=1',
 '大宗商品':'http://s.weibo.com/user/&tag=%25E5%25A4%25A7%25E5%25AE%2597%25E5%2595%2586%25E5%2593%2581&auth=ord&page=1',
 '地产':'http://s.weibo.com/user/&nickname=%25E5%259C%25B0%25E4%25BA%25A7&auth=ord&page=1',
'文化产业':'http://s.weibo.com/user/&nickname=%25E6%2596%2587%25E5%258C%2596%25E4%25BA%25A7%25E4%25B8%259A&page=1',
 '招标':'http://s.weibo.com/user/&nickname=%25E6%258B%259B%25E6%25A0%2587&page=1',
 '股市':'http://s.weibo.com/user/&nickname=%25E8%2582%25A1%25E5%25B8%2582&page=1',
 '财经':'http://s.weibo.com/user/&nickname=%25E8%25B4%25A2%25E7%25BB%258F&auth=ord&page=1',
 '金融科技':'http://s.weibo.com/user/&nickname=%25E9%2587%2591%25E8%259E%258D%25E7%25A7%2591%25E6%258A%2580&page=1',
 '投资':'http://s.weibo.com/user/&nickname=%25E6%258A%2595%25E8%25B5%2584&auth=ord&page=1',
 '社会观察':'http://s.weibo.com/user/&nickname=%E7%A4%BE%E4%BC%9A%E8%A7%82%E5%AF%9F&page=1'}

dict2 = {'职场':'http://s.weibo.com/user/&nickname=%25E8%2581%258C%25E5%259C%25BA&page=1',
 '智库':'http://s.weibo.com/user/&nickname=%25E6%2599%25BA%25E5%25BA%2593&auth=ord&page=1',
 '大数据':'http://s.weibo.com/user/&nickname=%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE&page=1',
 '互联网':'http://s.weibo.com/user/&nickname=%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591&auth=ord&page=1',
 '物流':'http://s.weibo.com/user/&nickname=%25E7%2589%25A9%25E6%25B5%2581&page=1'}

# for k,v in dict1.items():
#   print(k, v)
