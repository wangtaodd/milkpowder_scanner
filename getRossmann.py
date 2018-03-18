# coding:utf-8
import requests
from product import product
from lxml import html


name_ch = {"LG0": "蓝罐0段",
           "LG1": "蓝罐1段",
           "LG2": "蓝罐2段",
           "LG3": "蓝罐3段",
           "ZH1": "纸盒1+",
           "ZH2": "纸盒2+",
           "BJ0": "白金0段",
           "BJ1": "白金1段",
           "BJ2": "白金2段"}


def rossmannInit(name):
    rossmann_url = {"LG0": "https://www.rossmann.de/produkte/aptamil/pronutra-pre-anfangsmilch/4008976022350.html",
                    "LG1": "https://www.rossmann.de/produkte/aptamil/pronutra-anfangsmilch-1/4008976022329.html",
                    "LG2": "https://www.rossmann.de/produkte/aptamil/pronutra-folgemilch-2/4008976022336.html",
                    "LG3": "https://www.rossmann.de/produkte/aptamil/pronutra-folgemilch-3/4008976022343.html",
                    "ZH1": "https://www.rossmann.de/produkte/aptamil/pronutra-kindermilch-1/4008976022985.html",
                    "ZH2": "https://www.rossmann.de/produkte/aptamil/pronutra-kindermilch-2/4008976022992.html",
                    "BJ0": "https://www.rossmann.de/produkte/aptamil/profutura-anfangsmilch-pre/4008976022923.html",
                    "BJ1": "https://www.rossmann.de/produkte/aptamil/profutura-anfangsmilch-1/4008976022909.html",
                    "BJ2": "https://www.rossmann.de/produkte/aptamil/profutura-folgemilch-2/4008976022916.html"}
    rm_lst = []
    for i in name:
        milk = product()
        milk.setName(name_ch[i])
        milk.setUrl(rossmann_url[i])
        rm_lst.append(milk)
    return rm_lst


def checkRossmann(rm_lst):
    print("checking Rossmann：")
    for i in rm_lst:
        page = requests.get(i.url)
        tree = html.fromstring(page.content)

        isAvailable = tree.xpath('//span[@class="product-buy__standard-inner"]/text()')
        isNotAvailable = tree.xpath('//div[@title="product-order__soon-online"]/text()')
        isNotAvailable = isNotAvailable + tree.xpath('//div[@class="product-order__soon-online"]/text()')

        if isAvailable:
            maxAmount = tree.xpath('//input[@id="amount"]/@max')[0]
            i.isAvailable = True
            i.maxAmount = maxAmount
            print(i.name + "\t有货,\t限购数量：" + str(maxAmount))
        elif isNotAvailable:
            i.isAvailable = False
            print(i.name + "\t无货")


def test():
    checkList = name_ch.keys()
    rmList = rossmannInit(checkList)
    checkRossmann(rmList)
    for i in rmList:
        print(i.name, i.isAvailable)

if __name__ == "__main__":
    test()
