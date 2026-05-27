# 05_control_flow/practice.py
# 제어문 (Control Flow) 학습

# 1. 분기문 (if)
print("--- if 조건문 ---")
weather = "비"
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지" | weather == "황사":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")


# 2. 반복문 (for)
print("\n--- for 반복문 ---")
for waiting_no in range(1, 6): # 1부터 5까지
    print(f"대기번호: {waiting_no}")

for no in range(5):
    print(f"f대기번호 : {no+1}")
    print("대기번호 : {0}".format(no+1))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print(f"{customer}님, 커피가 준비되었습니다.")



# 3. 반복문 (while)
print("\n--- while 반복문 ---")
customer = "토르"
index = 5
while index >= 1:
    print(f"{customer}님, 커피가 준비되었습니다. 호출 {index}회 남았습니다.")
    print("{0}님, 커피가 준비되었습니다. 호출 {1}회 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기 처분되었습니다.")


# customer = "이순신"
# person = "Unknown"
# while person != customer:
#     person = input("이름이 누구인가요? ")
#     if person == customer:
#         print("{0}님, 커피가 준비되었습니다.".format(customer))
#     else:
#         print("손님이 다릅니다. 다시 입력해주세요.")
    

# 4. break와 continue
print("\n--- break 와 continue ---")
absent = [2, 5] # 결석한 학생 번호
no_book = [7]   # 책을 안 가져온 학생 번호

for student in range(1, 11): # 1번부터 10번까지
    if student in absent:
        continue # 다음 학생으로 넘어가기
    elif student in no_book:
        print(f"오늘 수업 못해먹겠네. {student}번은 교무실로 따라와.")
        break # 반복문 즉시 종료
    print(f"{student}번, 책을 읽어봐.")


# 5. 한 줄 for 문
students = [1,2,3,4,5]

students = [i + 100 for i in students]
print(students)

students = ["a", "bb", "ccc", "dddd"]

students = [i.upper() for i in students]
print(students)

students = [len(i) for i in students]
print(students)