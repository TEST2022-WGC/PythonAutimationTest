# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 21:46
# @Author  : simon.wang
# @File    : yaml_util.py
# @Software: PyCharm
import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        """
        把yaml文件传入到类
        :param yaml_file:
        """
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        """
        反序列化，把yaml格式转化成dict格式
        :return:
        """
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value

    # 写入yaml文件
    def write_yaml(self):
        pass

