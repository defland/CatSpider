# coding:utf-8


"""
version v0.1

构成：

- 爬虫队列 queue
    - 用queue对象实现（new/add/del/mod/find/）
    - 队列存储到redis，queue内部实现方法存取redis

by yg

"""

from . import setting


class Queue:
    """
    1、增删改查
    2、是否采用Redis存储
    3、默认采用广度优先的队列,新添加的url放入queue尾部
    """

    def __init__(self):
        self.use_redis = setting.USE_REDIS
        self.items = []

    def isEmpty(self):  # 为空
        return self.items == []

    def takeout(self, item):  # 顶部取出
        self.items.insert(0, item)

    def putin(self):  # 顶部删除
        return self.items.pop()

    def size(self):
        return len(self.items)  # 大小，高度

    def show(self):
        print(self.items)
