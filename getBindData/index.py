# -*- coding: utf8 -*-
import json
from esAPI import esAPI


def main_handler(event, context):
    # print("Received event: " + json.dumps(event, indent = 2))
    # print("Received context: " + str(context))
    account = event["queryString"]["account"]
    password = event["queryString"]["password"]
    esapi = esAPI(url='http://jwxt.gcu.edu.cn', code='huananligongdaxueguangzhouxueyuan', account=account,
                  password=password)
    login_result = esapi.user_login()
    if login_result is True:
        data = {
            'schedule': esapi.get_schedule(),
            'examTime': esapi.get_exam_time(),
            'score': esapi.get_score(use_api=3),
            'info': esapi.get_info()
        }
        return {
            'status': 'ok',
            'data': data
        }
    else:
        return {
            'status': 'loginError',
            'data': login_result
        }
