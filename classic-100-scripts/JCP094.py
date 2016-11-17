#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import numpy as np

if __name__ == '__main__':

    play = raw_input('Do you want to paly it or not(y or n):')

    while play == 'y' or play == 'yes':

        print 'The name of the game is guess a number \n Come on let\'s begin the game'
        #number = np.random.randint(0,10000)
        number = 20
        flag = 'on'
        while flag == 'on':
            guess = int(raw_input('please input a number: '))
            a = time.time()

            if guess > number:
                print 'your number is bigger'
            elif guess < number:
                print 'your number is smaller'
            else:
                print 'that\'s the number'
                b = time.time()
                flag = 'off'

        var = (b-a) / 18.2

        if var > 15:
            print 'you are slow'
        elif var > 5 and var <=15:
            print 'normal'
        else:
            print 'smart'


        print 'your time is %d second' % var
        break

        print 'again?'
    else:
        print 'what a pity!'

