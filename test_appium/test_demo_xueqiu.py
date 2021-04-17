from appium import webdriver
desired_cap = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": " com.xueqiu.android.common.MainActivity",
  "noReset": True,
  "dontStopAppOnReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(20)
# el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
# el1.click()
# el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
# el2.send_keys("alibaba")
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
# el3.click()
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[1]")
# el4.click()

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
driver.back()
driver.quit()