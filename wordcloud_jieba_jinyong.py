# coding: utf-8
import jieba
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

back_color = imread('/Users/zp/Desktop/data_mining/practices/background1.jpeg')
# print(back_color)

font_path = '/Users/zp/Desktop/data_mining/practices/simheittf/simhei.ttf'
wc = WordCloud( background_color='white', mask=back_color, max_font_size=100,max_words=1000,font_path=font_path, random_state=42 )

text = open('/Users/zp/Desktop/data_mining/practices/words.text','r').read()
# print(text)
pattern = re.compile(u"[\u4e00-\u9fa5]+")
text = re.findall(pattern, text)
# print(text)

word_generator = jieba.cut(''.join(text) )

##way 1
words = ','.join(word_generator)
words = words.split(',')
# print(words)

stopwords = pd.read_table('/Users/zp/Desktop/data_mining/practices/stopwords.txt',sep='\t',names=['stopwords'],index_col=False,encoding='utf-8')
print(stopwords['stopwords'][:10])

cleaned_words = [ x for x in words if x not in list(stopwords['stopwords']) ]
cleaned_words = ' '.join(cleaned_words)
# print(cleaned_words)
print(len(words))
print(len(cleaned_words))

wc.generate(cleaned_words)
image_colors = ImageColorGenerator(back_color)
plt.imshow(wc)
wc.to_file('first_pic_jinyong.png')
# plt.axis('off')
# plt.figure()
# plt.imshow(wc.recolor(color_func=image_colors))
# plt.axis('off')

