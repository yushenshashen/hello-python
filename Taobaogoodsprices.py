#python3
#coding: utf-8

#author: zp
#date: 2018-12-2
#goal: learn requests + re lib to get data from taobao

import requests
import re

def getHTMLText( url ):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ''

def getGoodsInfor( goodsInfor, html ):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]\"',html )
		tlt = re.findall(r'\"rwa_title\"\:.*?\"', html)
		for i in range(len(plt)):
			price = eval( plt.split(':')[1] )
			title = eval( tlt.split(':')[1] )
			goodsInfor.append( [price, title] )
	except:
		return ''

def printGoodsList( goodsInfor ):
	tplt = '{:4}\t{:6}\t{:8}'
	print(tplt.format("序号","价格","商品"))
	count = 0
	for g in goodsInfor:
		count = count + 1
		print( tplt.format(count, g[0],g[1] ) )

def main():
	goods = 'bag'
	depth = 2
	start_url = 'https://s.taobao.com/search?q=' + goods
	goodsInfor = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44 * i)
			html = getHTMLText( url )
			getGoodsInfor(goodsInfor, html )
		except:
			continue
	print(goodsInfor)
	printGoodsList(goodsInfor )

main()

