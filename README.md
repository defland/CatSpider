# CatSpider

Python编写的异步+分布式+通用mini爬虫，可以支持爬取队列、Request定制、IP代理访问和页面抓取、Response数据清洗、本地化 存储等功能。

# CatSpider构成

- 爬虫队列 queue
- Request请求、页面下载器(改用gevent+request异步请求)
- Response处理和信息提取
- 清洗后的数据存储


# CatSpider base

- Redis
- Requests
- Gevent

# CatSpider 目录说明和工作流说明


```
.
├── README.md
├── catspider.py # 执行入口
├── core
│   ├── __init__.py # 初始化文件
│   ├── setting.py # 项目设置
│   ├── xanalyzer.py # 数据清洗部分
│   ├── xdownloader.py # 下载器，制造request、设置header轮转、IP代理、异步多线程下载页面等功能
│   ├── xitem.py # 爬虫数据本地化存储
│   └── xqueue.py #  爬虫队列
└── requirements.txt # pip 库列表

```
使用流程：

- 定义first url，放入爬虫队列
- 在setting.py配置下载器参数
- xanalyzer.py编写数据清洗和提取规则，新url放入爬虫队列,清洗出来数据转存xitem
- xitem.py存储数据

执行工作流：

- python catspider.py start 等可以附带参数
- 爬虫从队列头部取出




# 基于CatSpider的Demo

- 囤好币(币种的行情、背景信息)


