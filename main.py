from datetime import datetime
from flask import Flask, abort, jsonify, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import PostbackEvent, TextSendMessage

app = Flask(__name__)

TOKEN = 'yr0jTF4gnZtOxYpsELwA6r6YE2I5tozZlgGl9DgdpcvrjsuTgeubSgBEpmfnyCOHSFhesy3IAblcWP3grpBtKW8ogz/J109jAWU0NJXEd0dH0bkE0gr84ONdQt83gk59YvkNNe3V7s2+uqMDLYOlGAdB04t89/1O/w1cDnyilFU='
SECRET = 'ef9cdd7b06f601f2118b9b8d84786910'

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