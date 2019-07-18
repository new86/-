"""
-*- coding:utf-8 -*-
项目:微信机器人--数据库--工具
"""
import pymysql

class Myssql:
# 数据库配置信息
    def __init__(self,localhost,port,user,passwd,database,charset):
        self.config={"host":localhost,
                     "port":port,
                     "user":user,
                     "passwd":passwd,
                     "database":database,
                     "charset":charset
        }
        self.db=pymysql.connect(**self.config)
        self.cursor=self.db.cursor()

    #delete from tableName where where
    def delete(self,tableName,where):
        """
        删除数据
        :return:
        """
        if where is None:
            a= "delete from %s" % (tableName)
            return print("OK")
        a = "delete from %s where %s" % (tableName, where)
        return print("OK")



    def Myexecute(self,instruct,tableName,values):
        try:
            if instruct=="insert":
                pass
            elif instruct=="delete":
                self.delete(tableName,values)

            elif instruct=="update":
                pass
            elif instruct=="select":
                pass
        except Exception as e:
            print(e,instruct)






