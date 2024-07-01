# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 06:41:38 2024

@author: shadd
"""

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price *.10
else:
    down_payment= 0.2 * price
print(f'Down payment: ${down_payment}')