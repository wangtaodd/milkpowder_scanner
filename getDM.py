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


def dm_init(name):
    dm_url = {"LG0": "https://www.dm.de/aptamil-pronutra-anfangsmilch-pre-von-geburt-an-p4008976022350.html",
              "LG1": "https://www.dm.de/aptamil-pronutra-anfangsmilch-1-von-geburt-an-p4008976022329.html",
              "LG2": "https://www.dm.de/aptamil-pronutra-folgemilch-2-nach-dem-6-monat-p4008976022336.html",
              "LG3": "https://www.dm.de/aptamil-pronutra-folgemilch-3-ab-dem-10-monat-p4008976022343.html",
              "ZH1": "https://www.dm.de/aptamil-kindermilch-ab-1-jahr-p4008976022985.html",
              "ZH2": "https://www.dm.de/aptamil-kindermilch-ab-2-jahren-p4008976022992.html",
              "BJ0": "https://www.dm.de/aptamil-profutura-anfangsmilch-pre-von-geburt-an-p4008976022923.html",
              "BJ1": "https://www.dm.de/aptamil-profutura-anfangsmilch-1-p4008976022909.html",
              "BJ2": "https://www.dm.de/aptamil-profutura-folgemilch-2-nach-dem-6-monat-p4008976022916.html"
              }
    dm_lst = []
    for i in name:
        milk = product()
        milk.setName(name_ch[i])
        milk.setUrl(dm_url[i])
        dm_lst.append(milk)
    return dm_lst


def check_dm(dm_lst):
    print("checking dm：")
    for i in dm_lst:
        page = requests.get(i.url)
        tree = html.fromstring(page.content)

        product_name = tree.xpath('//span[@itemprop="name"]/@content')
        if not product_name:
            is_not_available = "No Page Found"
        else:
            is_not_available = tree.xpath('//span[@class="availability availability-notAvailable"]/text()')
        is_available = tree.xpath('//span[@class="availability availability-inStock"]/text()')
        if is_available:
            max_amount = max(int(x) for x in tree.xpath('//option/@value'))
            i.isAvailable = True
            i.maxAmount = max_amount
            print(i.name+"\t有货,\t限购数量："+str(max_amount))
        elif is_not_available:
            print(i.name+"\t无货")
            i.isAvailable = False


def test():
    check_list = name_ch.keys()
    dm_list = dm_init(check_list)
    check_dm(dm_list)
    for i in dm_list:
        print(i.name, i.isAvailable)


if __name__ == "__main__":
    test()
