from esAPI import esAPI

esapi = esAPI(url='http://jwxt.gcu.edu.cn',code='huananligongdaxueguangzhouxueyuan', account='201810098161', password='wwd123456')
login_result = esapi.user_login()
if login_result is True:
    print(esapi.get_score(use_api=3))
else:
    print(login_result)

