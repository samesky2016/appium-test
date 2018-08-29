
class Element(object):

    # 常用操作关键字
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    INDEX = "index"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    CLICK = "click"
    TAP = "tap"
    ACCESSIBILITY = "accessibility"
    ADB_TAP = "adb_tap"
    SWIPE_DOWN = "swipe_down"
    SWIPE_UP = "swipe_up"
    SWIPE_LEFT = "swipe_left"
    SET_VALUE = "set_value"
    GET_VALUE = "get_value"
    LONG_PRESS = "long_press"
    #查找元素的超时时间
    WAIT_TIME = 20
    #查找元素时的轮训时间，默认是0.5秒，容易报找不到元素的错误。
    POLL_FREQUENCY=0.1
    PRESS_KEY_CODE = "press_keycode"

    GET_CONTENT_DESC = "get_content_desc"

    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"

    # 检查点
    CONTRARY = "contrary"  # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval"  # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check"  # 默认检查点，就是查找页面元素
    COMPARE = "compare"  # 历史数据和实际数据对比
    TOAST = "toast"


    RE_CONNECT = 1 # 是否打开失败后再次运行一次用例

    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"
