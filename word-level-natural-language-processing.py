# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:46:58 2015
An example of word-level natural language processing task.
@author: YungLeChao
"""

def token_features(token, part_of_speech):
    if token.isdigit():
        yield "numeric"
    else:
        yield "token={}".format(token.lower())
        yield "token,pos={},{}".format(token, part_of_speech)
    if token[0].isupper():
        yield "uppercase_initial"
    if token.isupper():
        yield "all_uppercase"
    yield "pos={}".format(part_of_speech)