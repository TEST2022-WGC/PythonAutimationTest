# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 23:01
# @Author  : simon.wang
# @File    : profiles_get_profile.py
# @Software: PyCharm
import allure
import pytest
from common.logger_util import logger
from base.base_util import BaseUtil
from common.request_util import RestClient
from common.common_util import read_config_yaml, read_extract_yaml, read_testcase_webapi_yaml


# @allure.parent_suite('针对单接口的测试')
# @allure.suite('Profiles模块')
# @allure.sub_suite("接口：/profiles/profile 通过卡号、手机号、证件号、Email或外部会员号 获取一条会员档案信息")
@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("LPS_Web_API 接口自动化测试")
@allure.feature("Profiles模块")
class TestGetProfile(BaseUtil):

    @allure.link(name="点击查看接口swagger", url=read_config_yaml('web_api', 'url') +
                                           '/docs/index#!/Profiles/Profiles_GetProfile')
    @allure.story('/profiles/profile   通过卡号、手机号、证件号、Email或外部会员号 获取一条会员档案信息')
    @pytest.mark.parametrize('data', read_testcase_webapi_yaml("profiles/test_get_profile.yaml"))
    def test_get_profile(self, data):
        allure.dynamic.title(data['title'])
        allure.dynamic.description(data['description'])
        # 判断是否跳过这条用例
        skip = data['skip']
        if skip == 1:
            logger.info(f'是否跳过这条测试用例：{skip} 跳过')
            pytest.skip(f'因为用例中skip值为{skip}，所以跳过本条用例')
        elif skip == 0:
            logger.info(f'用例中skip值为:{skip} 继续执行用例')
            # 获取请求用的参数
            self.url = '/api/v' + read_config_yaml('web_api', 'version') + \
                       data['request']['url']
            self.method = data['request']['method']
            # 更换headers的token
            if data['request']['headers']['Authorization'] is None:
                data['request']['headers']['Authorization'] = read_extract_yaml('api_token')
            self.headers = data['request']['headers']
            self.body = data['request']['body']
            self.validate = data['validate']['codes']
            logger.info(f'获取参数url:{self.url},method:{self.method},headers:{self.headers},params:{self.body}')
            try:
                self.res = RestClient(read_config_yaml('web_api', 'url')).request(url=self.url, method=self.method,
                                                                                  headers=self.headers, **self.body)
                # 上传响应报文
                allure.attach(self.res.text, 'response body')
            except Exception as e:
                logger.exception(f'Exception信息：\n + {e}')
                logger.error(f'返回报文是：{self.res}')
            finally:
                success_code = (200, 201, 202, 203, 204)
                failed_code = (400, 401, 402, 403, 404, 500, 501, 502, 503, 504)
                if self.res.status_code in success_code:
                    logger.info(f'响应状态码为：{self.res.status_code}')
                    assert self.res.status_code == self.validate
                    assert self.res.json()['id'] == data['validate']['equals']
                elif self.res.status_code in failed_code:
                    logger.info(f'响应状态码为：{self.res.status_code}')
                    assert self.res.status_code == self.validate
                else:
                    logger.error('不符合预期值,或者未知的异常错误')
                    pytest.fail('用例执行失败：不符合预期值,或者未知的异常错误')

        else:
            logger.error(f'无法判断是否执行本条用例，本条用例中的skip值为：{skip}')
            pytest.fail(f'无法判断是否执行本条用例，本条用例中的skip值为：{skip}')
