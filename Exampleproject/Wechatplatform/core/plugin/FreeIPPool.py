#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import urllib2
from cprint import cprint
import re
from threading import Thread, current_thread

'''
1、需求：为了避免部分网站反爬虫机制，经常需要使用IP代理访问，但是网上免费IP具有时效性，此模块用于构建维护可用免费IP池。
2、设计：IPSpiders类，专门用来去爬多个免费网站的IP。Items类，专门用于保存爬去到的数据到DB中。GetIP类，提取IP和维护IP池。
3、采用单利模式
by yg

'''
# 官网给的单例模式实现代码，利用了装饰器的特点


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class IpSpiders():

    def __init__(self):
        #
        self.item = Ip_Item()
        self.start_crawl_flag = False

    # 每个网站对饮给一个方法爬虫
    def spider_one(self):
        # 爬虫A
        web_str = self.download_page(
            url=r"http://www.kuaidaili.com/free/inha/1")

        cprint(web_str)

        # 数据格式: data=[{'ip':'xx.xx.xx.xx','port':'80','location','time'},{'ip':'xx.xx.xx.xx','port':'80'}]
        data = []
        one_ip_data_dict = {'ip': None, 'port': None,
                            'location': None, 'time': None}

        # 分析里面的内容,用正则拿出来，
        ip_regular = r"<td.*IP.*>(.+)</td>"
        port_regular = r"<td.*PORT.*>(.+)</td>"

        ip_list = re.findall(ip_regular, web_str)
        port_list = re.findall(port_regular, web_str)

        # print ip_list,len(ip_list)
        # print port_list,len(port_list)
        # print location_list,len(location_list)
        # print time_list,len(time_list)

        # 把数据放到list中
        for i in range(0, len(ip_list)):

            one_ip_data_dict = {
                'ip': ip_list[i],
                'port': port_list[i],
            }
            data.append(one_ip_data_dict)
        cprint(data)

        # 验证IP可用性
        usable_data = self.item.verify_ip(data)

        # 调用item存储数据
        self.item.receive_date(usable_data)

        pass
        return True


# 每个网站对饮给一个方法爬虫
    def spider_sec(self):
        # 爬虫B
        web_str = self.download_page(url=r"http://www.xicidaili.com/nn/1")

        cprint(web_str)

        # 数据格式: data=[{'ip':'xx.xx.xx.xx','port':'80','location','time'},{'ip':'xx.xx.xx.xx','port':'80'}]
        data = []
        one_ip_data_dict = {'ip': None, 'port': None,
                            'location': None, 'time': None}

        # 分析里面的内容,用正则拿出来，
        ip_regular = r"<td>(\d+\.\d+\.\d+\.\d+)</td>"
        port_regular = r"<td>(\d{2,5})</td>"

        ip_list = re.findall(ip_regular, web_str)
        port_list = re.findall(port_regular, web_str)

        print ip_list, len(ip_list)
        print port_list, len(port_list)

        # 把数据放到list中
        for i in range(0, len(ip_list)):

            one_ip_data_dict = {
                'ip': ip_list[i],
                'port': port_list[i],
            }
            data.append(one_ip_data_dict)
        # cprint(data)

        # 验证IP可用性
        usable_data = self.item.verify_ip(data)

        # 调用item存储数据
        self.item.receive_date(usable_data)

        pass
        return True

    def spider_three(self):

        # 爬虫C
        web_str = self.download_page(
            url=r"http://www.xdaili.cn/ipagent/freeip/getFreeIps?page=1&rows=10")
        cprint(web_str)

        # 数据格式: data=[{'ip':'xx.xx.xx.xx','port':'80','location','time'},{'ip':'xx.xx.xx.xx','port':'80'}]
        data = []
        one_ip_data_dict = {'ip': None, 'port': None,
                            'location': None, 'time': None}

        # 分析里面的内容,用正则拿出来，
        ip_regular = r'"(\d+\.\d+\.\d+\.\d+)"'
        port_regular = r'"port":"(\d{2,5})"'

        ip_list = re.findall(ip_regular, web_str)
        port_list = re.findall(port_regular, web_str)

        print ip_list, len(ip_list)
        print port_list, len(port_list)

        # 把数据放到list中
        for i in range(0, len(ip_list)):

            one_ip_data_dict = {
                'ip': ip_list[i],
                'port': port_list[i],
            }
            data.append(one_ip_data_dict)
        # cprint(data)

        # 验证IP可用性
        usable_data = self.item.verify_ip(data)

        # 调用item存储数据
        self.item.receive_date(usable_data)

        pass
        return True

    def spider_four(self):

        # 爬虫D
        web_str = self.download_page(url="http://www.nianshao.me")
        cprint(web_str)

        # 数据格式: data=[{'ip':'xx.xx.xx.xx','port':'80','location','time'},{'ip':'xx.xx.xx.xx','port':'80'}]
        data = []
        one_ip_data_dict = {'ip': None, 'port': None,
                            'location': None, 'time': None}

        # 分析里面的内容,用正则拿出来，
        ip_regular = r'(\d+\.\d+\.\d+\.\d+)</td>'
        port_regular = r'<td .+>(\d{2,5})</td>'

        ip_list = re.findall(ip_regular, web_str)
        port_list = re.findall(port_regular, web_str)

        print ip_list, len(ip_list)
        print port_list, len(port_list)

        # 把数据放到list中
        for i in range(0, len(ip_list)):

            one_ip_data_dict = {
                'ip': ip_list[i],
                'port': port_list[i],
            }
            data.append(one_ip_data_dict)
        # cprint(data)

        # 验证IP可用性
        usable_data = self.item.verify_ip(data)

        # 调用item存储数据
        self.item.receive_date(usable_data)

        pass
        return True

    # 获取数据

    def get_ip(self):

        if self.start_crawl_flag == False:
            self.start_crawl()

        # print self.item.data
        return self.item.data

    # 开始爬取
    def start_crawl(self):

        self.spider_one()
        self.spider_sec()
        self.spider_three()
        self.spider_four()
        self.start_crawl_flag = True
        return True

    # 网页下载器
    def download_page(self, url):
        # 构建头部，轮转，下载，返回。
        user_agent = [
            r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:54.0) Gecko/20100101 Firefox/54.0",
            r"Opera/9.27 (Windows NT 5.2; U; zh-cn)",
            r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            r"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            r"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            r"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            r"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            r"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        # 用urllib2下载网页
        headers = {'User-Agent': random.choice(user_agent)}
        req = urllib2.Request(url=url, headers=headers)
        response_object = urllib2.urlopen(req)

        return response_object.read()

    # data=[{'ip':'xx.xx.xx.xx','port':'80'},{'ip':'xx.xx.xx.xx','port':'80'}]

