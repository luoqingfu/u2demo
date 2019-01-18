import os
import subprocess

import pytest


def init_env():
    cmd = "python -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    print('初始化运行环境')

def init_report():
    cmd = "allure generate --clean data -o reports"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    print("报告地址:{}".format(report_path))


init_env()
pytest.main(["-s", "--reruns=2", "android/testcase","--alluredir=data"])
init_report()
