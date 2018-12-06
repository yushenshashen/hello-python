# coding utf-8
# date: 2018-12-6
# author: zp
# goal: analysis music ##动态网页  new lib selenium
# original: https://blog.csdn.net/jdjrdata/article/details/73614607

import sys
from selenium import webdriver

url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
driver = webdriver.PhantomJS()

driver.get(url)
driver.switch_to.frame('contentFrame')
data = driver.find_element_by_id('m-pl-container').find_element_tag_name('li')
results = []
for i in range(len(data)):
    nb = data[i].find_element_by_class_name('nb').text
    if 'wan' in nb and int(nb.split('wan')[0]) > 500:
        msk = data[i].find_element_by_css_selector('a.mask')
        results.append([msk.get_attribute('title'),nb, msk.get_attribute('href')])
