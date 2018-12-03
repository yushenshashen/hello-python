#python3
#coding: utf-8

#author: zp
#date: 2018-12-3
#goal: learn requests + re + bs4 lib to get stock data in eastmoney

import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url, code='utf-8'):
	try:
		r = requests.get( url, timeout=30 )
		r.raise_for_status
		r.encoding = code
		return r.text
	except:
		return ''

def getStockList(lst, stock_url):
	html = getHTMLText( stock_url, code = 'GB2312' )
	soup = BeautifulSoup(html,'html.parser' )
	a = soup.find_all('a')
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r's[zh]\d{6}',href)[0] )
		except:
			continue

def getStockInfor(lst, stock_url, output_file ):
	for stock in lst:
		count = 0
		url = stock_url + stock + '.html'
		html = getHTMLText(url )

		try:
			if html == '':
				continue
			else:
				inforDict = {}
				soup = BeautifulSoup( html, 'html.parser' )

				name = soup.find_all(attrs={'class':'bets-name'}) 
				inforDict.update({'股票名称':name.text.split()[0]})

				stockInfor = soup.find('div',attrs={'class':'stock-bets'})

				keyList = stockInfor.find_all('dt')
				valueList = stockInfor.find_all('dd')
				for i in range(len(keyList)):
					key = keyList[i].text
					value = valueList[i].text
					inforDict[key] = value

				with open(output_file, 'a') as f:
					f.write(str(inforDict) + '\n')
					count = count + 1
					print('\r当前速度: {:.2f}%'.format( count*100/len(lst) ),end='' )
		except:
			print('\r当前速度: {:.2f}%'.format( count*100/len(lst) ),end='' )
			continue

def main():

	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_infor_url = 'http://quote.eastmoney.com/stock/'
	output_file = '/Users/zp/Desktop/data_mining/practices/spider_stock_3rdweek.txt'
	slist = []
	getStockList(slist, stock_list_url )
	getStockInfor( slist,stock_infor_url, output_file)

main()