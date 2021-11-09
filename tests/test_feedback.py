import time
from unittest.mock import patch
from pydingbot import feedback

FAKE_CONFIG = {
        'default':
            {
                'webhook': 'https://oapi.dingtalk.com/robot/send?access_token=170d919d864e90502b48603ecbcd7646701bd66cc590f495bac1b7c5049e171e',
                'secret': 'SEC474937571de1506cdd724af0d5866f4fa2788968032a2d6d982da988bea4e5de'
            }
    }

@patch('pydingbot.main.Dingbot')
def test_feedback_normal(mock_dingbot):
    dingbot = mock_dingbot.return_value
    dingbot.send_msg.return_value = '{"errcode":0,"errmsg":"ok"}'

    @feedback(**FAKE_CONFIG['default'])
    def some_task_normal():
        time.sleep(2)

    assert some_task_normal() == ('{"errcode":0,"errmsg":"ok"}',
                                  '{"errcode":0,"errmsg":"ok"}')


@patch('pydingbot.main.Dingbot')
def test_feedback_failed(mock_dingbot):
    dingbot = mock_dingbot.return_value
    dingbot.send_msg.return_value = '{"errcode":0,"errmsg":"ok"}'

    @feedback(**FAKE_CONFIG['default'])
    def some_task_failed():
        time.sleep(2)
        1 / 0

    assert some_task_failed() == ('{"errcode":0,"errmsg":"ok"}',
                                    '{"errcode":0,"errmsg":"ok"}',
                                    'ZeroDivisionError: division by zero')
