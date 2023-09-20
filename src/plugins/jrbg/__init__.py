'''
Descripttion: 
version: 
Author: tylerytr
Date: 2023-09-18 17:08:34
LastEditTime: 2023-09-19 16:56:43
LastEditors: tylerytr
FilePath: /tyleryin/feishu_bot/bagu_bot/src/plugins/jrbg/__init__.py
Email:601576661@qq.com
Copyright (c) 2023 by tyleryin, All Rights Reserved. 
'''
from pathlib import Path
import os
import nonebot 
import random
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import logger
# from .config import Config


random_bg=on_command("jrbg",rule=to_me(),priority=5)

Interview_experience_path="src/Interview_experience/C++基架后端/solution/build"
current_dir = os.getcwd()
files_path=os.path.join(current_dir,Interview_experience_path)
@random_bg.handle()
async def handle_random_bg():
    
    file_list = []
    file_name = ""
    
    for root, dirs, files in os.walk(files_path):
        for temp in files:
            #logger.info(str(temp))
            file_path = os.path.join(root, temp)
            file_list.append(file_path)
    # file_name=len(file_list)
    if file_list:
        file_name = random.choice(file_list)
    current_file=open(file_name,"r")
    content=current_file.read()
    current_file.close()
    
    await random_bg.send(content)
    
    
    
    
    


