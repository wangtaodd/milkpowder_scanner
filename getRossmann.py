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
    rossmann_url = {"LG0": "https://www.rossmann.de/produkte/aptamil/pronutra-advance-pre-anfangsmilch-von-geburt-an/4056631001202.html",
                    "LG1": "https://www.rossmann.de/produkte/aptamil/pronutra-advance-1-anfangsmilch-von-geburt-an/4056631001226.html",
                    "LG2": "https://www.rossmann.de/produkte/aptamil/pronutra-advance-2-folgemilch-nach-dem-6-monat/4056631001240.html",
                    "LG3": "https://www.rossmann.de/produkte/aptamil/pronutra-advance-3-folgemilch-ab-dem-10-monat/4056631001264.html",
                    "ZH1": "https://www.rossmann.de/produkte/aptamil/pronutra-kindermilch-1/4008976022985.html",
                    "ZH2": "https://www.rossmann.de/produkte/aptamil/pronutra-kindermilch-2/4008976022992.html",
                    "BJ0": "https://www.rossmann.de/produkte/aptamil/profutura-pre-anfangsmilch-von-geburt-an/4056631001301.html",
                    "BJ1": "https://www.rossmann.de/produkte/aptamil/profutura-1-anfangsmilch-von-geburt-an/4056631001325.html",
                    "BJ2": "https://www.rossmann.de/produkte/aptamil/profutura-2-folgemilch-nach-dem-6-monat/4056631001349.html"}
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
    # for i in rmList:
    #     print(i.name, i.isAvailable)

if __name__ == "__main__":
    test()
