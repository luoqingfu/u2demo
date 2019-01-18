import time
from driver import *


def driver_setup(request):
    request.instance.driver = Driver().init_driver(device_name)
    request.instance.driver.app_start(pck_name, lanuch_activity, stop=True)
    time.sleep(lanuch_time)
    allow(request.instance.driver)

    def driver_teardown():
        request.instance.driver.app_stop(pck_name)
    request.addfinalizer(driver_teardown)


def allow(driver):
    driver.watcher("允许").when(text="允许").click(text="允许")
    driver.watcher("跳过 >").when(text="跳过 >").click(text="跳过 >")
    driver.watcher("不要啦").when(text="不要啦").click(text="不要啦")