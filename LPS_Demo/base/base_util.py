# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 23:42
# @Author  : simon.wang
# @File    : base_util.py
# @Software: PyCharm
import allure

from base.get_token import Token
from common.common_util import clear_extract_yaml, read_extract_yaml


# 接口测试用
class BaseUtil:
    from common.logger_util import logger

    def setup_class(self):
        Token().write_token()
        self.logger.info('class前置，清空并重新写入extract')

    def setup_method(self):
        self.logger.info("------------------------------接口测试用例开始------------------------------")

    def teardown_method(self):
        self.logger.info("------------------------------接口测试用例结束------------------------------")

    def teardown_class(self):
        clear_extract_yaml()
        self.logger.info('class后置，清空extract文件')


