# -*- coding: utf-8 -*-

import configparser


def parse_config_file(config_file):
    cf = configparser.ConfigParser()
    cf.read(config_file)
    k_v_items = cf.items('spider')
    config_items_dict = {}
    for k, v in k_v_items:
        config_items_dict[k] = v
    return config_items_dict
