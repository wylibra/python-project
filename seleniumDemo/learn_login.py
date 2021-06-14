# 功能：自动登录、退出系统，事件行为（点击、设置值、获取元素）

# coding utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 自动登录&自动退出
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://insight.jingdata.com/#/login")
driver.find_element_by_link_text("账号登录").click()
time.sleep(3)
driver.find_element_by_name("phoneNumber").send_keys("15510774677")
driver.find_element_by_name("password").send_keys("wang8yuan!")
time.sleep(3)
driver.find_element_by_class_name('tologin').click()
time.sleep(3)
driver.find_element_by_class_name('dialog-close').click()

# 退出
dropdown = driver.find_element_by_css_selector('.kr-avatar .el-dropdown-selfdefine')
ActionChains(driver).move_to_element(dropdown).perform()
time.sleep(2)
exitdom = driver.find_element_by_class_name('icon-v_exit')
ActionChains(driver).move_to_element(exitdom).perform()
driver.find_element_by_class_name('icon-v_exit').click()

# 再次登录
driver.find_element_by_css_selector('.kr-avatar a').click()

driver.find_element_by_link_text("账号登录").click()
time.sleep(3)
driver.find_element_by_name("phoneNumber").send_keys("15510774677")
driver.find_element_by_name("password").send_keys("wang8yuan!")
time.sleep(3)
driver.find_element_by_class_name('tologin').click()
time.sleep(3)
driver.find_element_by_class_name('dialog-close').click()

