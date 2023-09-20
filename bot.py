'''
Descripttion: 
version: 
Author: tylerytr
Date: 2023-09-18 12:10:15
LastEditTime: 2023-09-19 19:56:24
LastEditors: tylerytr
FilePath: /tyleryin/feishu_bot/test/bot.py
Email:601576661@qq.com
Copyright (c) 2023 by tyleryin, All Rights Reserved. 
'''
import nonebot
# from nonebot.adapters.feishu import Adapter as FeishuAdapter
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init()

driver = nonebot.get_driver()
# driver.register_adapter(FeishuAdapter)
driver.register_adapter(Adapter)
#nonebot.load_plugins("src/plugins/")
nonebot.load_from_toml("pyproject.toml")

# nonebot.load_builtin_plugins("echo")  # 内置插件
# nonebot.load_plugin("nonebot-plugin-status")
if __name__ == "__main__":
    nonebot.run()

