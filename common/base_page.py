# 封装基本函数--执行日志，异常处理，失败截图
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.my_log import MyLog
import datetime
from common import project_path
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, times=30, poll_frequency=0.5, doc=''):
        '''
        :param locator: 元素
        :param times:
        :param poll_frequency:
        :param doc:
        :return:
        '''
        MyLog().info("{0}等待元素{1}可见".format(doc, locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            #     结束等待时间
            end = datetime.datetime.now()
            #     求时间差
            wait_time = (end - start).seconds
            MyLog().info('{0}查找{1}元素用了{2}'.format(doc, locator, wait_time))

        except:
            MyLog().error("{0}等待元素{1}可见失败".format(doc, locator))
            #         截图
            self.save_screenshot(doc)
            raise

            # 等待元素存在

    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=''):
        MyLog().info("查找元素{0}可见".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            MyLog().error("{0}查找元素{1}可见失败".format(doc, locator))
            #  截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        #     元素操作
        MyLog().info("{0}点击元素：{1}".format(doc, locator))
        try:
            ele.click()
        except:
            MyLog().info("元素点击操作失败")
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        #    输入操作
        try:
            ele.send_keys(text)
        except:
            MyLog().info('元素输入操作失败！！！')
            self.save_screenshot(doc)
            raise

    # 获取元素文本内容
    def get_text(self, locator, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.text
        except:
            MyLog().info('获取元素内容失败！！！')
            self.save_screenshot(doc)
            raise

    # 获取元素的属性

    def get_element_attribute(self, locator, attr, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.get_attribute(attr)
        except:
            MyLog().info("获取元素的属性失败！！！")
            self.save_screenshot(doc)
            raise

    # 元素存在则为True，否则为False

    def is_eleExist(self, locator, timeout=10, doc=''):
        MyLog().info("在{0}页面中是否存在元素{1}".format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            MyLog().info("{0}秒内页面{1}存在元素{2}".format(timeout, doc, locator))
            return True
        except:
            MyLog().info("{0}秒内页面{1}不存在元素{2}".format(timeout, doc, locator))
            return False

    #  alert处理
    def alert_action(self, action='accept'):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 截图
    def save_screenshot(self, name):
        # 图片名称,模块名-页面名称_某个操作名称_时间.png
        # 当前时间

        screen_shot_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        file_path = project_path.screen_shot_path + '\\' + name + '_' + screen_shot_time + '.png'
        try:
            self.driver.save_screenshot(file_path)
        except:
            MyLog().info('{0}截图失败'.format(name))
            raise


if __name__ == '__main__':
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(type(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    picture_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    print(picture_time)
