# 02_operators/practice.py
# 연산자 (Operators) 학습

# 1. 산술 연산자 (+, -, *, /, %, //, **)
from random import randrange
print("--- 산술 연산자 ---")
print(1 + 1) # 더하기: 2
print(3 - 2) # 빼기: 1
print(5 * 2) # 곱하기: 10
print(6 / 3) # 나누기: 2.0 (실수형 반환)
print(2 ** 3) # 거듭제곱 (2의 3제곱): 8
print(5 % 3) # 나머지: 2
print(5 // 3) # 몫: 1

# 2. 비교 연산자 (>, >=, <, <=, ==, !=)
print("--- 비교 연산자 ---")
print(10 > 3) # True
print(4 >= 7) # False
print(5 == 5) # True
print(5 != 3) # True

# 3. 논리 연산자 (and, or, not)
print("--- 논리 연산자 ---")
print((3 > 0) and (3 < 5)) # True (둘 다 참이어야 True)
print((3 > 0) or (3 > 5))  # True (하나라도 참이면 True)
print(not (3 > 0))         # False (참을 거짓으로, 거짓을 참으로)

# 4. 복합 대입 연산자 (+=, -=, *=, /= 등)
print("--- 복합 대입 연산자 ---")
number = 10
number += 2 # number = number + 2 와 동일
print(number) # 12
number -= 3
print(number) # 9
number *= 2
print(number) # 18
number /= 2
print(number) # 9.0
number %= 2
print(number) # 1.0
number //= 2
print(number) # 0.0
number **= 2
print(number) # 0.0

# 5. 수식
print("--- 수식 ---")
print(2 + 3 * 4 ) # 14
print((2 + 3) * 4 ) # 20

# 6. 숫자처리 함수
print("--- 숫자처리 함수 ---")
print(abs(-5)) #절대값 # 5
print(pow(2, 3)) #거듭제곱 # 8
print(round(2.5)) #반올림 # 2
print(int(2.99)) #버림 # 2
print(float(2)) #실수형 변환 # 2.0

# 7. math 라이브러리 함수
print("--- math 라이브러리 함수 ---")
from math import *
print(sqrt(9)) # 제곱근 # 3.0
print(ceil(2.2)) # 올림 # 3
print(floor(2.8)) # 버림 # 2
print(max(1, 2, 3, 4, 5)) # 최댓값 # 5
print(min(1, 2, 3, 4, 5)) # 최솟값 # 1


# 8. random 라이브러리 함수
print("--- random 라이브러리 함수 ---")
from random import *
print(random()) # 0.0에서 1.0 사이의 실수 난수
print(int(random() * 10)) # 0에서 9 사이의 정수 난수
print(int(random() * 10 + 1)) # 1에서 10 사이의 정수 난수
print(randint(1, 10)) # 1에서 10 사이의 정수 난수
print(randrange(1, 11)) # 1에서 10 사이의 정수 난수
print(choice([1, 2, 3, 4, 5])) # 1에서 5 사이의 정수 중 하나 선택
print(choice(["가위", "바위", "보"])) # 가위, 바위, 보 중 하나 선택



