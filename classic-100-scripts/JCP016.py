#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime

if __name__ == '__main__':

    #output today 
    print(datetime.date.today())
    print(datetime.date.today().strftime('%d/%m/%Y'))

    miyazakiBirthDate = datetime.date(1941, 1, 5)
 
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
 
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
 
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))