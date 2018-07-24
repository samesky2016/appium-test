
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.LoginPage import LoginPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginPageTest(ParametrizedTestCase):
    # 登录捷生活APP
    # unittest框架，测试用例首单词必须以test开头
    def testLoginJslifeApp(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/loginTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        page.checkPoint()



    @classmethod
    def setUpClass(cls):
        super(LoginPageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginPageTest, cls).tearDownClass()
