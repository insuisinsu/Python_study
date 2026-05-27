# 표준 체중 구하는 프로그램
# 남자 : 키 x 키 x 22
# 여자 : 키 x 키 x 21
# 표준 체중은 별도의 함수 내에서 계산
# 함수명: std_weight
# 전달값 :  height, gender
# 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height, gender):

    std_weight = 0

    if gender == "남":
        std_weight = height * height * 22
    elif gender == "여":
        std_weight = height * height * 21
    
    return std_weight

# 남, 175, 65
man = std_weight(175, "남")
print("키 175cm 남성의 표준 체중: {0:.2f}kg".format(man))
# 여, 167, 55
woman = std_weight(167, "여")
print("키 167cm 여성의 표준 체중: {0:.2f}kg".format(woman))



