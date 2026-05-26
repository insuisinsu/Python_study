# 02_operators/practice.py
# 연산자 (Operators) 학습

# 1. 산술 연산자 (+, -, *, /, %, //, **)
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
