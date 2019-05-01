import configparser
from imgurpython import ImgurClient
from linebot.models import *

config = configparser.ConfigParser()
config.read("config.ini")

# imgur api
client_id = config['imgur_api']['Client_ID']
client_secret = config['imgur_api']['Client_Secret']
album_id = config['imgur_api']['Album_ID']

def edu_bg():
    my_intro = '我的學歷' + '\uDBC0\uDC6C' * 2 + '\n' \
               '研究所：國立中央大學資工所' + '\n' + \
               '大學：國立中央大學' + '\n' + \
               '高中：台北市立麗山高級中學' + '\n' + \
               '目前錄取中央資工所' + '\n' + \
               '但還在等待清大資工所的備取' + '\n' \
               '需要大家幫我集氣呀！！！' + '\uDBC0\uDC91' * 3

    content = [
        TextSendMessage(my_intro),
    ]
    return content

def language():
    client = ImgurClient(client_id, client_secret)
    images = client.get_album_images(album_id)

    intro = '英文是我一直以來都有在持續學習的語言 對於聽說讀寫都有一定的信心\n' + \
            '大二時考的多益成績是810分' + '\uDBC0\uDC8D' * 2 + '\n' \
            '且因為自己的興趣 大學時曾修過基礎韓文 以下是我的多益成績單和韓文課證書' + '\uDBC0\uDC30'
    content = [TextSendMessage(intro), 
    ImageSendMessage(original_content_url=images[0].link,preview_image_url=images[0].link),
    ImageSendMessage(original_content_url=images[1].link,preview_image_url=images[1].link),
    ]

    return content

def my_profile():
    my_intro = '嗨嗨！！我是詹承翰' + '\n' + \
               '今年22歲' + '\uDBC0\uDC30' * 2 + '\n' + \
               '我平時喜歡和朋友打球運動' + '\n' + \
               '也喜歡看電影 逛街' + '\uDBC0\uDC6F' * 2 + '\n' + \
               '對寫程式有很大的興趣' + '\n' + \
               '熱愛探索自己未接觸過的領域 也喜愛學習新的技術' + '\n' + \
               '很高興你想要認識我' + '\n' + \
               '也很高興認識你哦~~' + '\uDBC0\uDC01' * 2

    content = [
        TextSendMessage(my_intro), 
    ]

    return content

def skill():
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='實作經驗',
            text='blog6109是我用Django寫的部落格' + '\n'
                 'github中也有我的其他實作作品哦~',
            thumbnail_image_url='https://imgur.com/7rSHjg4.png',
            actions=[
                URITemplateAction(
                    label='blog6109',
                    uri='https://blog6109.herokuapp.com/'
                ),
                URITemplateAction(
                    label='Alvin_zhan github',
                    uri='https://github.com/alvinzhan'
                ),
            ]
        )
    )

    content = [
        buttons_template,
    ]
    return content

def default():
    error_string = '抱歉' + '\uDBC0\uDC92' * 2 + '\n' \
                   '我還沒有新增該項資料' + '\uDBC0\uDC14' + '\n' \
                   '可以告訴我你想知道什麼哦！'

    advice = '先看看我的其他資料吧！' + '\uDBC0\uDC7A' + '\n' + \
             '可以輸入以下關鍵字：' + '\n' \
             '學歷' + '\n' + \
             '語言能力' + '\n' + \
             '自我介紹' + '\n' + \
             '專長'

    content = [
        TextSendMessage(error_string), 
        TextSendMessage(advice),
    ]

    return content
