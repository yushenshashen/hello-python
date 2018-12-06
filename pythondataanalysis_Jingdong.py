# coding: utf-8
# date: 2018-12-6
# author: zp
# goal: get comments from bok 'python data analysis' in Jingdong
# original: https://www.sohu.com/a/196965958_752099

import re
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

#step 1 get infor from web
page_count = 10
comments_text = []
comments_date = []
for i in range(page_count):
    url  = 'https://club.jd.com/review/11352441-1-' + str(i) +'-0.html'
    r = requests.get(url,timeout=10)
    soup = BeautifulSoup(r.text, 'html.parser')
    infors = soup.find_all('div',class_= 'comment-content')
    for infor in infors:
        comments_text.append(infor.string.strip())
#         print(infor.string.strip())
    
    infors = soup.find_all('span',class_= 'date-comment')
    for infor in infors:
        comments_date.append(infor.string)
#         print(infor.string)
    
comments_date = pd.DataFrame( comments_date )
comments_text = pd.DataFrame( comments_text )
comments = pd.concat( [comments_date, comments_text], axis=1 )
comments.columns = ['date','text']
print(comments[:5])
    
#step 2 wordcloud analysis
from wordcloud import WordCloud
import jieba
from collections import Counter
import matplotlib.pyplot as plt

words = jieba.cut(''.join(comments['text']))
words = list(words)
print(Counter(words).most_common(10))

stopwords = pd.read_table('/Users/zp/Desktop/data_mining/practices/stopwords.txt',sep='\t',names=['stopwords'],index_col=False,encoding='utf-8')
# print(stopwords[:5])

cleaned_words = [ x for x in words if x not in list(stopwords['stopwords']) ]
cleaned_words = ' '.join(cleaned_words)
print(cleaned_words)

wc = WordCloud(font_path='simheittf/simhei.ttf', background_color='white',max_font_size=50,random_state=42)
wc.generate_from_text(cleaned_words)

plt.imshow(wc)
plt.axis('off')
wc.to_file('pythondataanalyiscomments_ciyun.png')

#step 3 analysis date of comments
comments['day'] = comments['date'].apply( lambda x: x.split()[0] )
grouped = comments['text'].groupby(comments['day'])
print(grouped.size()[:5])
print(grouped.size().index )
print(list(grouped.size().index) )

plt.figure()
grouped.size().plot(kind='bar',alpha=0.5,color='r')
plt.legend()
# plt.xticklabels( list(grouped.size().index) )
plt.xlabel('date')
plt.ylabel('comments count')
plt.title('comments in Jingdong')
plt.savefig('comments_in_Jingdong.png')
