# coding:utf-8
import requests
from lxml import html
import time, sched
from wxpy import *
import logging
from tulingRobot import tuling
from simsimi import simsimi
import random

logging.basicConfig(filename="logger.log", level=logging.WARNING)

schedule = sched.scheduler(time.time, time.sleep)


def rossmannInit():
    rossmann_languan_0 = "https://www.rossmann.de/produkte/aptamil/pronutra-pre-anfangsmilch/4008976022350.html"
    rossmann_languan_1 = "https://www.rossmann.de/produkte/aptamil/pronutra-anfangsmilch-1/4008976022329.html"
    rossmann_languan_2 = "https://www.rossmann.de/produkte/aptamil/pronutra-folgemilch-2/4008976022336.html"
    rossmann_languan_3 = "https://www.rossmann.de/produkte/aptamil/pronutra-folgemilch-3/4008976022343.html"
    rossmann_zhihe_1 = "https://www.rossmann.de/produkte/aptamil/pronutra-kindermilch-1/4008976022985.html"
    rossmann_zhihe_2 = "https://www.rossmann.de/produkte/aptamil/pronutra-kindermilch-2/4008976022992.html"
    rossmann_baijin_0 = "https://www.rossmann.de/produkte/aptamil/profutura-anfangsmilch-pre/4008976022923.html"
    rossmann_baijin_1 = "https://www.rossmann.de/produkte/aptamil/profutura-anfangsmilch-1/4008976022909.html"
    rossmann_baijin_2 = "https://www.rossmann.de/produkte/aptamil/profutura-folgemilch-2/4008976022916.html"
    rossmann_hipp_3 = "https://www.rossmann.de/produkte/hipp/bio-bio-folgemilch-3/4062300001503.html"

    rossmann = [rossmann_languan_0,
                rossmann_languan_1,
                rossmann_languan_2,
                rossmann_languan_3,
                rossmann_zhihe_1,
                rossmann_zhihe_2,
                rossmann_baijin_0,
                rossmann_baijin_1,
                rossmann_baijin_2]

    productNameChinese={rossmann_languan_0:"蓝罐0段",
                        rossmann_languan_1:"蓝罐1段",
                        rossmann_languan_2:"蓝罐2段",
                        rossmann_languan_3:"蓝罐3段",
                        rossmann_zhihe_1:"纸盒1+",
                        rossmann_zhihe_2:"纸盒2+",
                        rossmann_baijin_0:"白金0段",
                        rossmann_baijin_1:"白金1段",
                        rossmann_baijin_2:"白金2段"}
    rossmann = [rossmann_zhihe_1,
                rossmann_baijin_2,
                rossmann_languan_3]
    return rossmann, productNameChinese


def checkRossmann(rossmann,productNameChinese):
    print("检查Rossmann：")
    for i in rossmann:
        page = requests.get(i)
        tree = html.fromstring(page.content)

        isAvaiable = tree.xpath('//span[@class="product-buy__standard-inner"]/text()')
        isNotAvaiable = tree.xpath('//div[@title="product-order__soon-online"]/text()')
        isNotAvaiable = isNotAvaiable + tree.xpath('//div[@class="product-order__soon-online"]/text()')

        if isAvaiable:
            amount = tree.xpath('//input[@id="amount"]/@value')
            maxAmount = tree.xpath('//input[@id="amount"]/@max')[0]
            print(productNameChinese[i] + "\t有货,\t限购数量：" + str(maxAmount))
            client.send("Rossmann:"+productNameChinese[i] + "\t有货,\t限购数量：" + str(maxAmount))
        elif isNotAvaiable:
            print(productNameChinese[i] + "\t无货")

