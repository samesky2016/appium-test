import os

import sys

from Base.BaseRunner import ParametrizedTestCase
from PageObject.My.MyPage import MyPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class JsLifeAppTest(ParametrizedTestCase):

    def executor(self,app={}):

        page = MyPage(app)
        page.operate()
        page.checkPoint()

    def test_executor(self):
        folder=os.walk(PATH("../yamls"))
        for root, dirs, files in folder:
            for file in files:
                if file.startswith("test001"):
                    try:

                        testCasePath=os.path.join(root, file)

                        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
                               "path": testCasePath,
                               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
                        self.executor(app)
                        self.driver.launch_app()
                    except Exception as e:
                        print(e)
                        self.driver.launch_app()
                        continue


if __name__ == "__main__":
    js=JsLifeAppTest()
    js.test_executor()
