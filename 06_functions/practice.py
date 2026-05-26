# 06_functions/practice.py
# 함수 (Functions) 학습

# 1. 함수 정의와 호출
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 2. 전달값(Parameter)과 반환값(Return)
def deposit(balance, money): # 입금
    print(f"입금이 완료되었습니다. 잔액은 {balance + money} 원입니다.")
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance - money} 원입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance} 원입니다.")
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
balance = withdraw(balance, 1000) # 잔액 부족

# 3. 기본값 (Default values)
def profile(name, age=17, main_lang="파이썬"):
    print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")

profile("유재석") # 기본값 적용
profile("김태호", 25, "자바")

# 4. 가변인자 (Variable arguments: *args)
def profile_with_hobbies(name, age, *hobbies):
    print(f"이름: {name}\t나이: {age}", end="\t")
    print("취미:", end=" ")
    for hobby in hobbies:
        print(hobby, end=" ")
    print()

profile_with_hobbies("유재석", 20, "Python", "Java", "C", "C++")
profile_with_hobbies("송강호", 25, "영화", "독서")

# 5. 지역변수와 전역변수
gun = 10

def checkpoint(soldiers): # 경계 근무 나가는 군인 수
    global gun # 전역 공간에 있는 gun 변수를 함수 내에서 사용
    gun = gun - soldiers
    print(f"[함수 내부] 남은 총: {gun}")

checkpoint(2)
print(f"전체 남은 총: {gun}")
