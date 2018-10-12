import os

from Base.BaseRunner import ParametrizedTestCase
from PageObject.JslifeApp.JslifeAppBasePage import JslifeAppPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class JsLifeAppTest(ParametrizedTestCase):

    def executor(self,app={}):

        page = JslifeAppPage(app)
        page.operate()
        page.checkPoint()

    def test_executor(self):
        folder=os.walk(PATH("../../yamls"))
        for root, dirs, files in folder:
            for file in files:
                if file.startswith("test001"):
                    self.driver.launch_app()
                    try:

                        testCasePath=os.path.join(root, file)

                        app = {"logTest": self.logTest, "launch_app":self.launch_app,"driver": self.driver,
                               "path": testCasePath,
                               "device": self.devicesName, "caseName":file.split(".")[0]}
                        self.executor(app)
                    except Exception as e:
                        print(e)
                        continue


if __name__ == "__main__":
    js=JsLifeAppTest()
    js.test_executor()
