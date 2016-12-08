# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = 'bid=hhucxXoyk1g; ll="118282"; ps=y; ct=y; ue="898657127@qq.com"; push_noty_num=0; push_doumail_num=0; _ga=GA1.2.813170573.1479442669; __utma=30149280.813170573.1479442669.1480654027.1480660612.10; __utmb=30149280.0.10.1480660612; __utmc=30149280; __utmz=30149280.1480660612.10.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.15452; _vwo_uuid_v2=B2CF66A89CE1C284420A7C1996CFE93C|32ee12198293f51ec3a4122e41e0801f; ap=1; as="https://movie.douban.com/"'
    trans = transCookie(cookie)
    print trans.stringToDict()