# -*- coding: utf-8 -*-
# @Time    : 2023/3/14 19:53
# @Author  : simon.wang
# @File    : allure_util.py
# @Software: PyCharm
import json
from common.common_util import get_project_path


class AllureUtil:
    def __init__(self):
        self.dict = {}

    # 获取json里面数据
    def get_json_data(self, name):
        # 定义为只读模型，并定义名称为f
        with open(f'{get_project_path()}/report/widgets/summary.json', 'rb') as f:
            # 加载json文件中的内容给params
            params = json.load(f)
            # 修改内容
            params['reportName'] = name
            # 将修改后的内容保存在dict中
            self.dict = params
        # 关闭json读模式
        f.close()
        # 返回dict字典内容
        return self.dict

    # 写入json文件
    def write_json_data(self):
        # 定义为写模式，名称定义为r
        with open(f'{get_project_path()}/report/widgets/summary.json', 'w', encoding="utf-8") as r:
            # 将dict写入名称为r的文件中
            json.dump(self.dict, r, ensure_ascii=False, indent=4)

        # 关闭json写模式
        r.close()


