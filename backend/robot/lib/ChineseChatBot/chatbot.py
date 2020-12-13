'''
问答机器人

'''

import sys
from os.path import abspath, join, dirname
sys.path.append(join(abspath(dirname(__file__)), ''))

from filter import  LayerFilter

class ChatBot:

    def __init__(self):
        self.layer_filter = LayerFilter()
        self.white_list = []

    @classmethod
    def to_log(cls, question, answer):
        log_content = f'Q:{question}---A:{answer} \n'
        print(log_content)
        # with open('config/chat_log.txt', 'a', encoding='utf-8') as f:
        #     f.write(log_content)
    
    def local_start(self):
        """本地聊天模式"""

        print('我们开始聊天吧~')
        while True:
            question = input('>> ')
            if question == '关机':
                print('好的，下次再见~')
                break
            answer = self.layer_filter.get_answer(question)
            print(answer)
            # self.to_log(question,answer)


    def repeat(self,question):
        """回复消息"""
        answer = self.layer_filter.get_answer(question)
        self.to_log(question,answer)  
        return answer
