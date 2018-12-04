#author: zp
#date: 2018-12-4
#goal: analysis moview zhanlang2 from douban

import requests
import re
from bs4 import BeautifulSoup


#find comment directly
# https://movie.douban.com/subject/26363254/comments?start=0&limit=20&sort=new_score&status=P

#1 get download comments from web
comments = []
for i in range(2):
    # print(i)
    r = requests.get('https://movie.douban.com/subject/26363254/comments?start=' + str(i) + '&limit=20&sort=new_score&status=P')
    soup = BeautifulSoup(r.text, 'html.parser')
    infors = soup.find_all('span', class_ = "short")
    for infor in infors:
        comment = infor.string.strip()
        comments.append(comment)
        # print(infor.string)

comments = ''.join(comments)

#2 clean data
pattern = re.compile(u"[\u4e00-\u9fa5]+")  ###match chinese
comments = re.findall(pattern, comments)
cleaned_comments = ''.join(comments)
print(cleaned_comments)

#3 divide data into word
import jieba #分词包
cuted = jieba.cut(cleaned_comments)
print(cuted)
cuted = ','.join(cuted)
words = cuted.split(',')
print(words)

# from collections import Counter
# print( Counter(cuted).most_common(10) )
#
import pandas as pd
# words = pd.DataFrame.from_dict(Counter(cuted),orient='index',columns=['words'])
# print(words[:5])
#
stopwords = pd.read_table('/Users/zp/Desktop/data_mining/practices/stopwords.txt',sep='\t',names=['stopwords'],index_col=False,encoding='utf-8')
print(stopwords['stopwords'][:10])
print(stopwords[:5])


cleaned_words = [ x for x in words if x not in list(stopwords['stopwords']) ]
cleaned_words = ' '.join(cleaned_words)
print(cleaned_words)

import matplotlib.pyplot as plt
import matplotlib

from wordcloud import  WordCloud
wc = WordCloud(font_path='/Users/zp/Downloads/simheittf/simhei.ttf', background_color='white',max_font_size=8).generate(cleaned_words)

plt.show(wc)
# plt.axis('off')
wc.to_file('/User/zp/Desktop/')