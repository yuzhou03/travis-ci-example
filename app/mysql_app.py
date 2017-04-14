#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

from util.zplayutil import *

def connMysql(host='', db='', user='', passwd='', port=0, charset=''):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return conn


def connMysql_localhost(host='localhost', db='test', user='', passwd='', port=5506, charset='utf8'):
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port)
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return conn


def query(sql):
    """
    短连接查询：根据sql，查询得到dict类型结果
    :param sql:
    :return dict:
    """
    conn = connMysql()
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result


def query_local(sql):
    """
    短连接查询：根据sql，查询得到dict类型结果
    :param sql:
    :return dict:
    """
    conn = connMysql_localhost()
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result
