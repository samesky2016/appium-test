
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
    def _003_myBalance(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver, "path": PATH("../yamls/myPage/myBalanceTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        page = MyPage(app)
        page.operate()
        page.checkPoint()
    # 我的页面检查卡券
    def _004_myVoucher(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver, "path": PATH("../yamls/myPage/myVoucherTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = MyPage(app)
        page.operate()
        page.checkPoint()

    # 卡券详情页面检查
    def _005_myVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver, "path": PATH("../yamls/myPage/myVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = MyPage(app)
        page.operate()
        page.checkPoint()

    # 未使用卡券详情页面检查
    def _006_UnusedVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver, "path": PATH("../yamls/myPage/unusedVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = MyPage(app)
        page.operate()
        page.checkPoint()
    # 已过期卡券详情页面检查
    def _007_OverTimeVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver, "path": PATH("../yamls/myPage/overTimeVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = MyPage(app)
        page.operate()
        page.checkPoint()
    # 已过期卡券详情页面检查
    def test_008_ConsumeRecord(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver, "path": PATH("../yamls/myPage/consumeRecord.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = MyPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(MyPageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MyPageTest, cls).tearDownClass()
