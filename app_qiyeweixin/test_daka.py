from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDk:
    def setup_class(self):
        desire_cap = {

            "platformName": "android",
            "deviceName": "127.0.0.1:21513",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "skipDeviceInitialization": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "autoGrantPermissions": "true",
            "noReset": "True",
            "settings[waitForIdleTimeout]": 3 , #设置等待页面空闲状态
            "dontStopAppOnReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(15)

    def teardown_class(self):
        print("运行结束")
        self.driver.quit()

    @pytest.mark.daka
    def test_daka(self):
        #进入工作台tab
        wo = self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/hxj"]/android.widget.RelativeLayout[3]')
        wo_ebd = wo.is_enabled()
        print(wo_ebd)
        if wo.is_enabled() == True:
            wo.click()
        else:
            print("元素不可用，元素的值为{}".format(wo_ebd))
        # 滑动页面查找“打卡”text元素
        daka_text = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        # element_daka = self.driver.find_elements_by_xpath("//*[@class='android.widget.TextView' and @text='打卡']")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_selected(element_daka))
        # element_daka.click()

        #点击打卡按钮打卡
        dk = self.driver.find_element_by_id('com.tencent.wework:id/awr')
        dk.click()
        ase_dk = 'com.tencent.wework:id/ps'
        # print(self.driver.page_source)
        #设置元素显式等待
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,ase_dk)))

        assert str(ase_dk) in self.driver.page_source

