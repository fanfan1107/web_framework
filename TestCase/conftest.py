import pytest
from selenium import webdriver
from Test_Datas import Common_Data as CD
from PageObjects.login_page import Login_Page
from common.my_log import MyLog
from Test_Datas import login_datas as LD
from PageObjects.index_page import IndexPage

driver = None


# 申明它是一个fixture
@pytest.fixture(scope='class')
def access_web():
    global driver
    # 前置操作
    MyLog().info('-----所用用例之前的，setup---整个测试类只执行一次')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.login_url)
    lg = Login_Page(driver)
    yield (driver, lg)  # 分割线，后面接返回值，fixture的函数名称用来接收他的返回值

    # 后置操作
    print('---使用用例之后的，teardown--整个测试类只执行一次')
    driver.quit()


@pytest.fixture()
def refresh_page():
    global driver
    # 前置操作
    yield
    driver.refresh()


# @pytest.fixture(scope='class')
# def access_web_invest():
#     global driver
#     #     前置操做
#     MyLog().info('----所有用例前置----')
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(CD.login_url)
#     lg = Login_Page(driver)
#     lg.login(LD.success_data['user'], LD.success_data["password"])
#     BP = Bidpage(driver)
#     # 选择一个标
#     IndexPage(driver).click_first_bid()
#     yield (driver, BP)
#     # 后置操作
#     MyLog().info('---所有用例执行完成后，关闭-----')
#     driver.quit()
