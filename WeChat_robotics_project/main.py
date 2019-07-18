"""
-*- coding:utf-8 -*-
项目:微信机器人--数据库--主模块
"""
from Store_data import *


def main():
    config = {"host": "localhost",
              "port": 3306,
              "user": "root",
              "passwd": "123456",
              "database": "weather",
              "charset": "utf8"
    }
    db = Myssql(**config)
    #测试代码
    db.Myexecute("delete","user",'("2019-7-16","www","晴")')





if __name__=="__main__":
    main()

