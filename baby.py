from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('hkUCqCIH7OadeaYR92b/j7g1m/rtSlhUp0HRV2hwXxY2Z5wnmsmI39RVr2InQLzujiS1ozkrNSoV7bu9kAJ3JxukEJLaFZwRE0Sg1dfM/yCz/XINVjzJnBodPgQWFGfzLFXM5XolxBbUMcTVbB8P9QdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('b41edbbd4896962a21919048f27e5c82')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']         # 取得 reply token
        msg = json_data['events'][0]['message']['text']   # 取得使用者發送的訊息
        text_message = TextSendMessage(text=msg)          # 設定回傳同樣的訊息
        line_bot_api.reply_message(tk,text_message)       # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()
