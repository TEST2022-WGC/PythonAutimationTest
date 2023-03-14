# -*- coding: utf-8 -*-
# @Time    : 2023/3/11 15:05
# @Author  : simon.wang
# @File    : get_token.py
# @Software: PyCharm


import requests
from common import common_util


class Token:

    def __init__(self):
        """
        token配置以及存放token值的路径
        当请求token时的url或date有变动时，直接在配置文件修改即可
        """
        self.url = common_util.read_config_yaml('token', 'token_url')
        self.header = {
            'Content - Type': 'application / x - www - form - urlencoded'
        }
        self.date = common_util.read_config_yaml('token', 'date')
        self.extract = common_util.get_project_path() + '\\config\\extract.yaml'
        self.extract_dict = {}

    def get_token(self):
        """
        获取请求头中的Bearer开的token字符串
        :return: 放入请求头的token
        """
        res = requests.request('post', url=self.url, headers=self.header, data=self.date)
        token = res.json()['access_token']
        # 组装成请求头中的格式
        tokens = "Bearer" + ' ' + token
        return tokens

    def write_token(self):
        common_util.clear_extract_yaml()
        self.extract_dict = {
            "api_token": Token().get_token()
        }
        common_util.write_extract_yaml(self.extract_dict)


if __name__ == '__main__':
    Token().write_token()
