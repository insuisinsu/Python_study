# 09_exceptions/practice.py
# 예외처리 (Exception Handling) 학습

# 1. 예외처리 기본 구조 (try-except)
print("--- 나누기 계산기 ---")
try:
    nums = []
    # 주석을 풀고 실행해보세요.
    # nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    # nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    # nums.append(int(nums[0] / nums[1]))
    
    # 예시 실행 코드
    nums.append(6)
    nums.append(0) # 0으로 나누기 에러 유도
    nums.append(int(nums[0] / nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다. 숫자만 입력하세요.")
except ZeroDivisionError as err:
    print(f"에러! 0으로 나눌 수 없습니다. ({err})")
except Exception as err:
    print(f"알 수 없는 에러가 발생했습니다: {err}")

# 2. 에러 발생시키기 (raise) & 사용자 정의 예외
class BigNumberError(Exception): # 사용자 정의 에러 클래스
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("\n--- 한 자리 숫자 나누기 전용 계산기 ---")
    num1 = 15 # 에러 발생을 위해 두 자리 수 설정
    num2 = 5
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값: {num1}, {num2} (두 자리 수는 입력할 수 없습니다.)")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
except BigNumberError as err:
    print(f"에러가 발생했습니다. {err}")
finally: # 에러 여부와 상관없이 무조건 실행되는 구문
    print("계산기를 이용해 주셔서 감사합니다.")
