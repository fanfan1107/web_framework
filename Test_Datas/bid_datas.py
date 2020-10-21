# 投资金额输入
bid_invest_datas = {"amount": 100}
# 请输入10的整数倍
bid_invest_no10_datas = [{'amount': 1, 'check': '请输入10的整数倍'},
                         {'amount': 111, 'check': '请输入10的整数倍'},
                         {'amount': -1, 'check': '请输入10的整数倍'}]
# 投资金额不是100倍数错误，投资为空,0
bid_invest_no100_null_0_datas = [{'amount': 0, 'check': '请正确填写投标金额'},
                                 {'amount': 10, 'check': '投标金额必须为100的倍数'},
                                 ]
