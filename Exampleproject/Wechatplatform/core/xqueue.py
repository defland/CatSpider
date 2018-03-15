# coding:utf-8


"""
version v0.1

构成：

- 爬虫队列 queue
    - 用queue对象实现（new/add/del/mod/find/）
    - 队列存储到redis，queue内部实现方法存取redis

by yg

"""


import setting
import redis


class CloudXqueue:
    """
    1、增删改查
    2、是否采用Redis存储
    3、默认采用广度优先的队列,新添加的url放入queue尾部
    """

    def __init__(self, queue_name, namespace='CloudXqueue', **redis_kwargs):
        self.use_redis = setting.USE_REDIS
        # reids queue namespace
        self.key = '%s:%s' % (namespace, queue_name)
        self.__redis_r = self.init_redis()  # use redis

    def init_redis(self):
        if self.use_redis:
            pool = pool = redis.ConnectionPool(
                host=setting.REDIS_DICT.get('ADDRESS'),
                port=setting.REDIS_DICT.get('PORT'),
                password=setting.REDIS_DICT.get('PASSWROD'),
                db=setting.REDIS_DICT.get('DB')
            )
            r = redis.Redis(connection_pool=pool)
            return r

    def isEmpty(self):  # 为空
        return self.size() == 0

    def insert(self, item):  # 顶部取出
        try:
            self.__redis_r.rpush(self.key, item)
            return True
        except Exception as e:
            print(e)
            return False

    def get(self, block=True, timeout=None):  # 顶部删除
        # 分阻塞模式和非阻塞模式
        if block:
            return self.__redis_r.blpop(self.key, timeout=timeout)
        else:
            return (self.key, self.__redis_r.lpop(self.key))

    def get_no_wait(self):  # 顶部删除
        return self.get(block=False)

    def size(self):
        return self.__redis_r.llen(self.key)  # 大小，高度

    def show(self):
        for key in self.__redis_r.scan_iter(self.key):
            # print the key
            print(key)


class LocalXqueue:

    def __init__(self):
        self.items = []

    def isEmpty(self):  # 为空
        return self.items == []

    def enqueue(self, item):  # 顶部新增
        self.items.insert(0, item)

    def dequeue(self):  # 顶部删除
        return self.items.pop()

    def size(self):
        return len(self.items)  # 大小，高度

    def show(self):
        print(self.items)


if __name__ == "__main__":

    x = CloudXqueue('test')
    print(x.size())
