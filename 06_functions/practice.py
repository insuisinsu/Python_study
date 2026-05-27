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

# 반환값이 여러 개일 경우
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

# 결과값을 변수에 담아 사용
balance = deposit(balance, 1000)
result = withdraw_night(balance, 500)
print(f"수수료 {result[0]}, ", f"잔액: {result[1]}")

# 반환값을 변수에 각각 할당
balance2 = 1000
commission2, balance2 = withdraw_night(balance2, 500)
print(f"수수료 {commission2}, ", f"잔액: {balance2}")

# 변수 여러개에 한꺼번에 할당 (Tuple Unpacking)
balance3, commission3 = withdraw_night(1000, 500)
print(f"수수료 {commission3}, ", f"잔액: {balance3}")



# 3. 기본값 (Default values)
def profile(name, age=17, main_lang="파이썬"):
    print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")

profile("유재석") # 기본값 적용
profile("김태호", 25, "자바")

# 키워드 - 인자의 순서를 바꾸어도 됨
profile(main_lang="자바", age=25, name="김태호")


# 4. 가변인자 (Variable arguments: *args)
def profile_with_hobbies(name, age, *hobbies):
    print(f"이름: {name}\t나이: {age}", end="\t")
    print("취미:", end=" ")
    for hobby in hobbies:
        print(hobby, end=" ")
    print()

profile_with_hobbies("유재석", 20, "Python", "Java", "C", "C++")
profile_with_hobbies("송강호", 25, "영화", "독서")
profile_with_hobbies("송강호", 25, ["영화", "독서"]) # 리스트가 그대로 출력됨 -> * args 로 변경하면 해결
hobbies = ["영화", "독서"] 
profile_with_hobbies("송강호", 25, *hobbies)


# 5. 지역변수와 전역변수
gun = 10

# 전역 변수를 사용
def checkpoint(soldiers): # 경계 근무 나가는 군인 수
    global gun # 전역 공간에 있는 gun 변수를 함수 내에서 사용
    gun = gun - soldiers
    print(f"[함수 내부] 남은 총: {gun}")

checkpoint(2)
print(f"전체 남은 총: {gun}")

# 지역 변수 확인
def checkpoint2():
    gun = 20    # 전역변수를 사용하지 않으면, 함수 내에서 새로운 변수가 생성됨.
    print(gun)

checkpoint2() # 20 출력
print(gun) # 8 출력

# 반환 값으로 전역 변수를 수정하는 방법 - 권장
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    return gun

gun = checkpoint_ret(gun, 2)
print(f"전체 남은 총: {gun}")

