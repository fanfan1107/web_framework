import pytest
from common import project_path
if __name__ == '__main__':
    # pytest.main(["-m", "smoke", "-s", "-q", "--alluredir=./allurereport"])
    # pytest.main(["-s", "-q", "--alluredir=./allurereport"])
    pytest.main(["-s", "-q", "--alluredir=./OutPuts/allure_report"])