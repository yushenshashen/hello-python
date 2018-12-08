#date: 2018-12-8
#zp:zp
#goal: learn lib xpath  very convinent only copy the path

from lxml import etree
import requests
import random

url = 'http://book.douban.com/top250?start=1'
r = requests.get(url)

s = etree.HTML(r.text)
file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
time.sleep( random.randint(2,5) )
for div in file:
    print(div.xpath('./tr/td[2]/div[1]/a/@title')[0])
    print(div.xpath('./tr/td[2]/div[1]/a/@href')[0])
    print(div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0])
    print(div.xpath('./tr/td[2]/p[2]/span/text()')[0].strip())
    