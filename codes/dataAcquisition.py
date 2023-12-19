# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:21:15 2019

@author: Taimoor
"""

import requests
session = requests.Session()
session.trust_env = False

#proxies = {
#          'http' : 'http://192.168.12.84:808',
#          'https' : 'https://192.168.23.38:808'
#       }

response = session.get('http://cstags.pk')
print(response)
print(response.text)