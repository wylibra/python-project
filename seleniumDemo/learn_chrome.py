# 功能：chrome浏览器 自动化查询 截图（不能正常运行的话看下chrome浏览器和chromedriver的版本是否一致）

# coding utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
# 获取网址
driver.get("http://www.baidu.com")
# 设置页面宽长
driver.get_window_size()  # 获取浏览器的大小
driver.set_window_size(400, 500)  # 定义指定页面长宽
driver.maximize_window()  # 最大页面长宽

time.sleep(3)
driver.find_element_by_id("kw").send_keys("自动化测试")
time.sleep(3)
# ctrl+a 全选输入框的全部内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# time.sleep(3)
# 清除输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
driver.find_element_by_id('kw').clear()
time.sleep(3)
driver.find_element_by_id('kw').send_keys('测试')
time.sleep(3)
driver.find_element_by_id('su').click()
time.sleep(5)
# 截图
driver.get_screenshot_as_file('test.png')  # 在当前脚本的同一级目录生成浏览器截屏的图片文件
# 退出浏览器
driver.quit()

# selenium 八种单数定位方式(都需要确立唯一)

# driver.find_element_by_name("wd")  # 通过name属性定位
# driver.find_element_by_id("head")  # 通过id属性定位
# driver.find_element_by_class_name("head_wrapper")  # 通过class属性定位
# driver.find_element_by_link_text("百度一下")  # 文案定位
# driver.find_element_by_partial_link_text("百")  # 包含文案定位
# driver.find_element_by_css_selector("#lg > img")  # css selector定位
# driver.find_element_by_tag_name()  # 标签名定位,如果有多个,获取的是html页面中第一个
# driver.find_element_by_xpath(".//*[@id='kw']").clear()  # xpath定位

# selenium操作浏览器

# maximize_window():浏览器窗口最大化
# minimize_window():浏览器窗口最小化
# set_window_size():设置浏览器窗口大小，（第一个参数：宽，第二个参数高）
# back():浏览器后退
# forword():浏览器前进
# refresh():刷新页面
# current_window_handle:浏览器当前选项卡（浏览器窗口）
# window_handles:浏览器打开的所有选项卡（浏览器窗口）
# switch_to_window:切换浏览器选项卡（切换浏览器窗口）
# close():关闭当前浏览器选项卡（浏览器窗口）
# quit():关闭浏览器

# selenium操作键盘

# send_keys():输入字符串
# clear():清空文本框
# send_keys(Keys.CONTROL,‘a’):全选ctrl+a
# send_keys(Keys.CONTROL,‘x’):剪切ctrl+x
# send_keys(Keys.CONTROL,‘c’):复制ctrl+c
# send_keys(Keys.CONTROL,‘v’):粘贴ctrl+v
# send_keys(Keys.ENTER):回车键：enter
# send_keys(Keys.SPACE):空格键：Space
# send_keys(Keys.BACK_SPACE):退格键：BACK_SPACE
# send_keys(Keys.ESCAPE):退出键：Esc
# send_keys(Keys.TAB):制表键：Tab
# send_keys(Keys.F1):键盘 F1
