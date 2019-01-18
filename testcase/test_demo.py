import uiautomator2 as u2
import pytest
import allure
@allure.feature("测试首页")#类的主要测试部分
#@allure.environment(app_package='com.mobile.fm')# 具体Environment参数可自行设置
# @allure.environment(app_activity='com.mobile.fm.activity')
# @allure.environment(device_name='aad464')
# @allure.environment(platform_name='Android')



class TestInfo():
    '''
    Allure中对严重级别的定义：
    1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
    2、 Critical级别：临界缺陷（ 功能点缺失）
    3、 Normal级别：普通缺陷（数值计算错误）
    4、 Minor级别：次要缺陷（界面错误与UI需求不符）
    5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范
    '''

    @allure.story('测试是否可以获取信息')  # 分支功能
    @allure.severity('blocker')
    @allure.step('')
    @allure.issue('www.baidu.com')
    @allure.testcase('www.baidu.com')



    def test_info(self):
        """
        我是一个用例描述，这个用例是用来获取Android信息的
        """
        d = u2.connect('emulator-5554')
        print(d.info)
        #d.app_install('https://imtt.dd.qq.com/16891/7E569C80A3714D58E77F6173EB8F6329.apk?fsname=com.netease.cloudmusic_5.7.2_130.apk&csr=1bbd')

    @allure.step("字符串相加：{0}，{1}")
    # 测试步骤，可通过format机制自动获取函数参数
    def str_add(str1, str2):
        if not isinstance(str1, str):
            return "%s is not a string" % str1
        if not isinstance(str2, str):
            return "%s is not a string" % str2
        return str1 + str2


    @allure.story('test_story_01')
    @allure.severity('blocker')
    def test_case(self):
        str1 = 'hello'
        str2 = 'world'
        assert self.str_add(str1, str2) == 'helloworld'
    #在报告中增加附件：allure.attach(’arg1’,’arg2’,’arg3’)：
    #file = open('../testfile/image/lqf.fpg', 'rb').read()
    #allure.attach('test_img', file, allure.attach_type.PNG)




if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '../report/xml'])

