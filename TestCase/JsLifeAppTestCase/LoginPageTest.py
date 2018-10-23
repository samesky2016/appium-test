
import os
import sys

from Base.BaseRunner import ParametrizedTestCase
from PageObject.JslifeApp.Home.LoginPage import LoginPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginPageTest(ParametrizedTestCase):
    def execute(self,app={}):
        page = LoginPage(app)
        page.operate()
        page.checkPoint()

    # 登录捷生活APP成功
    def test_001_loginJslifeApp(self,isCheck=True):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver, "path": PATH("../../yamls/jsLifeAppYaml/01_home/test001_loginTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 捷生活注册校验
    def test_002_register(self):
        app = {"logTest": self.logTest,"launch_app":self.launch_app, "driver": self.driver, "path": PATH("../../yamls/jsLifeAppYaml/01_home/test002_registerTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        self.execute(app)


    @classmethod
    def setUpClass(cls):
        super(LoginPageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginPageTest, cls).tearDownClass()

if __name__ == '__main__':
    lpt=LoginPageTest()
    lpt.test_loginJslifeApp()

