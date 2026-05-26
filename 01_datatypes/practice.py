# 01_datatypes/practice.py
# 자료형 (Data Types) 학습

# 1. 숫자형 (Numbers)
print(5)
print(-10)

# 2. 문자열 (Strings)
print('그렇다고')
print("ㅎㅋㅎㅋ")
print("ㅎㅋ" * 5)

# 3. 불리언 (Booleans)
print(5 > 10)
print(15 > 10)

# 4. 변수 (Variables)
# 애완동물 소개
name = '해피'
age = 4
print("우리집 강아지 이름은 " + name)
print(name + "는 " + str(age) + "살이요") # 숫자를 문자열로 변환 (str)
print(name + "는 빨리 자라요")
print(name + "는 꼬리를 흔들어요")
print(name + "는 귀여워요")

# print() 를 여러번 사용할 때 줄바꿈을 없애기 위해 end=" " 사용
print("우리집 강아지 이름은 " + name, end=" ")
print(name + "는 " + str(age) + "살이요", end=" ")
print(name + "는 빨리 자라요", end=" ")
print(name + "는 꼬리를 흔들어요", end=" ")
print(name + "는 귀여워요")


# + 를 넣으면 붙여쓰기
print(name + str(age) + "빨리자라요" + "꼬리를흔들어요" + "귀여워요")
print(name , str(age), "빨리 자라요", "꼬리를 흔들어요", "귀여워요")