import allure
import pytest
import uiautomator2 as u2

from page_obj.login import Login

d = u2.connect('emulator-5554')
#@pytest.mark.usefixtures('driver_setup')
@allure.feature('测试登录功能')
class TestLogin(Login):
    def setup(self):
        d.app_start('com.netease.cloudmusic')
        #sess = d.session('com.netease.cloudmusic')
    def teardown(self):
        d.app_stop('com.netease.cloudmusic')

    # @pytest.fixture()
    # def init(self, scope="function"):
    #     self.login = Login(self.driver)
    #     yield self.login
    @allure.story('登录')
    @pytest.mark.P0
    def test_login(self):
        #self.d.wait_activity(".ApiDemos", timeout=10)
        # self.login()
        #output = self.d.shell("pwd").output
        #print(output)
        # sleep(2)
        #m_activity = self.d.current_app()
        #assert m_activity['activity'] == 'com.netease.cloudmusic.activity.MainActivity'
        Login.login(self)


if __name__ == '__main__':
    pytest.main('-s', 'test_login.py')
