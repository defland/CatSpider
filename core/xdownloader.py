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

    # use for ip proxies
    ip_list = []  # 存储代理ip
    ip_proxies = setting.DOWNLOADER_DICT.get('IP_PROXIES')  # 是否启用IP代理
    ip_overdue = setting.DOWNLOADER_DICT.get('IP_OVERDUE')  # 过期次数

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
        self.timeout = setting.DOWNLOADER_DICT.get('TIMEOUT')

        self.rotary_head = setting.DOWNLOADER_DICT.get(
            'ROTARY_HEAD')  # 是否启用头部轮转

        self.use_proxy = {}  # 记录单个request使用的ip代理

    def start_download(self):

        # 是否启用给代理
        proxies = None
        if Xdownloader.ip_proxies:
            ip_dict = Xdownloader.add_ip_proxies()
            if ip_dict != {}:
                http_str = "http://%s:%s/" % (ip_dict.get('ip'),
                                              ip_dict.get('port'))
                proxies = {'http': http_str}
                print(http_str)

        # 开始下载
        try:
            # GET方法
            responese_obj = requests.request(
                method='GET',
                url=self.url,
                params=self.payload,
                headers=self.add_useragent() if self.rotary_head else {},
                cookies=self.cookies,
                allow_redirects=True,
                proxies=proxies,
                timeout=self.timeout
            )

        except Exception as e:
            # raise e
            print('Connection error %s with %s', (self.url, ip_dict))
            Xdownloader.ip_list.remove(ip_dict)  # 删除失效的代理ip
            print('The invalid IP address has been deleted.')
            print(Xdownloader.ip_list, len(Xdownloader.ip_list))
            return {'status': False,
                    'url': self.url,
                    'exception': e,
                    'error': 'Connection error'
                    }

        # print(responese_obj)
        print(responese_obj.request.headers)
        print(responese_obj.headers)
        # print(responese_obj.url)
        # print(responese_obj.text)
        return {'status': True,
                'url': self.url,
                'error': None,
                'responese': responese_obj
                }

    @staticmethod
    def add_ip_proxies():
        # 调用免费ip代理

        #
        if Xdownloader.ip_overdue == 0 or Xdownloader.ip_list == []:
            # first get ip list

            ip_ojb = IpSpiders()
            ip_list = ip_ojb.get_ip()
            print(ip_list)
            Xdownloader.ip_list = ip_list
            choice_ip = random.choice(Xdownloader.ip_list)
            Xdownloader.ip_overdue -= 1  # 使用寿命-1

            return choice_ip

        elif Xdownloader.ip_list != []:

            choice_ip = random.choice(Xdownloader.ip_list)
            Xdownloader.ip_overdue -= 1  # 使用寿命-1
            return choice_ip
        else:

            return {}

    def add_cookies(self, cookies):

        self.cookies = cookies
        return self.cookies

    def add_useragent(self):
        # 添加头部信息
        user_agent_list = setting.USER_AGENT_LIST  # 是否启用IP代理
        return {'User-Agent': random.choice(user_agent_list)}


if __name__ == "__main__":

    x = Xdownloader(url=r'http://looncode.com')
    y = Xdownloader(url=r'https://baidu.com')
    z = Xdownloader(url=r'https://feixiaohao.com')
    x.start_download()
    y.start_download()
    z.start_download()
