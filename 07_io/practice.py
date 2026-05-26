# 07_io/practice.py
# 입출력 (Input/Output) 학습

# 1. 표준 입출력
print("Python", "Java", sep=", ", end="?") # 구분자(sep), 끝부분(end) 지정
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

# 2. 정렬 포맷팅
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # subject를 8칸 공간 좌측 정렬, score를 4칸 공간 우측 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 3. 사용자 입력 (input)
# input()으로 입력받는 값은 항상 '문자열(str)' 타입입니다.
# user_input = input("아무 글자나 입력해보세요: ")
# print(f"입력하신 글자: {user_input}")

# 4. 파일 입출력
print("\n--- 파일 쓰기 ---")
# 'w': write (덮어쓰기)
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 'a': append (이어쓰기)
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100\n")
score_file.close()

print("--- 파일 읽기 ---")
# 'r': read (읽기)
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # 전체 읽기
score_file.close()

# 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# 5. with 문 (파일을 열고 자동으로 닫아줌)
print("\n--- with 문 사용 ---")
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
