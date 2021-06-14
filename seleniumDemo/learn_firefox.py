# 功能：打开Firefox浏览器，现在有报错geckodriver，还不能运行

# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Create a new instance of the Firefox driver
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

# create a new Firefox session

driver = webdriver.Firefox()
driver.implicitly_wait(10)  # 设置超时时间
driver.maximize_window()  # 窗口最大化显示

#  navigate to the application home page

driver.get("http://www.baidu.com/")

# get the search textbox

search_field = driver.find_element_by_id("kw")  # 找到输入框
search_field.clear()  # 清空当前输入内容

# enter search keyword and submit

search_field.send_keys("铜钱贯")  # 重新这是搜索关键字
search_field.submit()  # 提交进行搜索

# get all the anchor elements which have product names displayed
#  currently on result page using find_ elements_ by_ xpath method

products = driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")

# get the number of anchor elements found

print("Found " + str(len(products)) + "products:")

# iterate through each anchor element and print the text that is
#  name of the product

for product in products:
    print(product.text)

#  close the browser window

# driver.quit()
