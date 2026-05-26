# 04_data_structures/practice.py
# 자료구조 (Data Structures) 학습

# 1. 리스트 (List) - 순서가 있고 수정 가능한 목록
print("--- 리스트 (List) ---")
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 위치 찾기
print(subway.index("조세호")) # 1

# 추가
subway.append("하하") # 맨 뒤에 추가
print(subway)

subway.insert(1, "정형돈") # 1번 인덱스에 삽입
print(subway)

# 꺼내기
print(subway.pop()) # 맨 뒤 요소 꺼내기 및 삭제
print(subway)

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]
num_list.clear()
print(num_list) # []

# 2. 딕셔너리 (Dictionary) - Key와 Value 쌍
print("\n--- 딕셔너리 (Dictionary) ---")
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 유재석
print(cabinet.get(5)) # None (대괄호[]는 에러를 내지만 get()은 None 반환)
print(cabinet.get(5, "사용 가능")) # 값이 없으면 기본값 출력

# Key 존재 여부 확인
print(3 in cabinet) # True

# 값 추가 및 변경
cabinet["C-20"] = "서장훈"
cabinet[3] = "김종국" # 기존 값 변경
print(cabinet)

# 삭제
del cabinet[3]
print(cabinet)

# Key, Value 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 3. 튜플 (Tuple) - 순서가 있으나 수정 불가능 (속도가 빠름)
print("\n--- 튜플 (Tuple) ---")
menu = ("돈까스", "치즈까스")
print(menu[0])
# menu.add("생선까스") # 에러 발생! 값 추가/변경 불가

# 4. 세트 (Set) - 중복 안됨, 순서 없음 (집합)
print("\n--- 세트 (Set/집합) ---")
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3} (중복 제거됨)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python) # {'유재석'}
print(java.intersection(python))

# 합집합
print(java | python) # {'유재석', '김태호', '양세형', '박명수'}
print(java.union(python))

# 차집합
print(java - python) # {'김태호', '양세형'}
print(java.difference(python))

# 값 추가/삭제
python.add("김종국")
python.remove("유재석")
print(python)
