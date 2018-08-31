
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
               "path": PATH("../yamls/myPage/myBalanceTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 我的页面检查卡券
    def test_004_myVoucher(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/myVoucherTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        self.execute(app)

    # 卡券详情页面检查
    def test_005_myVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/myVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        self.execute(app)

    # 未使用卡券详情页面检查
    def test_006_unusedVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/unusedVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        self.execute(app)
    # 已过期卡券详情页面检查
    def test_007_overTimeVoucher_detail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/overTimeVoucherDetailTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 消费记录列表检查
    def test_008_consumeRecord(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/consumeRecord.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)


    # 消费记录详情检查
    def test_009_consumeRecordDetail(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/consumeRecordDetail.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)


    # 我车辆列表--新增车辆
    def test_010_myCarAdd(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/myCarAddTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 我车辆列表
    def test_011_myCarList(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/myCarTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 我车辆列表--删除车辆-选择放弃操作
    def test_012_myCarDelCancel(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/myCarDelCancelTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 我车辆列表--删除车辆-删除成功
    def test_013_myCarDelSuccess(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/myCarDelSuccessTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 开门申请记录查询
    def test_014_myCarDel(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/openDoorApplyTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 意见反馈-新增
    def test_015_feedbackAdd(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/feedbackAddTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 意见反馈-追问
    def test_016_feedbackMore(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/feedbackMoreTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 意见反馈-删除
    def test_017_feedbackDel(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/feedbackDelTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 关于我们
    def test_018_aboutUs(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/aboutUsTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 设置-账户安全
    def test_019_settingAccountSafe(self):
        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
               "path": PATH("../yamls/myPage/settingAccountSafeTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)

    # 设置-开门设置
    def test_020_settingOpenDoor(self):
        app = {"logTest": self.logTest, "launch_app": self.launch_app, "driver": self.driver,
               "path": PATH("../yamls/myPage/settingOpenDoorTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    # 设置-开门设置
    def test_021_settingQuestion(self):
        app = {"logTest": self.logTest, "launch_app": self.launch_app, "driver": self.driver,
               "path": PATH("../yamls/myPage/settingQuestionTest.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        self.execute(app)
    @classmethod
    def setUpClass(cls):
        super(MyPageTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MyPageTest, cls).tearDownClass()
