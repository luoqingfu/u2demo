import uiautomator2 as u2

from config import *


class Driver():
    def init_driver(self, device_name):
        try:
            d = u2.connect(device_name)
            d.wait_timeout = wait_timeout
            d.click_post_delay = click_post_delay
            return d
        except Exception as e:
            print('链接设备异常')

