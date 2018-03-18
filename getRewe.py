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


def reweInit(name):
    rewe_url = {"LG0": "https://shop.rewe.de/PD1958158?variantArticleId=4008976022350",
                "LG1": "https://shop.rewe.de/PD1958156?variantArticleId=4008976022329",
                "LG2": "https://shop.rewe.de/PD1958154?variantArticleId=4008976022336",
                "LG3": "https://shop.rewe.de/PD1958152?variantArticleId=4008976022343",
                "ZH1": "https://shop.rewe.de/PD1964189?variantArticleId=4008976022985",
                "ZH2": "https://shop.rewe.de/PD1964191?variantArticleId=4008976022992",
                "BJ0": "https://shop.rewe.de/PD2522946?variantArticleId=4008976022923",
                "BJ1": "https://shop.rewe.de/PD2522955?variantArticleId=4008976022909",
                "BJ2": "https://shop.rewe.de/PD2522960?variantArticleId=4008976022916",
                }

    rewe_lst = []
    for i in name:
        milk = product()
        milk.setName(name_ch[i])
        milk.setUrl(rewe_url[i])
        rewe_lst.append(milk)

    return rewe_lst


def checkRewe(rewe_lst):
    print("checking rewe：")
    for i in rewe_lst:
        page = requests.get(i.url)
        tree = html.fromstring(page.content)
        # TODO:
        # isNotAvailable = tree.xpath('//span[@class="availability availability-notAvailable"]/text()')
        isNotAvailable = False
        isAvailable = tree.xpath('//meso-data[@data-context="product-detail"]/@data-amount')
        if isAvailable:
            i.isAvailable = True
            maxAmount = tree.xpath('//meso-data[@data-context="product-detail"]/@data-orderlimit')[0]
            i.maxAmount = maxAmount
            print(i.name+"\t有货,\t限购数量："+str(maxAmount))
        elif isNotAvailable:
            print(i.name+"\t无货")
            i.isAvailable = False


def test():
    checkList = name_ch.keys()
    reweList = reweInit(checkList)
    checkRewe(reweList)
    for i in reweList:
        print(i.name, i.isAvailable)

if __name__ == "__main__":
    test()
