# 03_strings/practice.py
# 문자열 처리 (String Processing) 학습

# 1. 문자열 선언 & 줄바꿈 (Multiline String)
print("--- 문자열 선언 & 줄바꿈 ---")
sentence = "안녕하세요. 파이썬 공부 중입니다."
print(sentence)

sentence2 = """
여러 줄의 문자열을
입력하고 싶을 때는
따옴표 3개를 사용합니다.
"""
print(sentence2)

# 2. 슬라이싱 (Slicing) - 특정 부분만 가져오기
print("--- 슬라이싱 ---")
jumin = "990123-1234567"
print("성별: " + jumin[7])            # 7번째 인덱스 문자: 1
print("연도: " + jumin[0:2])          # 0번째 부터 2 직전까지 (0, 1): 99
print("생년월일: " + jumin[:6])       # 처음부터 6 직전까지: 990123
print("뒤 7자리: " + jumin[7:])       # 7번째 인덱스 부터 끝까지: 1234567
print("뒤 7자리(역순): " + jumin[-7:]) # 뒤에서 7번째부터 끝까지: 1234567

# 3. 문자열 처리 함수
print("--- 문자열 처리 함수 ---")
python = "Python is Amazing"
print(python.lower())        # 소문자로: python is amazing
print(python.upper())        # 대문자로: PYTHON IS AMAZING
print(python[0].isupper())   # 0번째 문자가 대문자인지: True
print(len(python))           # 문자열 길이: 17
print(python.replace("Python", "Java")) # 문자열 대체: Java is Amazing

index = python.index("n")
print(index)                 # "n"의 첫 위치: 5
index = python.index("n", index + 1)
print(index)                 # 2번째 "n" 의 위치: 15

print(python.find("Java"))   # 문자열이 없으면 -1 반환
# print(python.index("Java")) # index()는 에러 발생
print(python.count("n"))     # "n"이 나온 횟수: 2

# 4. 문자열 포맷팅 (Formatting)
print("--- 문자열 포맷팅 ---")
# 방법 1: % 사용 (C언어 스타일)
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요" % ("노란","하늘"))
print("나는 %03d살입니다." % 20) # %03d는 숫자를 세자리로 표현하고 앞을 0으로 채운다.

# 방법 2: format() 함수 사용
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 순서 지정
print("나는 {0}살이며, {1}색을 좋아해요".format(20,"하늘"))
print("나는 {age}살이며, {color}색을 좋아해요.")
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "노란"))

# 방법 3: f-string (파이썬 3.6 이상 추천!)
age = 20
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 5. 탈출 문자
print("백문이 불여일견\n이보단 일견") # \n: 줄바꿈
print('이것은 "따옴표" 입니다.') # \: 따옴표
print("이것은 \"따옴표\" 입니다.") # \ (따옴표)
print("이것은 \t 탭 입니다.") # \t: 탭 (공백)
print("이것은 \b 백스페이스 입니다.") # \b: 백스페이스 (한글자 지움)
print("이것은 \r 캐리지 리턴 입니다.") # \r: 캐리지 리턴 (커서를 맨 앞으로 이동)
print("이것은 \f 폼 피드 입니다.") # \f: 폼 피드 (새 페이지로 이동)
print("이것은 \\ 역슬래시 입니다.") # \ (역슬래시)
# print("파일은 C:\Users\바탕화면\Documents 에 있습니다.") # 에러 발생원인 : \U, \D 가 탈출문자로 인식됨
print("파일은 C:\\Users\\바탕화면\\Documents 에 있습니다.")
