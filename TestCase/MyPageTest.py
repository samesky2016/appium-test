
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.My.MyPage import MyPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# noinspection PyArgumentList
class MyPageTest(ParametrizedTestCase):


    def execute(self,app={}):
        page = MyPage(app)
        page.operate()
        page.checkPoint()

    # 我的页面检查余额
    def test_003_myBalance(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test003_myBalanceTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 我的页面检查卡券
    def test_004_myVoucher(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test004_myVoucherTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        self.execute(app)

    # 卡券详情页面检查
    def test_005_myVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test005_myVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        self.execute(app)

    # 未使用卡券详情页面检查
    def test_006_unusedVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test006_unusedVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        self.execute(app)
    # 已过期卡券详情页面检查
    def test_007_overTimeVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test007_overTimeVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 消费记录列表检查
    def test_008_consumeRecord(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test008_consumeRecord.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)


    # 消费记录详情检查
    def test_009_consumeRecordDetail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test009_consumeRecordDetail.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)


    # 我车辆列表--新增车辆
    def test_010_myCarAdd(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test010_myCarAddTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 我车辆列表
    def test_011_myCarList(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test011_myCarTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 我车辆列表--删除车辆-选择放弃操作
    def test_012_myCarDelCancel(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test012_myCarDelCancelTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 我车辆列表--删除车辆-删除成功
    def test_013_myCarDelSuccess(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test013_myCarDelSuccessTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 开门申请记录查询
    def test_014_myCarDel(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test014_openDoorApplyTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 意见反馈-新增
    def test_015_feedbackAdd(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test015_feedbackAddTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 意见反馈-追问
    def test_016_feedbackMore(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test016_feedbackMoreTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 意见反馈-删除
    def test_017_feedbackDel(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test017_feedbackDelTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 关于我们
    def test_018_aboutUs(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test018_aboutUsTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 设置-账户安全
    def test_019_settingAccountSafe(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/test019_settingAccountSafeTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 设置-开门设置
    def test_020_settingOpenDoor(self):
        app = {"logTest": self.logTest, "launch_app": self.launch_app, "driver": self.driver,
               "path": PATH("../yamls/myPage/test020_settingOpenDoorTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 设置-开门设置
    def test_021_settingQuestion(self):
        app = {"logTest": self.logTest, "launch_app": self.launch_app, "driver": self.driver,
               "path": PATH("../yamls/myPage/test021_settingQuestionTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    @classmethod
    def setUpClass(cls):
        super(MyPageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MyPageTest, cls).tearDownClass()
