#!/usr/bin/python
# -*- coding: UTF-8 -*-

#统计文章各个单词出现的词频，并按单次的词频从大到小输出 

import re
import collections
import numpy as np
import pandas as pd

def count_words(text):
	results = {}
	text = text.lower()
	all_text = re.sub("\"|,|\.|\!|\?", "", text)

	for word in all_text.split():
		if word in results:
			results[word] += 1
		else:
			results[word] = 1
	return results

if __name__ == '__main__':

	#text = '''Everyone has their own dreams, I am the same. But my dream is not a lawyer, not a doctor, not actors, not even an industry. Perhaps my dream big people will find it ridiculous, but this has been my pursuit! My dream is to want to have a folk life! I want it to become a beautiful painting, it is not only sharp colors, but also the colors are bleak, I do not rule out the painting is part of the black, but I will treasure these bleak colors! Not yet, how about, a colorful painting, if not bleak, add color, how can it more prominent American? Life is like painting, painting the bright red color represents life beautiful happy moments. Painting a bleak color represents life difficult, unpleasant time. You may find a flat with a beautiful road is not very good yet, but I do not think it will. If a person lives flat then what is the point? Life is only a short few decades, I want it to go Finally, Each memory is a solid.'''

	##if put the article into a file
	with open('data.txt') as text:
		text = text.read()
		words = count_words(text)

		##according to key
		#words_sortted = sorted(words.items())
		##according to value
		words_sortted = collections.OrderedDict(sorted(words.items(),key=lambda x : -x[1]))
		#or ,words_sortted = sorted(words.items(),key=lambda x : x[1],reverse=True)

		for k,v in words_sortted.items():
			print 'word \'%s\' frequency is: %d' % (k,v)




