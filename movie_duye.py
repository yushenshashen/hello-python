# coding utf-8
# date: 2018-12-6
# author: zp
# goal: analysis comments of Duye from maoyan
# original: https://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652568697&idx=1&sn=e2e52e392996202b2e4142462594e953&chksm=8464d433b3135d25d066b37f4899070e195a96b5ddde7b6d4cf9ba4ee40926768d1f97379b37&scene=21#wechat_redirect

import re
import requests
from bs4 import BeautifulSoup
import json
# from datetime import datetime,timedelta
import datetime
import pyecharts
from wordcloud import WordCloud
import pandas as pd
from collections import Counter

if __name__ == '__main__':
#     url = 'http://m.maoyan.com/mmdb/comments/movie/42964.json?_v_=yes&offset=15&startTime=2018-11-9%2019%3A36%3A43'
#     starttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    ##need to accurate as second now we only to day
    starttime = datetime.date(2018,12,6)
    endtime = datetime.date(2018,11,9)
#     endtime = datetime.date(2018,11,9)
    print([starttime,endtime])
    print(endtime + datetime.timedelta(1))
    
    results = []
    while starttime > endtime:
        url = 'http://m.maoyan.com/mmdb/comments/movie/42964.json?_v_=yes&offset=15&startTime='+str(starttime)+'%2019%3A36%3A43'
        starttime = starttime - datetime.timedelta(1)
        print(url)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
            html = requests.get(url, headers=headers)
            if html.status_code ==200:
                json_data = json.loads(html.text)['cmts']
                for item in json_data:
#                     print(item)
                    infor =  [ item['cityName'],item['content'].strip(),item['gender'] if 'gender' in item else '',item['id'],item['startTime'] ]
#                     infor = [ x.strip().replace('\n','') for x in infor ]
                    results.append(infor)
#                     print( infor )
#                     print('\n')
#                 soup = BeautifulSoup(html.text,'html.parser')
#                 infors = re.findall('\"content:\":')

        except:
            pass
    results = pd.DataFrame(results, columns=['cityName','content','gender','id','startTime'] )
    print(results[:5])
    
    results.to_csv('movie_duye_comments.txt', sep='\t', index=False)

    data = pd.read_csv('movie_duye_comments.txt',sep='\t', header=0, encoding='utf-8')
    print(data['content'][:5])

    ##pic 1 distribution map
    geo = pyecharts.Geo(' distribution of duye ', 'data resource: maoyan')
    attr, value = geo.cast( list(data['content']))
    # print(value)
    geo.add('',attr, value, visual_range = [0,5000], visual_text_color='#fff',symbol_size=15,is_visualmap=True, is_piecewise=False, visual_split_number=10)
    geo.render( 'movie_duye_map.html' )

    ##pic 2 city bar
    data_top20 = Counter(list(data['cityName'])).most_common(20)
    print(data_top20)
    bar = pyecharts.Bar('top 20 city', 'data resource', title_pos='center',width=1200,height=600)
    attr, value = bar.cast(data_top20)
    bar.add('', attr,value, is_visualmap=True, visual_range=[0,20], visual_text_color='#fff',is_more_utils=True,is_label_show=True )
    bar.render('citydistribution_bar.html')

# main()    