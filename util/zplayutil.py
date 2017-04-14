#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser


def get_config_dict(cfg_file='../conf/app.conf', section='OSS'):
    config = ConfigParser.RawConfigParser()
    config.read(cfg_file)
    return dict(config.items(section))