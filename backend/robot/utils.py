'''
File name: utils.py
Explain: 主要功能函数文件
Create by: JinYu
Create Date:2020-12-13
Change by: 2020-12-13 by JinYu 初始化项目
'''
import json
from .lib.ChineseChatBot.chatbot import ChatBot
import requests

bot = ChatBot()


def chatterBotRepeat(sQuestion):
    sAnswer = bot.repeat(sQuestion)
    return sAnswer


def searchBotRepeat(sQuestion):
    sAnswer = "多喝热水\n"+sQuestion
    return sAnswer


def functionBotRepeat(sQuestion):
    sAnswer = "多喝热水\n"+sQuestion
    return sAnswer


def voiceToWord(pcmData):
    s_word = ""

    url = "http://vop.baidu.com/pro_api?dev_pid=80001&cuid=01000101&token=25.f6147b96ef2b0171c1255bc67867201e.315360000.1924180278.282335-23183171"

    payload = pcmData

    headers = {
        'Content-Type': 'audio/pcm;rate=16000',
        'Authorization': 'Bearer 24.42a2a960470b6823d052c15345f95513.2592000.1563515880.282335-15803531',
        'Cookie': 'BAIDUID=CD4B0219481E60D9EE11BD92C2956197:FG=1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jsonData = response.json()
    s_word = jsonData['result']
    return s_word
