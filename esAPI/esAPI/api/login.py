from requests import RequestException, TooManyRedirects
from esAPI.check_code import CHECK_CODE
from esAPI.utils import to_binary, to_text, get_alert_tip, get_view_state_from_html
from esAPI.exceptions import IdentityException, CheckCodeException, LoginException, \
    OtherException


class Login:
    """ 登录模块 """

    def __init__(self, config, user, request):
        self.config = config
        self.user = user
        self.Request = request

    def get_login(self, **kwargs):
        """
        登录入口 与 异常处理
        """
        args = (self.config['login_url'], self.config['exist_verify'])
        try:
            res = self._get_api(*args, **kwargs)
        except OtherException as e:
            raise LoginException(self.config['code'], to_text(str(e)))
        except RequestException:
            if self.config['use_proxy']:
                raise LoginException(self.config['code'], '教务系统外网异常，使用代理登录失败：RequestException')
            else:
                raise LoginException(self.config['code'], '教务系统外网异常：RequestException')

        # 处理登录结果
        try:
            self._handle_login_result(res)
        except CheckCodeException:
            # 处理验证码失败后多次尝试
            for i in range(5):
                try:
                    # 验证码错误时，再次登录
                    res = self._get_api(*args, **kwargs)
                except RequestException:
                    raise LoginException(self.config['code'], '接口请求失败1：RequestException')
                else:
                    try:
                        self._handle_login_result(res)
                    except CheckCodeException:
                        # 验证码错误情况，继续尝试
                        pass
                    else:
                        # 其他情况则跳出循环
                        break
        return True

    def _handle_login_result(self, res):
        """
        处理页面弹框信息
        """
        if res is True:
            # 登录成功
            return
        tip = get_alert_tip(res.text)
        if tip:
            if tip == '验证码不正确！！':
                raise CheckCodeException(self.config['code'], tip)
            raise IdentityException(self.config['code'], tip)
        raise LoginException(self.config['code'], '教务系统接口请求异常')

    def _get_login_payload(self, login_url, **kwargs):
        """
        获取登录页面的 请求参数
        """
        try:
            kwargs['timeout'] = 3
            res = self.Request.get(login_url, **kwargs)
        except RequestException:

            # 首次请求可能出现 Connection aborted
            res = self.Request.get(login_url, **kwargs)

        url_info = res.url.split(login_url)[0].split('/(')
        if len(url_info) == 2:
            self.Request.update_url_token('/(' + url_info[1])

        view_state = get_view_state_from_html(res.text)
        return {'__VIEWSTATE': view_state}

    def _get_api(self, login_url, exist_verify, **kwargs):
        """
        登录请求
        """
        code = ''
        login_payload = self._get_login_payload(login_url, **kwargs)
        if exist_verify:
            res = self.Request.get('/CheckCode.aspx')
            if res.content[:7] != to_binary('GIF89aH'):
                raise CheckCodeException(self.config['code'], "验证码获取失败")
            code = CHECK_CODE.verify(res.content)

        account = self.user['account'].encode('gb2312')
        payload = {
            'txtUserName': account,
            'TextBox1': account,
            'TextBox2': self.user['password'],
            'TextBox3': code,
            'txtSecretCode': code,
            'RadioButtonList1': '学生'.encode('gb2312'),
            'Button1': ' 登 录 '.encode('gb2312')
        }
        payload.update(login_payload)
        try:
            res = self.Request.post(login_url, data=payload, **kwargs)
        except TooManyRedirects:
            # 302跳转 代表登录成功
            return True
        return res
