
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.My.MyPage import MyPage
from TestCase.LoginPageTest import LoginPageTest
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# noinspection PyArgumentList
class MyPageTest(ParametrizedTestCase):
    # 我的页面检查余额
    def test_myBalance(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/myBalanceTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = MyPage(app)
        page.operate()
        page.checkPoint()
    # 我的页面检查卡券
    def myVoucher(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/registerTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = MyPage(app)
        page.operate()
        page.checkPoint()


    @classmethod
    def setUpClass(cls):
        #loginPageTest=LoginPageTest()
        LoginPageTest.test_loginJslifeApp(ParametrizedTestCase)
        super(MyPageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MyPageTest, cls).tearDownClass()