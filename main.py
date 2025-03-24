from datetime import datetime
from flask import Flask, abort, jsonify, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import PostbackEvent, TextSendMessage, MessageEvent, TextMessage
from apscheduler.schedulers.background import BackgroundScheduler

import message
import requests

app = Flask(__name__)
scheduler = BackgroundScheduler()

TOKEN = 'yr0jTF4gnZtOxYpsELwA6r6YE2I5tozZlgGl9DgdpcvrjsuTgeubSgBEpmfnyCOHSFhesy3IAblcWP3grpBtKW8ogz/J109jAWU0NJXEd0dH0bkE0gr84ONdQt83gk59YvkNNe3V7s2+uqMDLYOlGAdB04t89/1O/w1cDnyilFU='
SECRET = 'ef9cdd7b06f601f2118b9b8d84786910'

line_bot_api = LineBotApi(TOKEN)
whhandler = WebhookHandler(SECRET)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message':'Hi~'})

@app.route('/callback', methods=['POST'])
def callback():
    # 確認請求來自 LINE
    signature = request.headers['X-Line-Signature']

    # 獲取請求主體
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    try:
        whhandler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@whhandler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    if "買" in event.message.text:
        line_bot_api.reply_message(event.reply_token, message.create_product_bubble_msg())
    if "加入店主" in event.message.text:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(f'{event}')))

@whhandler.add(PostbackEvent)
def handle_postback(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(f'{event.postback}')))

def call_api(url:str):
    requests.get(url)

url = 'https://helloyu-line-bot.onrender.com/api/hello'
scheduler.add_job(call_api,'interval',minutes=12,args=[url])
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)