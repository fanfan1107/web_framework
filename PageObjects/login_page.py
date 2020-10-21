import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.LoginPage_locators import LoginPageLocator as loc
from common.base_page import BasePage


class Login_Page(BasePage):

    # 登录
    def login(self, username, password,):
        doc = "登录模块"
        self.wait_eleVisible(loc.user_locator, doc=doc)
        self.input_text(loc.user_locator,username, doc)
        self.wait_eleVisible(loc.password_locator, doc=doc)
        self.input_text(loc.password_locator,password, doc)

        self.wait_eleVisible(loc.login_button_locator, doc=doc)
        self.click_element(loc.login_button_locator, doc)

    # 用户不存在和账号或密码错误提示
    def get_message_no_exist_and_wrong_user_password(self):
        doc = '获取用户不存在和账号或密码错误提示'
        self.wait_eleVisible(loc.error_login_msg_locator)
        return self.get_text(loc.error_login_msg_locator, doc=doc)

    # 用户名为空提示
    def get_emoty_user_Login_message(self):
        doc = '获取用户名为空提示'
        self.wait_eleVisible(loc.error_login_msg_locator)
        return self.get_text(loc.error_login_msg_locator, doc=doc)
