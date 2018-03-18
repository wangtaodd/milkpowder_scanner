# encoding:utf-8
import requests
from lxml import html

# 商品名称 价格 品牌 重量 图片 配方 是否有货 货物编码
url = "https://www.dm.de/hipp-bio-getreidebrei-reisflocken-nach-dem-4-monat-p4062300252257.html"
page = requests.get(url)
tree = html.fromstring(page.content)
productName = tree.xpath('//span[@itemprop="name"]/@content')[0]
productBrand = tree.xpath('//span[@itemprop="brand"]/@content')[0]
productPrice = tree.xpath('//div[@class="price"]/span[@class="price-digit"]/text()')[0] + "." + \
               tree.xpath('//div[@class="price"]/span[@class="price-cent"]/text()')[0]
productWeight = tree.xpath('//div[@class="product-attributes-info-price"]/text()')[0].strip('\n\t').split(' ', 2)
isAvailable = tree.xpath('//span[@class="availability availability-inStock"]/text()')
img = tree.xpath('//img[@itemprop="image"]/@src')[0]
imgcontent = requests.get(img)
with open('picture.png', 'wb') as file:
    file.write(imgcontent.content)
print(isAvailable)
print(productWeight)
print(productName)
print(productBrand)
print(productPrice)