def dmInit():
    dm_languan_0 = "https://www.dm.de/aptamil-pronutra-anfangsmilch-pre-von-geburt-an-p4008976022350.html"
    dm_languan_1 = "https://www.dm.de/aptamil-pronutra-anfangsmilch-1-von-geburt-an-p4008976022329.html"
    dm_languan_2 = "https://www.dm.de/aptamil-pronutra-folgemilch-2-nach-dem-6-monat-p4008976022336.html"
    dm_languan_3 = "https://www.dm.de/aptamil-pronutra-folgemilch-3-ab-dem-10-monat-p4008976022343.html"
    dm_zhihe_1 = "https://www.dm.de/aptamil-kindermilch-ab-1-jahr-p4008976022985.html"
    dm_zhihe_2 = "https://www.dm.de/aptamil-kindermilch-ab-2-jahren-p4008976022992.html"
    dm_baijin_0 = "https://www.dm.de/aptamil-profutura-anfangsmilch-pre-von-geburt-an-p4008976022923.html"
    dm_baijin_1 = "https://www.dm.de/aptamil-profutura-anfangsmilch-1-p4008976022909.html"
    dm_baijin_2 = "https://www.dm.de/aptamil-profutura-folgemilch-2-nach-dem-6-monat-p4008976022916.html"
    dm = [dm_languan_0,
          dm_languan_1,
          dm_languan_2,
          dm_languan_3,
          dm_zhihe_1,
          dm_zhihe_2,
          dm_baijin_0,
          dm_baijin_1,
          dm_baijin_2]
    productNameChinese={dm_languan_0:"蓝罐0段",
                        dm_languan_1:"蓝罐1段",
                        dm_languan_2:"蓝罐2段",
                        dm_languan_3:"蓝罐3段",
                        dm_zhihe_1:"纸盒1+",
                        dm_zhihe_2:"纸盒2+",
                        dm_baijin_0:"白金0段",
                        dm_baijin_1:"白金1段",
                        dm_baijin_2:"白金2段"}
    dm = [dm_zhihe_1,dm_languan_3,dm_baijin_2]
    return dm,productNameChinese


def checkDM(dm,productNameChinese):
    print("检查dm：")
    for i in dm:
        page = requests.get(i)
        tree = html.fromstring(page.content)
        isNotAvaiable = tree.xpath('//span[@class="availability availability-notAvailable"]/text()')
        isAvaiable = tree.xpath('//span[@class="availability availability-inStock"]/text()')
        if isAvaiable:
            maxAmount = max(int(x) for x in tree.xpath('//option/@value'))
            print(productNameChinese[i]+"\t有货,\t限购数量："+str(maxAmount))
            client.send("dm:" + productNameChinese[i] + "\t有货,\t限购数量：" + str(maxAmount))
        elif isNotAvaiable:
            print(productNameChinese[i]+"\t无货")


def perform_command(cmd,inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    checkRossmann(rossmann, productName)
    checkDM(dm,dm_name)
    lizhi.send("购票")


def re_log(cmd,inc):
    schedule.enter(inc, 0, re_log, (cmd, inc))
    bot, lizhi, client, group = initBot()
    print("log in time:"+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))


def timming_exe(cmd,inc):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(1, 0, perform_command, (cmd,inc))
    schedule.enter(60*60, 0, re_log, (cmd, 60*60))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()


def reminder(chatbot, receiver, msg):
    for i in receiver:
        target = chatbot.friends().search(i)[0]
        target.send(msg)


def initBot():
    bot = Bot(cache_path='bot.pkl')
    lizhi = bot.mps().search("南京李志")[0]
    lastMsg = "你好，跨年还未开票，请保持关注。更多资讯请关注微博@叁叁肆计划——李志团队"
    client = bot.friends().search('王韬')[0]
    group = bot.groups().search("科学代购")[0]

    @bot.register(msg_types=TEXT)
    def new_friends(msg):
        if msg.sender == lizhi:
            print(msg.text)
            logging.info(msg.text)
            lastMsg = "你好，跨年还未开票，请保持关注。更多资讯请关注微博@叁叁肆计划——李志团队"
            if msg.text != lastMsg:
                reminder(bot, ['王韬'], "李志音乐会最近消息:" + msg.text)
        elif isinstance(msg.chat, Friend):
            return tuling(msg.text, msg.sender)

    return bot, lizhi, client, group


if __name__ == "__main__":
    rossmann, productName = rossmannInit()
    dm, dm_name = dmInit()
    checkTime = 60*5
    bot, lizhi, client, group = initBot()
    timming_exe('No command',checkTime)