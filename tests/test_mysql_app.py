#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from app.mysql_app import *


def test_count():
    sql = "select count(*) from date_test;"
    result = query(sql)
    assert len(result) == 3, 'records count not  3, failed.'
