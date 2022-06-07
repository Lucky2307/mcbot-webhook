import requests
from slp import StatusPing
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import json

line_bot_api = LineBotApi('znWCJmc8IYf5e71x6QyisnYnQK0OlbLff39YrrIvPQtNfXlXK0fodThYkjoPp9YNXpy31OJw3DAP7CAwH5SqPW2fH1ZFW22jy1+hfY1pEBYrF4NmY3mlYDK5kgXCoq4Vvyxz1sf8mL8ym9SZE0LZoQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dfe4f46e3907bcdd2061b1581f0f4d49')

def index(request):
    try:
        req_json = request.get_json()
        message_text = req_json['events'][0]['message']['text']
        message_replyToken = req_json['events'][0]['replyToken']
    except:
        return 'error'

    if message_text == '!mc start':
        try:
            r = requests.get(url = 'https://asia-southeast2-pekoland-server.cloudfunctions.net/start-server')
            line_bot_api.reply_message(message_replyToken, TextSendMessage('Start'))
        except:
            return 'error'

    if message_text == '!mc stop':
        try:
            r = requests.get(url = 'https://asia-southeast2-pekoland-server.cloudfunctions.net/stop-server')
            line_bot_api.reply_message(message_replyToken, TextSendMessage('Dahan gan'))
        except:
            return 'error'

    if message_text == '!mc status':
        try:
            status_online_count = StatusPing('34.87.108.231').get_status()['players']
            response = 'Online players: {}'.format(status_online_count['online'])
            if status_online_count['online'] > 0:
                for player in status_online_count['sample']:
                    response = response + '\n' + player['name']
        except:
            response = 'Server offline'
        line_bot_api.reply_message(message_replyToken, TextSendMessage(response))

    if message_text == '!mc help':
        try:
            line_bot_api.reply_message(message_replyToken, TextSendMessage('Commands: \n!mc start: Start server \n!mc stop: Stop server \n!mc status: Get server status or online players'))
        except:
            return 'error'

    return 'ok'
