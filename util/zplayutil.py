#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import os

scriptdir = os.path.dirname(__file__)


def get_config_dict(section='mysql', cfg_file=os.path.join(scriptdir, '../conf/app.conf.example')):
    config = ConfigParser.RawConfigParser()
    config.read(cfg_file)
    return dict(config.items(section))


if __name__ == '__main__':
    print get_config_dict().get('db_port')
