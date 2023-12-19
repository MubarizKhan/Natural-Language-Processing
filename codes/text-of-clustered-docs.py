# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:21:14 2020

@author: Dr. Taimoor
"""

#reading data and spliting docs
corpus = open('D:\\Dataset.txt').read()
print(corpus)

data = corpus.split('\n')
print(data)

#vectorizing data
from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
matrix_data = vec.fit_transform(data)
print(matrix_data)

#clustering
from sklearn.cluster import KMeans
km = KMeans(n_clusters = 2)
km.fit(matrix_data)
print(km.labels_)

#finding and printing source text of documents grouped together
raw_text_cluster0 = [data[i] for i in range(0, len(data)) if km.labels_[i] == 0]
raw_text_cluster1 = [data[i] for i in range(0, len(data)) if km.labels_[i] == 1]

print(raw_text_cluster0)
print(raw_text_cluster1)

#finding and printing of structured input for documents grouped together
struc_text_cluster0 = [matrix_data[i].toarray() for i in range(0, len(matrix_data.toarray())) if km.labels_[i] == 0]
struc_text_cluster1 = [matrix_data[i].toarray() for i in range(0, len(matrix_data.toarray())) if km.labels_[i] == 1]

print(struc_text_cluster0)
print(struc_text_cluster1)