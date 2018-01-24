# CatSpider

Python编写的异步爬虫，可以支持爬取队列、Request定制、代理访问和页面抓取、数据清洗等功能。

# CatSpider构成

- 爬虫队列 queue
- Request请求、页面下载器(改用gevent+request异步请求)
- Response处理和信息提取
- 清洗后的数据存储


# 基于CatSpider的Demo

- 囤好币(币种的行情、背景信息)
