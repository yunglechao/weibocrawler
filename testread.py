# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:04:40 2015

@author: YungLeChao
"""
def sparse_vector (indices, values):
    vector = [indices, values]
    ind = values.index(max(values))
    print (indices[ind], values[ind])
    return vector