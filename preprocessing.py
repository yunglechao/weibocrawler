# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:16:42 2015

@author: YungLeChao
"""

from sklearn import preprocessing
import numpy as np
import scipy
X = np.array([[ 1., -1.,  2.], [ 2.,  0.,  0.], [ 0.,  1., -1.]])
X_scaled = preprocessing.scale(X)
print(X_scaled)
#X_scaled.mean(axis=0)
#X_scaled.std(axis=0)
min_max_scaler = preprocessing.MinMaxScaler()
X_minmax = min_max_scaler.fit_transform(X)
print(X_minmax)
data_csr = scipy.sparse.csr_matrix
X_normalized = preprocessing.normalize(X, norm='l2')
normalizer = preprocessing.Normalizer().fit(X)
print(normalizer.transform(X))
