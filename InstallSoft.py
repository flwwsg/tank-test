# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {"platformName": "Android", "deviceName": "127.0.0.1:5555", "app": "D:\\aPackage\\app-release (90).apk"}
# caps["noRest"] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# TouchAction(driver).press(x=939, y=956).perform()
time.sleep(1)
TouchAction(driver).press(x=938, y=956).move_to(x=259, y=956).release().perform()
TouchAction(driver).press(x=938, y=956).move_to(x=238, y=956).release().perform()
TouchAction(driver).press(x=981, y=956).move_to(x=210, y=956).release().perform()
TouchAction(driver).press(x=984, y=956).move_to(x=259, y=956).release().perform()
TouchAction(driver).press(x=984, y=956).move_to(x=259, y=956).release().perform()
TouchAction(driver).tap(x=568, y=1616).perform()
TouchAction(driver).tap(x=959, y=1847).perform()
TouchAction(driver).tap(x=565, y=597).perform()
TouchAction(driver).tap(x=153, y=895).perform()
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText")
el1.send_keys("13072374137")
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText")
el2.send_keys("123456aa")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.widget.EditText")
el3.send_keys("1111")
TouchAction(driver).tap(x=998, y=1569).perform()
TouchAction(driver).tap(x=705, y=1529).perform()
TouchAction(driver).tap(x=668, y=1535).perform()
TouchAction(driver).tap(x=696, y=1844).perform()
TouchAction(driver).tap(x=647, y=1069).perform()
TouchAction(driver).tap(x=426, y=558).perform()
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText")
el4.send_keys("100")
TouchAction(driver).tap(x=791, y=1273).perform()
TouchAction(driver).press(x=816, y=1689).move_to(x=824, y=1459).release().perform()
TouchAction(driver).tap(x=1002, y=1151).perform()
TouchAction(driver).press(x=891, y=1459).move_to(x=854, y=724).release().perform()
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[22]/android.widget.Image")
# driver.implicitly_wait(4)
el1.click()
time.sleep(4)
TouchAction(driver).tap(x=564, y=1581).perform()
time.sleep(0.5)
TouchAction(driver).tap(x=672, y=1752).perform()

el6 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText")
el6.send_keys("000000")
