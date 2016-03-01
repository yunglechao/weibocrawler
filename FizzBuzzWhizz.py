# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:55:02 2015

@author: YungLeChao
"""



#for i in range(1,101):
#    fizz += [('Fizz'*(i%a==0)+'Buzz'*(i%b==0)+'Whizz'*(i%c==0)) or str(i)]

def FizzBuzzWhizz(a=None, b=None, c=None):
    return [lambda a, b, c, i=i:('Fizz'*(i%a==0)+'Buzz'*(i%b==0)+'Whizz'*(i%c==0)) or i for i in range(1,101)]
    
for student in FizzBuzzWhizz():
    print(student(3,5,7))