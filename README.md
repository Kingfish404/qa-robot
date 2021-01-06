# QARobot

AI聊天机器人项目，可以判断是语音还是文字，获取内容，内容分为命令和普通聊天，如果是命令，根据命令的不同回复回复不同的结果；聊天，根据内容判断，只能匹配内容进行回复。

## 项目结构

* doc 文件夹，接口文档
* backend 文件夹，项目Django后端
* frontend 文件夹，项目前端

各端细节见分别文件夹内的`README.md`文件

## 功能

* 问病情  
* 查资料  
* 聊天  

## 技术路线

* NLP - 自然语言处理 - 真问答 - 聊天   
* 爬虫 - 关键词匹配问答 - example： 发烧 -> 发烧balabala    
* 自己设计的功能性问答 - 查询附近最近的医院|查看功能列表   


## Lib

* Chatterbot  
* bs4  
* jieba

## 待办事项

语义库的准备

## 致谢

非常感谢以下开源项目，我们参考了以下项目的代码和设计

* [https://github.com/GoWeiXH/ChineseChatBot](https://github.com/GoWeiXH/ChineseChatBot)