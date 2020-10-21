import os

# 专门读取路径的值
# 获取到顶级目录
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试用例的路径
# test_case_path = os.path.join(project_path, "test_data", "cs.xlsx")

# 测试报告的路径
# test_report_path = os.path.join(project_path, "test_result", "html_report", "test_api.html")
# print(test_case_path)


# 截图保存的路径
screen_shot_path= os.path.join(project_path, "OutPuts", "ScreenShots")


# 保存日志的路径
test_log_path = os.path.join(project_path, "OutPuts", "logs", "test_log.txt")


# allure报告的路径
allure_report_path=os.path.join(project_path, "OutPuts", "allure_report")



