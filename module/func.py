from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage,StickerSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn, QuickReply, QuickReplyButton, MessageAction

from linebot import  WebhookParser
import pymysql

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
#https://raw.githubusercontent.com/juice-kuo/super3000/master/static/images/TemplateSendMessage/
#http://120.125.72.233/~survey/static_images/
baseurl = 'https://raw.githubusercontent.com/juice-kuo/super3000/master/static/images/TemplateSendMessage/'
#'https://i.imgur.com/qUCe1UF.png'  baseurl + 'asisline.png'
def sendButton(event):  #關於我們
    
        message = TemplateSendMessage(
            alt_text='關於我們',
            template=ButtonsTemplate(
                thumbnail_image_url=baseurl + 'asisline.png',  #顯示的圖片
                title='關於我們',  #主標題
                text='請選擇：',  #副標題
                actions=[
                    URITemplateAction(  #開啟網頁
                        label='銘傳大學網站',
                        uri='https://web.mcu.edu.tw/'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='應用統計與資料科學學系網站',
                        uri='http://web.asis.mcu.edu.tw/zh-hant'
                    ),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
def sendCarousel0(event):  #應用統計與資料科學學系網站
    
        message = [
            TextSendMessage(
                text = '應用統計與資料科學學系網站'
            ),
            TextSendMessage(
                text = 'http://web.asis.mcu.edu.tw/zh-hant'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
		
def sendCarousel1(event):  #董監事持股資訊
    
        message = [
            TextSendMessage(
                text = '董監事持股資訊 --- 提供查詢 : 企業董監事之持股'
            ),
            TextSendMessage(
                text = 'https://asisproject.herokuapp.com/select_list/'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
		
def sendCarousel2(event):  #PM2.5
    
        message = [
            TextSendMessage(
                text = 'PM2.5 資訊平台 --- 提供查詢 : 桃園地區PM2.5的10年資訊(2006~2016) & 預測模型'
            ),
            TextSendMessage(
                text = 'http://web.asisrlab.mcu.edu.tw:3838/survey/Taopm25/'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
		
def sendCarousel3(event):  #台灣證券即時資訊
    
        message = [
            TextSendMessage(
                text = '台灣證券即時資訊 --- 提供查詢 : 台灣證券市場的即時資訊 & 技術指標 & 智慧選股'
            ),
            TextSendMessage(
                text = 'https://reurl.cc/5ogAKv'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
		
def sendCarousel4(event):  #台灣加權指數
    
        message = [
            TextSendMessage(
                text = '台灣加權指數 建模平台 --- 提供選擇API參數 建構各種預測模型 (1990—2018)'
            ),
            TextSendMessage(
                text = 'http://web.asisrlab.mcu.edu.tw:3838/survey/twindex/'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
		
def sendCarousel5(event):  #消費者物價指數
    
        message = [
            TextSendMessage(
                text = '消費者物價指數  建模平台 --- 提供選擇API參數 建構各種預測模型 (1990—2018)'
            ),
            TextSendMessage(
                text = 'http://web.asisrlab.mcu.edu.tw:3838/survey/cpi/'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
		

    
def sendImgCarousel(event):  #金融相關網站
    
        message = TemplateSendMessage(
            alt_text='金融相關網站',
            template=ButtonsTemplate(
                thumbnail_image_url=baseurl + '金管會.png',  #顯示的圖片
                title='金融相關網站',  #主標題
                text='請選擇：',  #副標題
                actions=[
                    URITemplateAction(  #開啟網頁
                        label='金管會',
                        uri='https://www.fsc.gov.tw/ch/index.jsp'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='證券期貨局',
                        uri='https://www.sfb.gov.tw/ch/home.jsp?id=882&parentpath=0,8'
                    ),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    
def sendPizza(event):

        message = TextSendMessage(
            text='請選擇想查詢之商業司相關網站',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="商工行政服務相關網站入口網", text="https://gcis.nat.gov.tw/mainNew/index.jsp")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="商工登記公示資料查詢服務", text="https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="縣市別與近十年度公司設立登記案件統計", text="https://serv.gcis.nat.gov.tw/StatisticQry/cmpy/StaticFunction4.jsp")
                    ),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

def sendUse(event):  #@統資系常見問題
    try:
        message = TextSendMessage(
            text = '''這是統資系的介紹，請輸入關於統資系相關問題主題。
例如 : 多元入學、應用統計與資料科學學系、統資系、資料科學、課程、特色、大數據
               ''',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="多元入學", text="多元入學")),
                                   QuickReplyButton(action=MessageAction(label="領域", text="領域")),
                                   QuickReplyButton(action=MessageAction(label="統資系", text="統資系")),
                                   QuickReplyButton(action=MessageAction(label="社團", text="社團")),
                                   QuickReplyButton(action=MessageAction(label="畢業", text="畢業")),
                                   QuickReplyButton(action=MessageAction(label="資料科學", text="資料科學")),
                                   QuickReplyButton(action=MessageAction(label="就業", text="就業")),
                                   QuickReplyButton(action=MessageAction(label="系學會", text="系學會")),
                                   QuickReplyButton(action=MessageAction(label="工作出路", text="工作出路")),
                                   QuickReplyButton(action=MessageAction(label="課程", text="課程")),
                                   QuickReplyButton(action=MessageAction(label="特色", text="特色")),
                                   QuickReplyButton(action=MessageAction(label="應用統計與資料科學學系", text="應用統計與資料科學學系")),
                                   QuickReplyButton(action=MessageAction(label="大數據", text="大數據")),
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendQnA(event, mtext):  #QnA
    que1={'@BIG DATA':'',
          '@STAT':'',
          '@就業工業統計':'',
          '@就業商業統計':'',
          '@就業生物統計':'',
          '@就業資料科學':'',
          '@就業教育類型':'',
          '@程式設計':'',
          '@抽樣方法':'',
          '@迴歸分析':'',
          '@類別資料分析':'',
          '@財務報表分析':'',
          '@多變量分析':'',
          '@實驗設計':'',
          '@統計資料庫':'',
          '@雲端分散式程式設計':'',
          '@資料科學概論':'',
          '@資料探勘':'',
          '@統計套裝軟體':'',
          '@探索性資料分析與視覺化':'',
          '@關於我們':'',
          '@AI統資':'',
          '@就業連結':'',
          '@課程簡介':''
          }
    keys1 = que1.keys()	
    try:
        conn = pymysql.connect(host='120.125.72.233',user='survey',passwd='survey',db='survey',charset='utf8')
        cur = conn.cursor()
        sql_1="SELECT * FROM `consultapi_asisqa` WHERE `quenstion` LIKE '%" + mtext + "%'"
        if cur.execute(sql_1) != 0:
            a=cur.fetchall() 
            text1 = "關於"+mtext+"的相關提問&答覆如下：\n"
            for i in range(0,cur.execute(sql_1)):
                text1 += "\n 【提問】>>>> \n" + a[i][2] + "\n"
                text1 += "\n 【答覆】>>>>> \n" + a[i][3]+ "\n"
            message=[
                StickerSendMessage(
                    package_id='1',
                    sticker_id='2'
                ),
                TextSendMessage(text=text1)
            ]
            conn.close()
            line_bot_api.reply_message(event.reply_token, message)
        elif mtext in keys1:
            message = TextSendMessage(
				text = ''
            )
        else:
            message = TextSendMessage(
                text = '很抱歉，資料庫中無適當解答！\n請再輸入問題。'
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=''))
