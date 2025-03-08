from datetime import datetime
from flask import Flask, abort, jsonify, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import PostbackEvent, TextSendMessage

app = Flask(__name__)

TOKEN = ''
SECRET = ''

line_bot_api = LineBotApi(TOKEN)
whhandler = WebhookHandler(SECRET)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message':'Hi~'})

@whhandler.add(PostbackEvent)
def handle_postback(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(event.postback)))


if __name__ == '__main__':
    app.run(debug=True)