#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os

import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from app.operator import *


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2, 5) == 12
