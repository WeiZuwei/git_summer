from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.maximize_window()

#-------------------------------------------------------------------------

#浏览器页面前进和后退
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//a[@href='http://news.baidu.com']").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)


#-----------------------------------------------------------------------
#tab页切换,获取各个页面的handle句柄
driver.get('http://news.baidu.com')
print driver.current_window_handle
time.sleep(1)

driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[2]/strong/a").click()
driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[3]/strong/a").click()

handles = driver.window_handles
print handles

for handle in handles:
    print handle
    print driver.current_window_handle
    if handle != driver.current_window_handle:
        print 'switch to next window', handle
        time.sleep(2)
        driver.close()
        time.sleep(2)
        driver.switch_to.window(handle)
        time.sleep(2)


#------------------------------------------------------------------------------
#iframe切换
#driver.switch_to.frame("iframe1")
#driver.switch_to.default_content()


#-----------------------------------------------------------------------------
#截图并保存
driver.get_screenshot_as_file("C:\\Users\\qabuild\\Desktop\\baidu.png")