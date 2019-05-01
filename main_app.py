# python libraries
import configparser
from flask import Flask, request, abort
import random

# Line libraries

from linebot import (
    LineBotApi, WebhookHandler
    )
from linebot.exceptions import (
    InvalidSignatureError
    )
from linebot.models import *

# my own files
import myprofiles

app = Flask(__name__)

config = configparser.ConfigParser()
config.read("config.ini")

Channel_access_token = config['line_bot']['Channel_Access_Token']
Channel_secret = config['line_bot']['Channel_Secret']

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.message.text:", event.message.text)

    text_message = {
        '學歷': myprofiles.edu_bg, 
        '語言能力': myprofiles.language, 
        '自我介紹': myprofiles.my_profile, 
        '專長': myprofiles.skill, 
        'default': myprofiles.default,

        }

    content = text_message.get(event.message.text, text_message['default'])()

    line_bot_api.reply_message(
        event.reply_token,
        content,
    )

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):

    package_ids = [11537, 11538, 11539]

    package_index = random.randint(0, len(package_ids) - 1)
    package_id = str(package_ids[package_index])

    sticker_ids = [
        [52002734, 52002735, 52002736, 52002738, 52002739, 52002745, 52002748, 52002752, 52002761, 52002768, ],   # package 11537
        [51626494, 51626496, 51626497, 51626498, 51626499, 51626501, 51626503, 51626507, 51626508, 51626520, 51626521, 51626532, ],    # package 11538
        [52114110, 52114114, 52114115, 52114116, 52114117, 52114118, 52114122, 52114124, 52114125, 52114131, ],    # package 11539
        ]
    
    sticker_index = random.randint(0, len(sticker_ids[package_index]) - 1)
    sticker_id = str(sticker_ids[package_index][sticker_index])   # sticker_ids[which_package][which_sticker]

    sticker_message = StickerSendMessage(
        package_id = package_id,
        sticker_id = sticker_id,
    )

    line_bot_api.reply_message(
        event.reply_token,
        sticker_message)


if __name__ == "__main__":
    app.run()


