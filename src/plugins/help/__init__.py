'''
Descripttion: 
version: 
Author: tylerytr
Date: 2023-09-19 19:56:52
LastEditTime: 2023-09-19 19:58:03
LastEditors: tylerytr
FilePath: /tyleryin/feishu_bot/bagu_bot_qq/src/plugins/help/__init__.py
Email:601576661@qq.com
Copyright (c) 2023 by tyleryin, All Rights Reserved. 
'''
#-*- coding: utf-8 -*-
import json
import requests
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, MessageSegment
# from nonebot.adapters.feishu import MessageSegment

help = on_command("help", rule=to_me(), aliases={"help", "帮助"}, priority=5)

@help.handle()
async def handle_func():
    await help.send("你可以尝试对我说:XXXXXXXXX")
    #await help.send(MessageSegment.image(image_key="img_v2_11xxxxx17-f751-4e86-8f2d-43fd4b231edg"))
    #这里可以写关键词命中后的业务逻辑