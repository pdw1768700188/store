from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread

class LoginThread(Thread):
    def __init__(self, test_file, html_file):
        super().__init__()
        self.test_file = test_file
        self.html_file = html_file

    def run(self) -> None:
        runner = HTMLTestRunner.HTMLTestRunner(
            verbosity=1,
            title='登录测试',
            description='',
            stream=open(file=self.html_file, mode='w+', encoding='utf-8')
        )

        runner.run(unittest.defaultTestLoader.discover(os.getcwd(), pattern=f'Test*.py'))




login_s = LoginThread('TestLogin1.py', '成功.html')
login_f = LoginThread('testLogin2.py', '失败.html')

login_f.start()
login_s.start()
login_s.join()
login_f.join()
'''tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR系统测试报告",
    description= "HKR系统登陆测试",
    verbosity=1,
    stream = open(file="hkr.html",mode="w+",encoding="utf-8")
)

runner.run(tests)

# 邮件发送模块'''





