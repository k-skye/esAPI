from esAPI import esAPI

esapi = esAPI(url='http://jwxt.gcu.edu.cn',code='huananligongdaxueguangzhouxueyuan', account='201810096022', password='xiaokang123.')
login_result = esapi.user_login()
if login_result is True:
    print(esapi.get_score(use_api=3))
else:
    print(login_result)

