# 추첨하여 1명은 치킨, 3명은 커피 쿠폰
# 조건1 : 20명이 참가함. 아이디는 1~20
# 조건2 : 임의의 숫자를 뽑되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 활용
# sample
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

from random import *

# lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 직접 나열하는 방법
lis = list(range(1, 21)) # range 함수를 이용하는 방법

winners = sample(lis, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

