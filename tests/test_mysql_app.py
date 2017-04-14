#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


from app.mysql_app import *


def test_count():
    sql = "select count(*) as cnt from date_test;"
    result = query(sql)
    assert result[0].get('cnt'), 'records count not  3, failed.'


# def test_count_local():
#     sql = "select count(*) as cnt from date_test;"
#     result = query_local(sql)
#     print result
#     print type(result)
#     assert result[0].get('cnt') == 3, 'records count not  3, failed.'