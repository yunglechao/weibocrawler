# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:47:55 2015

@author: YungLeChao
"""

def ask(prompt, hint = "yes or no", chance = 2):
    while chance > 0:
        answer = input(prompt)
        if answer.lower() in ('y', 'yes'):
            print ("Thank you")
            return True
        if answer.lower() in ('n', 'no'):
            print ("Why not ")
            return False
        else:
            chance -= 1
            print (hint)
print ("Sorry, you have tried too many times.")