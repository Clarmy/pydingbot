import os
import time
import json
from unittest.mock import patch

from pydingbot import Dingbot

FAKE_CONFIG = {
        'default':
            {
                'webhook': 'https://oapi.dingtalk.com/robot/send?access_token=170d919d864e90502b48603ecbcd7646701bd66cc590f495bac1b7c5049e171e',
                'secret': 'SEC474937571de1506cdd724af0d5866f4fa2788968032a2d6d982da988bea4e5de'
            }
    }

@patch('time.time')
def test_sign_and_url(time):
    time.return_value = 1606483586.285
    dingbot = Dingbot(**FAKE_CONFIG['default'])
    dingbot.sign
    assert dingbot.signstring == 'WASfxzMjtdLTN6f0asAt4qLnI5w8xXM1EtOGHY1J1xU%3D'
    assert dingbot.url == 'https://oapi.dingtalk.com/robot/send?access_token=170d919d864e90502b48603ecbcd7646701bd66cc590f495bac1b7c5049e171e&timestamp=1606483586285&sign=WASfxzMjtdLTN6f0asAt4qLnI5w8xXM1EtOGHY1J1xU%3D'
    assert dingbot.timestamp == str(1606483586285)
