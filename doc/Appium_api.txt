Appium_API
#默认系统语言对应的Strings.xml文件内的数据。
get_app_string()
#查找某一个语言环境对应的字符串文件Strings.xml内数据
get_app_string(String language)
#按下某个键，具体哪个键由key值决定，key值定义在AndroidKeyCode类中
send_key_event(int key)
#获取当前activity,比如（.ApiDemos）
current_activity()
#根据bundleId来判断该应用是否已经安装
is_app_installed(String bundleId)
#安装app，appPath为应用的本地路径
install_app(String appPath)
#卸载app.bundleId在android中代表的是报名，而在ios中有专门的bundleId号。
remove_app(String bundleId)
#关闭应用，其实就是按home键把应用置于后台
close_app()
#启动应用
launch_app()
#先closeApp然后在launchAPP
reset_app()
#将字符数组用64位格式写到远程目录的某个文件中。也可以理解为把本地文件push到设备上。
push_file(String remotePath, byte[] base64Data)
#将设备上的文件pull到本地硬盘上
pull_file(String remotePath)
#将设备上的文件夹pull到本地硬盘上，一般远程文件为/data/local/tmp下的文件。
pull_folder(String remotePath)
#设置手机的网络连接状态，可以开关蓝牙、wifi、数据流量。通过NetworkConnectionSetting中的属性来设置各个网络连接的状态。
set_network_connect(NetworkConnectionSetting connection)
#得到当前网络的状态
get_network_connection()
#ios隐藏键盘
hide_keyboard()
#隐藏键盘，只能用于ios上。
hide_keyboard(String strategy, String keyName)
#执行一个touch动作，该touch动作是由TouchAction封装的。
perform_touchAction(TouchAction touchAction)
#点击element控件中心点按下，duration*5毫秒秒后松开，如此重复fingers次。
tap(int fingers, WebElement element, int duration)
#点击(x,y)点按下，duration*5毫秒后松开，如此重复fingers次。
tap(int fingers, int x, int y, int duration)
#从(startx,starty)滑到（endx,endy），分duration步滑，每一步用时是5毫秒。
swipe(int startx, int starty, int endx, int endy, int duration)
#2个手指操作控件，从对角线向中心点滑动。
pinch(WebElement el)
#以（x,y）为基准，计算得出（x,y-100）,(x,y+100)两个点，然后2个手指按住这两个点同时滑到（x,y）
pinch(int x, int y)
#与pinch(el)的动作刚好相反。两个手指由控件的中心点慢慢向控件的左顶点后右底点滑动。
zoom(WebElement el)
#和pinch(x,y)相反。两个手指从（x,y）点开始向（x,y-100）和（x,y+100）滑动。
zoom(int x, int y)
#锁屏多少秒后解锁
lock_screen(int seconds)
#模拟摇晃手机
shake()
#滚动到某个text属性为指定的字符串的控件
scroll_to(String text)
#滚动到某个text属性包含传入的字符串的控件
scroll_to_exact(String text)
#设置上下文
context(String name)
#可用上下文
get_context_handles()
#当前上下文
get_context()
#设置屏幕横屏或者竖屏
rotate(ScreenOrientation orientation)
#获取当前屏幕的方向
get_orientation()
#利用ios中的uiautomation中的属性来获取控件
find_element_by_ios_uiautomation(String using)
#和上面一样，不过获得的是多个控件
find_elements_by_ios_uiautomation(String using)
#利用android的uiautoamtor中的属性来获取单个控件。
find_element_by_android_uiautomator(String using)
#和上面一样，但是该方法获得是多个控件
find_elements_by_android_uiautomator(String using)
#利用accessibility id来获取单个控件
find_element_by_accessibilityid(String using)
#利用accessibility id来获得多个控件
find_elements_by_accessibilityid(String using)
'''AppiumDriver的辅助类，主要针对手势操作，比如滑动、长按、拖动等。
TouchAction的原理是讲一系列的动作放在一个链条中，然后将该链条传递给服务器。
服务器接受到该链条后，解析各个动作，逐个执行。'''
TouchAction()
#在控件上执行press操作
press(WebElement el)
#在坐标为（x,y）的点执行press操作
press(int x, int y)
#在控件el的左上角的x坐标偏移x单位，y左边偏移y单位的坐标上执行press操作。
press(WebElement el, int x, int y)
#释放操作，代表该系列动作的一个结束标志。
release()
#以el为目标，从另一个点移动到该目标上
move_to(WebElement el)
#以（x,y）点为目标，从另一个点移动到该目标上
move_to(WebElement el, int x, int y)
#在控件的中心点上敲击一下
tap(WebElement el)
#在（x,y）点轻击一下
tap(int x, int y)
#以控件el的左上角为基准，x轴向右移动x单位，y轴向下移动y单位。在该点上轻击。
tap(WebElement el, int x, int y)
#代表一个空操作，等待一段时间
wait_action()
#等待ms秒
wait_action(int ms)
#控件长按
long_press(WebElement el)
#点长按
long_press(int x, int y)
#偏移点长按
long_press(WebElement el, int x, int y)
#取消执行该动作
cancel()
#执行该动作


 Appium的辅助类，主要针对手势操作，比如滑动、长按、拖动等。针对最新版本（5.0.4）已不支持swipe等方法，所以可以用TouchAction类来封装成新的swipe方法。
1、按压控件

方法：

    press()

开始按压一个元素或坐标点（x,y）。通过手指按压手机屏幕的某个位置。

press(WebElement el, int x, int y)

press也可以接收屏幕的坐标（x,y）。

例：

    TouchAction(driver).press(x=0,y=308).release().perform()

除了press()方法之外，本例中还用到了别外两个新方法。

    release() 结束的行动取消屏幕上的指针。

    Perform() 执行的操作发送到服务器的命令操作。

2、长按控件

方法：

    longPress()

开始按压一个元素或坐标点（x,y）。 相比press()方法，longPress()多了一个入参，既然长按，得有按的时间吧。duration以毫秒为单位。1000表示按一秒钟。其用法与press()方法相同。

longPress(WebElement el, int x, int y, Duration duration)

例：

    TouchAction action = new TouchAction(driver);
    action.longPress(names.get(200),1000).perform().release();
    action.longPress(200 ,200,1000).perform().release();

3、点击控件

方法：

    tap()

对一个元素或控件执行点击操作。用法参考press()。

tap(WebElement el, int x, int y)

例：

    TouchAction action = new TouchAction(driver);
    action.tap(names.get(200)).perform().release();
    action.tap(200 ,200).perform().release();

4、移动

方法：

    moveTo()

将指针（光标）从过去指向指定的元素或点。

movTo(WebElement el, int x, int y)

其用法参考press()方法。

例：

    TouchAction action = new TouchAction(driver);
    action.moveTo(names.get(200)).perform().release();
    action.moveTo(200 ,200).perform().release();

5、暂停

方法：

    wait()

暂停脚本的执行，单位为毫秒。

action.wait(1000);