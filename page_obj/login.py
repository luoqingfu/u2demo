import allure
import uiautomator2 as u2

from common.base import Base

setting = 'com.netease.cloudmusic:id/q6'
login = 'com.netease.cloudmusic:id/q6'
login_phone = 'com.netease.cloudmusic:id/acb'
em = 'com.netease.cloudmusic:id/q1'
phone_input = 'com.netease.cloudmusic:id/i9'
phone_input_c = '13226349780'
pwd_input = 'com.netease.cloudmusic:id/i7'
longin_btn = 'com.netease.cloudmusic:id/q1'


class Login(Base):

    def __init__(self, driver):
        self.base = Base(driver)

    @allure.story('登录操作')
    def login(self):

        # d = u2.connect('emulator-5554')
        # #d.app_install(
        #     #'https://imtt.dd.qq.com/16891/7E569C80A3714D58E77F6173EB8F6329.apk?fsname=com.netease.cloudmusic_5.7.2_130.apk&csr=1bbd')
        # d(resourceId='com.netease.cloudmusic:id/q6').wait(timeout=5)
        # d(resourceId='com.netease.cloudmusic:id/q6').click_exists(timeout=3)
        # d(resourceId='com.netease.cloudmusic:id/acb').click_exists(timeout=3)
        # d(resourceId="com.netease.cloudmusic:id/q1").click_exists(timeout=3)
        # d(resourceId="com.netease.cloudmusic:id/i9").set_text("13226349780")
        # d(resourceId="com.netease.cloudmusic:id/i7").set_text("*********")
        # d(resourceId='com.netease.cloudmusic:id/q1').click_exists(timeout=3)
        self.base.click(setting)
        self.base.click(login)
        self.base.click(login_phone)
        self.base.send_keys(phone_input, phone_input_c)



