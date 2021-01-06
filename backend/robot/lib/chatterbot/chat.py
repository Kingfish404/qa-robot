'''
File name: chat.py
Explain: 主要功能函数文件
Create by: ChengTong
Create Date:2020-12-30
Change by: 2021-1-4 by ChengTong  创建机器人
'''
import chatterbot
from chatterbot import ChatBot
from chatterbot.filters import get_recent_repeated_responses
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

mybot = ChatBot(
    'Example Bot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.95,
            'default_response': '0',
            "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance
        }
    ],
    filters=["filters.get_recent_repeated_responses"]
)

