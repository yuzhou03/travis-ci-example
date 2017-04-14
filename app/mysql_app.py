#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb


def connMysql(host='', db='', user='', passwd='', port=0, charset=''):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
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


