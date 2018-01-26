# coding:utf-8

"""
version v0.1

构成：

- 爬虫队列 queue
    - 用queue对象实现（new/add/del/mod/find/）
    - 队列存储到redis，queue内部实现方法存取redis

- Request请求、页面下载器(改用gevent+request异步请求)
    - request 制作
    - 下载器 可以支持代理下载
    - 存储到内部队列(生产者-消费者模型)
    - 整个过程都是gevent异步的

- Response处理和信息提取
    - 消息的定义
    - 数据的清洗(抓取出信息出来)
    - 数据存入

- 清洗后的数据存储
    - 保存到数据库


by yg


"""

# 队列管理

from core import *


if __name__ == "__main__":

    # MVP版本
    # 串联整个工作流

    # frist url放入云队列
    # 开始下载器执行
    # 放入本队队列
    # 分析器取出分析内容(新的url、清洗出来的内容return、去重)
    # 清洗出来的内容保存到本地或者云端

    # first url

    clqueue = xqueue.CloudXqueue('FEIXIAOHAO')

    clqueue.insert('http://www.feixiaohao.com')
    clqueue.insert('http://looncode.com')

    # start download

    # print("get url from CloudXqueue:", clqueue.get_no_wait())
    # print("get url from CloudXqueue:", clqueue.get())

    dwer = xdownloader.Xdownloader(url=clqueue.get()[1])
    respnese_data = dwer.start_download()

    print(respnese_data)

    # # start data clear
    # xclear = xanalyzer.Xanalyzer(respnese_data)
    # xclear.start_clear()

    # # start data storage
