# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:13:55 2020

@author: Dr. Taimoor
"""


#Dataset link: https://archive.ics.uci.edu/ml/datasets/Eco-hotel

#As text file
#corpus = open('D:\\dataset-CalheirosMoroRita-2017.txt').read()

#with pandas
import pandas as pd
corpus = pd.read_csv('D:\\dataset-CalheirosMoroRita-2017.csv', delimiter = '\n', encoding = 'Latin-1', error_bad_lines = False)
print(corpus)