
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.LoginPage import LoginPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginPageTest(ParametrizedTestCase):
    # 登录捷生活APP成功
    def test_loginJslifeApp(self,isCheck=True):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/loginTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        # 作为一个步骤执行时，不执行检查点
        if isCheck:
            page.checkPoint()
    # 捷生活注册校验
    def register(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/registerTest.yaml"),
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

if __name__ == '__main__':
    lpt=LoginPageTest()
    lpt.test_loginJslifeApp()

