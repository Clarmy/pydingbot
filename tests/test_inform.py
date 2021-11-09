from unittest.mock import patch
from pydingbot import inform

FAKE_CONFIG = {
        'default':
            {
                'webhook': 'https://oapi.dingtalk.com/robot/send?access_token=170d919d864e90502b48603ecbcd7646701bd66cc590f495bac1b7c5049e171e',
                'secret': 'SEC474937571de1506cdd724af0d5866f4fa2788968032a2d6d982da988bea4e5de'
            }
    }

@patch('pydingbot.main.Dingbot')
def test_inform(mock_dingbot):
    dingbot = mock_dingbot.return_value
    dingbot.send_msg.return_value = '{"errcode":0,"errmsg":"ok"}'
    resp = inform(**FAKE_CONFIG['default'])

    assert resp == '{"errcode":0,"errmsg":"ok"}'
