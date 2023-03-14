import datetime
import os
import pytest
import time
from common.allure_util import AllureUtil


# 报告生成时间
t = datetime.datetime.now().strftime('%Y-%m-%d')
# 报告名称
report_name = 'report_' + t + '.html'
# 报告路径
report_path = os.getcwd() + '\\report\\'


if __name__ == '__main__':
    # pytest.main(['-vs', '--html=' + report_path + report_name, '--reruns=2'])
    # 运行测试用例
    pytest.main()
    time.sleep(1)
    # 生成allure报告
    os.system('allure generate ./temp -o ./report --clean')
    # 修改报告title
    w = AllureUtil()
    revised_dict = w.get_json_data('LPS Report')
    w.write_json_data()
