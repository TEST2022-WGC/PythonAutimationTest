import pytest
from common import logger_util
from common import common_util
from common import yaml_util


# 会话级fixture，自动执行，用来标记自动化测试整体的开始结束
@pytest.fixture(scope="session", name='logger', autouse=True)
def session_fixture():
    from common.logger_util import logger
    logger.info('session前置：本次自动化测试开始')
    yield
    logger.info('session后置：本次自动化测试结束')
    logger.info('session后置:开始removeHandler')
    logger.removeHandler('file')
    logger.info('session后置:removeHandler成功')




# # 定义作用域为方法的，非自动使用的，参数化
# @pytest.fixture(params=('第一次', '第二次', '第三次'))
# def web_all_params(request):
#     print('参数化前置')
#     yield request.param
#     print('参数化后置')
