from selenium import webdriver
import time
from lxml import html

chrome = webdriver.Chrome()
chrome.get('https://www.dm.de/baby-und-kind/babynahrung/brei/')
time.sleep(5)
page = chrome.page_source
# print(page)
tree = html.fromstring(page)
productName = tree.xpath('//div[@class="product-tile-description"]/a/strong/text()')
print(productName)