from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.IndexPage_locators import IndexPageLocator as loc
import random
from common.base_page import BasePage


class IndexPage(BasePage):

    # 判断退出这个元素是否存在
    def isExist_logout_ele(self):
        # 如果存在返回True，如果不存在返回False
        doc = '首页_退出元素'
        try:
            self.wait_eleVisible(loc.quit_locator, doc=doc)
            return True
        except:
            return False
