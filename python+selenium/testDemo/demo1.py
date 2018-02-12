from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
try:
    driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
    driver.find_element_by_xpath("//input[@id='su']").click()
except Exception as e:
    print ("Exception found: ", format(e))


time.sleep(2)

isTrue = driver.find_element_by_xpath("//a[contains(text(), '- Web Browser Automation')]").is_displayed()
assert isTrue

#get browser version
print ("browser version: ", driver.capabilities)
print ("browser version: ", driver.capabilities['browserVersion'])

#open a new tab in the browser, press CTRL+t will open a new tab, so here we will send "Ctrl+t"
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + '\t')

#browser size
print (driver.get_window_size())
driver.set_window_size(1024,768)

time.sleep(5)
driver.quit()
