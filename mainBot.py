# coding:utf-8
import requests
from lxml import html
import time, sched
from wxpy import *
import logging
from tuling import tuling
import getDM, getRossmann
# from simsimi import simsimi
import random

logging.basicConfig(filename="logger.log", level=logging.WARNING)

schedule = sched.scheduler(time.time, time.sleep)





def perform_command(cmd,inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    getRossmann.checkRossmann(rossmann_name)
    for i in rossmann_name:
        if i.isAvailable:
            client.send(i.name + "\t有货,\t限购数量：" + str(i.maxAmount))
        else:
            client.send(i.name + "\t无货")


def re_log(cmd,inc):
    schedule.enter(inc, 0, re_log, (cmd, inc))
    bot, lizhi, client, group = initBot()
    print("log in time:"+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))


def timming_exe(cmd,inc):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(1, 0, perform_command, (cmd, inc))
    # schedule.enter(60*60, 0, re_log, (cmd, 60*60))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()


def reminder(chatbot, receiver, msg):
    for i in receiver:
        target = chatbot.friends().search(i)[0]
        target.send(msg)


def initBot():
    bot = Bot(cache_path='bot.pkl')
    client = bot.friends().search('王韬')[0]
    # group = bot.groups().search("科学代购")[0]

    @bot.register(msg_types=TEXT)
    def new_friends(msg):
        if isinstance(msg.chat, Friend):
            return tuling(msg.text, msg.sender)
    return bot, client,


if __name__ == "__main__":
    name_ch = {"LG0": "蓝罐0段",
               "LG1": "蓝罐1段",
               "LG2": "蓝罐2段",
               "LG3": "蓝罐3段",
               "ZH1": "纸盒1+",
               "ZH2": "纸盒2+",
               "BJ0": "白金0段",
               "BJ1": "白金1段",
               "BJ2": "白金2段"}
    rossmann_name = getRossmann.rossmannInit(["BJ2"])
    dm_name = getDM.dm_init(name_ch.keys())
    checkTime = 60*30
    bot, client = initBot()
    timming_exe('No command',checkTime)