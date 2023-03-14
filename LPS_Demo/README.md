# KunlunLPS 石基昆仑-会员管理系统自动化测试框架
####Author:Simon.wang

本项目实现接口自动化的技术选型：**Python+Requests+Pytest+YAML+Allure+Jenkins** ，目前主要是针对接口项目来开展的，通过 Python+Requests 
来发送和处理HTTP协议的请求接口，使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure 来生成测试报告。

>相关接口项目：[DEV-SCM | Shiji](https://dev-scm.shijicloud.com/)


## 项目说明

最终目标为在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。

首先利用Python把HTTP接口封装成Python接口，接着把这些Python接口组装成一个个的关键字，再把关键字组装成测试用例，而测试数据则通过YAML文件进行统一
管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。

另外，对接口自动化进行Jenkins持续集成。

## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具最好在venv的虚拟环境中安装 requirements.txt 依赖，执行命令：

```
pip install -r requirements.txt
```

接着，修改 ```config/config.yaml``` 配置文件，在Windows环境下，安装相应依赖之后，在项目根目录的命令行窗口执行命令：

```
python all_run.py
```

**注意**：all_run.py 文件已经集成了pytest以及allure generate命令行，实现了一键运行生成报告，存放临时报告的是根目录下```temp```文件夹，
最终生成的Allure报告路径为根目录下的```report```，我配置的Jenkins持续集成也会在根目录下生成一个```allure-report```,一个为了调试方便查看，
一个是为了CI把报告展示出来。

## 项目结构

- base ====>> 接口封装层，如封装HTTP接口为Python接口，和配置用例执行的各个级别前后置
- common ====>> 各种工具类
- config ====>> 配置文件基本测试环境的配置```config.yaml```,临时存放token```extract.yaml```，logging的配置```logconfig```
  ,其他的是CI用到的个性化Allure报告配置，通过jenkins复制到temp实现
- data ====>> 测试数据文件管理
- log ====>> 日志生成目录
- report ====>> ```all_run.py```生成的Allure测试报告
- testcase_webapi ====>> 存放Web_API接口测试用例,未来还有可能有```testcase_posapi```
- tools ====>> 用来存放一些下载的工具，如Allure包或者Web自动化的浏览器驱动
- venv ====>> 虚拟环境，得自己创建个，然后使用里面的Lib下的安装好的三方库，或者创建好的情况下请看项目部署的第一步
- pytest.ini ====>> pytest的配置文件，必须放在根目录
- requirements.txt ====>> 相关依赖包文件
- all_run.py ====>> 一键执行测试，生成allure报告

## 关键字封装说明--后续优化目标

关键字应该是具有一定业务意义的，在封装关键字的时候，可以通过调用多个接口来完成。在某些情况下，比如测试一个充值接口的时候，在充值后可能需要调用查询接口
得到最新账户余额，来判断查询结果与预期结果是否一致，那么可以这样来进行测试：

- 1, 首先，可以把 **```充值-查询```** 的操作封装为一个关键字，在这个关键字中依次调用充值和查询的接口，并可以自定义关键字的返回结果。
- 2, 接着，在编写测试用例的时候，直接调用关键字来进行测试，这时就可以拿到关键字返回的结果，那么断言的时候，就可以直接对关键字返回结果进行断言。

## 编写框架及CI的总结

___

定制Allure报告：
<br>[详细教学](https://www.cnblogs.com/xiaogongjin/p/11705134.html)
<br>[环境模块配置](https://www.cnblogs.com/xwltest/p/16600306.html)
<br>[动态显示模块名和用例标题](https://blog.csdn.net/lixiaomei0623/article/details/120273737)
<br>python虚拟环境迁移报错：
<br>[pip命令-Fatal error in launcher: Unable to create process using ... 迁移虚拟环境后出错](https://blog.csdn.net/PSpiritV/article/details/122993602)
<br>jenkins配置：
<br>[jenkins报错找不到对应module](https://blog.csdn.net/u013571586/article/details/126635463)
<br>[jenkins查看的allure报告为空](https://blog.csdn.net/weixin_42051799/article/details/126426051)
```
# 需要提前配置allure环境，才可以直接使用命令行
allure serve ./report
```# PythonAutimationTest
