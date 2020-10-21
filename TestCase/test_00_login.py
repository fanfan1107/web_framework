import pytest
from Test_Datas import login_datas as LD
from common.my_log import MyLog
import time

@pytest.mark.usefixtures('access_web')
@pytest.mark.usefixtures('refresh_page')
class TestLogin:
    @pytest.mark.parametrize('data', LD.login_wrong_data)
    def test_login_00_wrong_format(self, access_web, data):
        access_web[1].login(data['user'], data['password'])
        time.sleep(1)
        MyLog().info('获取的提示信息为{0}'.format(access_web[1].get_message_no_exist_and_wrong_user_password()))
        assert access_web[1].get_message_no_exist_and_wrong_user_password() == data['check']

    def test_login_01_success(self):
        pass
