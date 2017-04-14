#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import os

os.sys.path.append(os.path.join(os.path.dirname(), "../"))

from util.zplayutil import *

mysql_config = get_config_dict(section="mysql")


def connMysql(host='localhost', db='test', user='root', passwd='', port=3306, charset=''):
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset, port=port)
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return conn


def connMysql_localhost(host='localhost', db='test', user=mysql_config.get('db_port'),
                        passwd=mysql_config.get('db_pass'), port=mysql_config.get('db_port'), charset='utf8'):
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
