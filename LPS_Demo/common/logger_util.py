# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 22:03
# @Author  : simon.wang
# @File    : logger_util.py
# @Software: PyCharm
import logging
import logging.config
import logging.handlers
import os

from common import common_util
from common import yaml_util
from common.common_util import get_project_path


class LoggerUtil:

    def __init__(self, file, logger):
        self.file = file
        self.logger = logger

    # 加载dict配置文件
    def add_dict_config(self):
        return logging.config.dictConfig(self.file)

    # 日志器
    def get_logger(self):
        loggers = logging.getLogger(self.logger)
        return loggers


class Logger:

    def __init__(self, loggers):
        """
        创建个配置文件配置好的 WGC 日志记录格式
        :param loggers: WGC
        """
        if not os.path.exists(get_project_path() + 'log'):
            os.makedirs(get_project_path() + 'log')
        self.file = yaml_util.YamlUtil(common_util.get_project_path() + '\\config\\logconfig.yaml').read_yaml()
        self.file['handlers']['file']['filename'] = os.path.dirname(os.path.dirname(__file__)) + '\\log\\trace.log'
        self.loggers = loggers
        logging.config.dictConfig(self.file)
        self.logger = logging.getLogger(self.loggers)


logger = Logger('WGC').logger

if __name__ == '__main__':
    logger.info('this is test info')
