### 1.测试框架介绍 <h3> 
本项目是以微信公众平台接口为例，基于python+Request+Pytest+parametrize驱动实现的的API接口自动化测试框架，特点如下：
* pytest结合allur-pyteste生成allure测试报告
* parametrize结合yaml实现数据驱动
* 封装yaml文件的读写，实现接口串联
### 2.测试目录结构介绍 <h3> 
* common/: 工具类包括request方法封装、yaml文件读写
* testcase/: 测试用例、测试接口数据文件
* temp/: 测试报告临时文件
* report/: allure测试报告
* all.py: 执行所有测试用例的主程序
* conftest.py 全局用例共享文件
* extract.yaml  token提取存储文件
* pytest.ini  pytest配置文件
