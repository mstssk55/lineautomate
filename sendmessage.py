from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os
from dotenv import load_dotenv
load_dotenv('.env') 
LINE_TOKEN = os.environ.get("LINE_TOKEN")
SEND = os.environ.get("SEND")

line_bot_api = LineBotApi(LINE_TOKEN)

try:
    line_bot_api.push_message(SEND, TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle
    print("失敗")
    