# 50명의 승객 중 매칭되는 승객 수
# 운행 소요 시간은 5 ~ 50 분
# 5 ~ 15 분 승객만 매칭 가능

from random import *

totalCnt = 0

for i in range(1, 51):
    minute = randint(5, 50)
    if minute >= 5 and minute <= 15:
        totalCnt += 1
        print("[O] 승객 {0} : {1}분".format(i, minute))
    else:
        print("[ ] 승객 {0} : {1}분 (매칭 실패)".format(i, minute))
print(f"총 매칭된 승객 수는 {totalCnt}명 입니다.") 