from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('hkUCqCIH7OadeaYR92b/j7g1m/rtSlhUp0HRV2hwXxY2Z5wnmsmI39RVr2InQLzujiS1ozkrNSoV7bu9kAJ3JxukEJLaFZwRE0Sg1dfM/yCz/XINVjzJnBodPgQWFGfzLFXM5XolxBbUMcTVbB8P9QdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('b41edbbd4896962a21919048f27e5c82')

line_bot_api.push_message('U75b15c083783a40fd1f2a6dc1f9b56db', TextSendMessage(text='你可以開始了'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

 
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    baby.run(host='0.0.0.0', port=port)
