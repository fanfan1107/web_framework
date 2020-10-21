from selenium.webdriver.common.by import By


class LoginPageLocator:
    #     用户名定位
    user_locator = (By.ID, 'username')
    #     密码定位
    password_locator = (By.ID, 'password')
    #     记住手机号定位
    remember_user_locator = (By.ID, 'chk_remember')
    #     登录按钮定位
    login_button_locator = (By.XPATH, '//input[@id="btn_login"]')

    # 用户名或密码错误/用户不存在定位提示定位
    error_login_msg_locator = (By.XPATH, '//div[@class="ant-message-custom-content ant-message-error"]/span')
    #     用户名必填提示
    emoty_user_Login = (By.XPATH, '//span[@id="username-error"]')
