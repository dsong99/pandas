import os, sys


coupon=5
ytm=0.05
n=30


one_ytm=1+ytm
one_ytm_nth=one_ytm**n

face_portion = 100/one_ytm_nth # 23.137744865585784

coupon_portion= coupon * ((1-1/one_ytm_nth)/ytm) # 76.86225513441421

bond_price= face_portion + coupon_portion

ytm=0.03
n=25
face_portion = 47.76055692616592
coupon_portion =87.06573845639014
bond_price = 134.82629538255605


#
# Calculation trial and error method
#
face_portion = 100/(1+ytm)**n # no coupon, only face value, par value/(1+i)**n
coupon_portion = 0
coupon_interval = coupon/(1+ytm)
coupon_portion += coupon_interval

for i in range(2,n+1):
    print('i={}, {}'.format(i, coupon_interval))
    coupon_interval = coupon_interval/(1+ytm)
    coupon_portion += coupon_interval



