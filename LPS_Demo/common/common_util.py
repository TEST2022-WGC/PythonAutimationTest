# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 21:31
# @Author  : simon.wang
# @File    : common_util.py
# @Software: PyCharm
import os
import yaml


def get_project_path():
    # 获取项目路径
    real_path = os.path.dirname(__file__).split('common')[0]
    return real_path


def read_config_yaml(first, second):
    # 读取全局配置yaml文件
    with open(str(get_project_path()) + 'config\\config.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg[first][second]


def read_logconfig_yaml():
    # 读取logconfig
    with open(str(get_project_path()) + 'config\\logconfig.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg


def read_extract_yaml(first):
    # 读取token
    with open(str(get_project_path()) + 'config\\extract.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg[first]


def write_extract_yaml(extract_dict):
    # 写入token
    with open(str(get_project_path()) + 'config\\extract.yaml', 'a') as f:
        yaml.dump(extract_dict, f)


def clear_extract_yaml():
    # 清空extract yaml文件
    with open(str(get_project_path()) + 'config\\extract.yaml', 'w') as f:
        f.truncate()


def read_testcase_webapi_yaml(testcase_name):
    # 读取web api测试用例，数据驱动用
    with open(str(get_project_path()) + 'data\\' + testcase_name, encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg


if __name__ == '__main__':
    print(get_project_path())