# 类似scrapy的item和pipeline


class Ip_Item(object):
    """docstring for Item"""

    # 需要的数据
    data = []

    def __init__(self):
        pass

    # data=[{'ip':'xx.xx.xx.xx','port':'80'},{'ip':'xx.xx.xx.xx','port':'80'}]
    def receive_date(self, data):
        #  接收数据的功能
        pass
        if data == []:
            print("收到数据为空")
            return False
        print("item收到数据")
        print data
        print(len(data))

        for i in data:  # 从data列表取出来，然后放入self.data
            # print i
            self.data.append(i)

        self.show_all_ip()
        # cprint(data)
        return True

    def show_all_ip(self):

        print("所有可用IP如下：")
        print self.data

        print("共计%s个" % str(len(self.data)))

    def save_to_db(self, data):
        # 保存到数据库中
        pass

    def save_to_txt(self, data):
        # 保存到文件
        pass

    def verify_ip(slef, data):
        # 检查哪些IP是可用的

        # 包装起来
        def get_test_ip():

            for i in data:
                yield i

        x = get_test_ip()
        # 要拿一次数据就x.next
        # print x.next()
        # print x.next()

        # 用来保存可用的IP
        usable_ip_list = []

        # 用于测试单个IP，每次运行从列表取一次IP出来测试
        def connect():
            # print data

            print "%s is running" % current_thread().name
            ip_dict = x.next()
            print ip_dict

            # 使用给代理方法1 ：这样处理的方式全局，影响其他urlopen
            # proxy = urllib2.ProxyHandler({'http':ip_str})
            # opener = urllib2.build_opener(proxy)
            # urllib2.install_opener(opener)

            # 使用代理方法2,每个访问自己使用代理。：

            ip_str = ip_dict['ip'] + ':' + ip_dict['port']
            req = urllib2.Request(url="http://cn.bing.com/")
            req.set_proxy(ip_str, 'http')
            # 访问：
            try:
                response = urllib2.urlopen(req, timeout=6)  # 访问打开
            except Exception as e:
                # 超时或者状态码不对
                print("IP[%s]失效" % ip_str)
            else:
                # 没有异常发生
                print response.getcode()
                if response.getcode() == 200:
                    print("IP:[%s]有效" % ip_str)
                    usable_ip_list.append(ip_dict)

        # 多线程改造
        thread_list = []
        for i in range(len(data)):
            t = Thread(target=connect, args=(), name=r"thread[%s]" % str(i))
            thread_list.append(t)

        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()

        print "有效的IP如下"
        print usable_ip_list

        # print(dir(response))

        pass

        return usable_ip_list



if __name__ == "__main__":

    x = IpSpiders()
    # z = IpSpiders()
    y = x.get_ip()
    print y


"""
结果类似：
[{'ip': '27.184.65.34', 'port': '8118'},
 {'ip': '116.2.119.95', 'port': '80'}, ]

"""
