#python3
#coding: utf-8

#author: zp
#date: 2018-12-2
#goal: learn requests lib to download data from web
#tips: python3 -m  pip install requests

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
    
def fillUnivList(ulist, html):
    # ulist = []
    soup = BeautifulSoup( html, 'html.parser' )
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append( [ tds[0].string, tds[1].string, tds[2].string] )
    
def printUnivList( ulist,num ):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print( tplt.format("排名","学校", "分数",chr(12288)) ) 
    # print( "{:^10}\t{:^10}\t{:^10}".format("排名","学校", "分数") )
    for i in range(num):
        u = ulist[i]
        print( tplt.format(u[0],u[1],u[2],chr(12288)) )
        # print( "{:^10}\t{:^10}\t{:^10}".format(u[0],u[1],u[2]) )
        
# if __name__ == '__main__':        
def main():
    uinfor = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    ulist = []
    fillUnivList(ulist, html)
    printUnivList( ulist, 20 )
    
main()
