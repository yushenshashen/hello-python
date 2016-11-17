#!/usr/bin/env python

#I = input('please input the I:')
I = int(raw_input('input: '))

if I <= 10:
	money = 0.1*I
elif 10 < I <= 20:
	money = 0.1*10 + (I-10)*0.075 
elif 20 < I <= 40:
	money = 0.1*10 + 0.075*10 + (I-20)*0.05
elif 40 < I <= 60:
	money = 0.1*10 + 0.075*10 + 0.05*20 + (I-40)*0.03
elif 60 < I <= 100:
	money = 0.1*10 + 0.075*10 + 0.05*20 + 0.03*20 + (I-60)*0.015
elif I > 100:
	money = 0.1*10 + 0.075*10 + 0.05*20 + 0.03*20 + 0.015*40 + (I-100)*0.01

print 'money is',money