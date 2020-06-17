import requests
import urllib
from flask_babel import _
from app import app
from hashlib import md5
from random import randint
import json


def translate(text, source_language, dest_language):
    baidu_trans_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    appid = app.config.get('BAIDU_TRANS_APP_ID')
    secret_key = app.config.get('BAIDU_TRANS_SECRET_KEY')

    if not appid or not secret_key:
        return _('Error: the translation service is not configured.')

    salt = randint(32768, 65536)
    sign = appid + text + str(salt) + secret_key
    sign = md5(sign.encode()).hexdigest()
    api = '{}?appid={}&q={}&from={}&to={}&salt={}&sign={}'.format(baidu_trans_url, appid, urllib.parse.quote(text),
                                                                source_language, dest_language, salt, sign)
    try:
        response = requests.get(api)
        if response.status_code != 200:
            return _('Error: the translation service failed.')
        res = json.loads(response.content.decode('utf-8'))
        if res.get('error_code'):
            return _('Error: can not access the translation service.')
        return res.get('trans_result')[0].get('dst')
    except Exception as e:
        return _('Error: the translation service failed.')
        app.logger.error(e)
