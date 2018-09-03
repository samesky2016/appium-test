#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import os

from Base.BaseElementEnmu import Element
from Base.BaseFile import readTemplate
from Base.BasePickle import read

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class Mailer(object):
    def __init__(self, maillist, mailtitle, mailcontent):
        self.mail_list = maillist
        self.mail_title = mailtitle
        self.mail_content = mailcontent

        self.mail_host = "smtp.qq.com"
        self.mail_user = "84028058"
        self.mail_pass = "lgvyjlhlzbrubhab"
        self.mail_postfix = "qq.com"

    @property
    def sendMail(self):

        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = 'appium测试报告'
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)

        puretext = MIMEText(str(self.mail_content),'html','utf-8')
        #puretext = MIMEText(self.mail_content)
        msg.attach(puretext)

        # jpg类型的附件
        #jpgpart = MIMEApplication(open('/home/mypan/1949777163775279642.jpg', 'rb').read())
        #jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
        #msg.attach(jpgpart)

        # 首先是xlsx类型的附件
        xlsxpart = MIMEApplication(open('../Report/'+Element.REPORT_FILE, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename=Element.REPORT_FILE)
        msg.attach(xlsxpart)

        # mp3类型的附件
        # mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
        # mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
        # msg.attach(mp3part)

        # pdf类型附件
        # part = MIMEApplication(open('foo.pdf', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        # msg.attach(part)

        try:
            s = smtplib.SMTP()  # 创建邮件服务器对象
            s.connect(self.mail_host)  # 连接到指定的smtp服务器。参数分别表示smpt主机和端口
            s.login(self.mail_user, self.mail_pass)  # 登录到你邮箱
            s.sendmail(me, self.mail_list, msg.as_string())  # 发送内容
            s.close()
            return True
        except Exception as e:
            print(str(e))
            return False
def sendEmail():

    # 读取结果数据
    sumData = read(PATH("../Log/" + Element.SUM_FILE))

    introduction = read(PATH("../Log/" + Element.DEVICES_FILE))

    #读取模板
    mail_content = readTemplate(PATH("../Report/"+Element.TEMPLATE_PATH))

    # 生成总况表
    mail_content = mail_content.replace("$versionCode", sumData["versionCode"])
    mail_content = mail_content.replace("$toatal", str(sumData["sum"]))
    mail_content = mail_content.replace("$versionName", sumData["versionName"])
    mail_content = mail_content.replace("$passTotal", str(sumData["pass"]))
    mail_content = mail_content.replace("$packingTime", sumData["packingTime"])
    mail_content = mail_content.replace("$failTotal", str(sumData["fail"]))
    mail_content = mail_content.replace("$testTime", sumData["testDate"])
    mail_content = mail_content.replace("$costTime", sumData["testSumDate"])

    # 生成每种机型用例执行情况表
    result = ""
    for item in introduction:
        result = result + "<tr><td>" + item["device"] + "</td><td>" + item["phone_name"] + "</td><td>" + str(
            item["pass"]) + "</td><td>" + str(item["fail"]) + "</td></tr>"

    mail_content = mail_content.replace("$testResult", result)
    mm = Mailer(Element.EMAILTO_LIST.split(";"), Element.EMAIL_TITLE, mail_content)
    res = mm.sendMail
    if res:
        print('--------->>邮件发送成功！')
    else:
        print('--------->>邮件发送失败！')


if __name__ == '__main__':
    # send list
    sumData = read(PATH("../Log/" + Element.SUM_FILE))

    introduction = read(PATH("../Log/" + Element.DEVICES_FILE))

    mailto_list = ["guobiao.hu@jieshun.cn"]
    mail_title = 'appium测试'
    mail_content = readTemplate(Element.TEMPLATE_PATH)

    #生成总况表
    mail_content=mail_content.replace("$versionCode",sumData["versionCode"])
    mail_content = mail_content.replace("$toatal", str(sumData["sum"]))
    mail_content = mail_content.replace("$versionName", sumData["versionName"])
    mail_content = mail_content.replace("$passTotal", str(sumData["pass"]))
    mail_content = mail_content.replace("$packingTime", sumData["packingTime"])
    mail_content = mail_content.replace("$failTotal", str(sumData["fail"]))
    mail_content = mail_content.replace("$testTime", sumData["testDate"])
    mail_content = mail_content.replace("$costTime", sumData["testSumDate"])

    #生成每种机型用例执行情况表
    result=""
    for item in introduction:
        result=result+"<tr><td>"+item["device"]+"</td><td>"+item["phone_name"]+"</td><td>"+str(item["pass"])+"</td><td>"+str(item["fail"])+"</td></tr>"

    mail_content=mail_content.replace("$testResult",result)
    mm = Mailer(mailto_list, mail_title, mail_content)
    res = mm.sendMail
    print(res)
