# 10_modules_packages/practice.py
# 모듈과 패키지 (Modules and Packages) 학습

# 1. 외장 모듈 임포트 (모듈 파일을 통째로 가져오기)
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# 2. from ~ import 구문 사용 (특정 클래스/함수만 직접 가져오기)
from travel.vietnam import VietnamPackage
trip_to2 = VietnamPackage()
trip_to2.detail()

# 3. from ~ import * 사용 (__init__.py 파일에 __all__이 정의되어 있어야 함)
from travel import *
trip_to3 = thailand.ThailandPackage()
trip_to3.detail()

# 4. 내장 함수 (Built-in Functions)
# input(), type(), dir() 등
print(dir()) # 현재 사용 가능한 네임스페이스 목록 출력

# 5. 외장 함수 (External Functions) - import 필요
print("\n--- 외장 함수 예제 (sys, os) ---")
import sys
print(sys.argv) # 실행 인수 출력

import os
print(os.getcwd()) # 현재 작업 디렉토리
if not os.path.exists("test_folder"):
    os.makedirs("test_folder")
    print("test_folder 폴더를 생성했습니다.")
else:
    os.rmdir("test_folder")
    print("test_folder 폴더를 삭제했습니다.")
