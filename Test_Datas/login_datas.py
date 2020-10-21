# 正常登录--测试数据
success_data = {"user": "s0025035", "password": "111111"}
# 登录异常数据--测试数据（）
login_wrong_data = [
    {"user": "s0002568977", "password": "smile123fan", "check": '用户不存在!'},
    {"user": "s0025035", "password": "smile123fan", "check": '您的用户名或密码错误'},
]
# 用户民或密码为空
phone_empty_data = [
    {"user": "", "password": "smile123fan", "check": '必填信息'},
    {"user": "18361223547", "password": "", "check": '必填信息'}
]
