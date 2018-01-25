# coding:utf-8


"""
version v0.1

构成：

- Request请求、页面下载器(改用gevent+request异步请求)
    - request 制作，定制请求头，轮转，设置POST、GET
    - 下载器 可以支持代理下载
    - 存储到内部队列(生产者-消费者模型)
    - 整个过程都是gevent异步的

by yg


"""

import requests
import setting

import random

from plugin.FreeIPPool import IpSpiders


class Xdownloader:
    """
    管理request定制到response获取整个流程
    """

    def __init__(
        self,
        url,
        way='GET',
        payload={},
        headers={},
        data={},
        cookies={}
    ):
        # url、header、
        self.url = url
        self.way = way  # 请求方法  get post
        self.payload = payload  # 参数
        self.headers = headers
        self.data = data  # 用于post请求
        self.cookies = cookies  # 用于附带cookies请求

        self.ip_proxies = setting.DOWNLOADER_DICT.get('IP_AGENT')  # 是否启用IP代理
        self.rotary_head = setting.DOWNLOADER_DICT.get(
            'ROTARY_HEAD')  # 是否启用头部轮转

    def start_download(self):

        # GET方法
        responese_obj = requests.request(
            method='GET',
            url=self.url,
            params=self.payload,
            headers=self.add_useragent() if self.rotary_head else {},
            cookies=self.cookies,
            allow_redirects=True,
            proxies=self.add_ip_proxies() if self.ip_proxies else None,
        )
        # print(responese_obj)
        print(responese_obj.request.headers)
        # print(responese_obj.url)
        # print(responese_obj.text)
        return "response"

    def add_ip_proxies(self):

        if self.ip_proxies:

            ip_ojb = IpSpiders()
            ip_list = ip_ojb.get_ip()
            print(ip_list)
            choice_ip = random.choice(ip_list)
            http_str = "http://%s:%s/" % (choice_ip.get('ip'),choice_ip.get('port'))
            print http_str
            return {"http": http_str}


    def add_cookies(self, cookies):
        self.cookies = cookies
        return self.cookies

    def add_useragent(self):
        # 添加头部信息
        pass
        user_agent_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

        return {'User-Agent': random.choice(user_agent_list)}


if __name__ == "__main__":

    x = Xdownloader(url=r'http://looncode.com')
    x.start_download()
