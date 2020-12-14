from esAPI import esAPI
import json

esapi = esAPI(url='http://jwxt.gcu.edu.cn',code='huananligongdaxueguangzhouxueyuan', account='201810087142', password='zs12..')
login_result = esapi.user_login()
if login_result is True:
    print(json.dumps(esapi.get_schedule()))
else:
    print(login_result)

